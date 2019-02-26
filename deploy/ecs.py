import time
import boto3
from typing import List
from .task_builder import TaskDefinitionBuilder


class ECS:
    def __init__(self, config=None):
        """Default Variables"""
        self.client = boto3.client('ecs')
        self.next_version = 0
        self.current_service = ''
        self.new_task = ''
        self.old_service = ''
        self.new_service = ''
        self.config = config

    def get_service_list(self, stage: str) -> None:
        try:
            response = self.client.list_services(
                cluster=self.config.BASE['cluster'],
                maxResults=10
            )['serviceArns']
        except Exception as e:
            print(e)
            raise Exception('get_service_list() error')

        if stage == 'first':
            temp = response[0].split('service/{}'.format(self.config.BASE['version_prefix']))
            self.next_version = int(temp[1]) + 1
            self.current_service = response[0]
        elif stage == 'second':
            self.describe_service(response)
        else:
            raise Exception('Invalid stage')

        print("[*] Get Service List Done")

    def describe_service(self, service_list: dict) -> None:
        try:
            desc_response = self.client.describe_services(
                cluster=self.config.BASE['cluster'],
                services=service_list
            )
            if desc_response['services'][0]['createdAt'] < desc_response['services'][1]['createdAt']:
                self.old_service = desc_response['services'][0]['serviceName']
                self.new_service = desc_response['services'][1]['serviceName']
            else:
                self.old_service = desc_response['services'][1]['serviceName']
                self.new_service = desc_response['services'][0]['serviceName']
        except Exception as e:
            print(e)
            raise Exception('describe_service() error')

    def delete_service(self) -> None:
        try:
            self.client.delete_service(
                cluster=self.config.BASE['cluster'],
                service=self.old_service,
                force=True
            )
            print("[*] Delete Service : {}".format(self.old_service))
        except Exception as e:
            print(e)
            raise Exception('delete_service() error')

    def create_service(self, task_definition: str) -> None:
        try:
            self.client.create_service(
                cluster=self.config.BASE['cluster'],
                serviceName=self.config.BASE['version_prefix'] + str(self.next_version),
                taskDefinition=task_definition,
                loadBalancers=[
                    {
                        'targetGroupArn': self.config.BASE['alb_target_group'],
                        'containerName': self.config.NGINX['name'],
                        'containerPort': self.config.NGINX['port']
                    },
                ],
                desiredCount=2,
                launchType='EC2',
                role=self.config.BASE['ecs_service_role'],
                deploymentConfiguration={
                    'maximumPercent': self.config.BASE['service_maximum_percent'],
                    'minimumHealthyPercent': self.config.BASE['service_minimum_healthy_percent']
                },
                placementStrategy=[
                    {
                        'type': 'spread',
                        'field': 'attribute:ecs.availability-zone'
                    },
                    {
                        'type': 'spread',
                        'field': 'instanceId'
                    }
                ],
                healthCheckGracePeriodSeconds=0,
                schedulingStrategy='REPLICA',
                enableECSManagedTags=False,
            )
            print("[*] Create Service Done")
        except Exception as e:
            print(e)
            raise Exception('create_service() error')

    def update_service(self, count: int, target_service: str, task_definition: str) -> None:
        try:
            self.client.update_service(
                cluster=self.config.BASE['cluster'],
                service=target_service,
                desiredCount=count,
                taskDefinition=task_definition,
                deploymentConfiguration={
                    'maximumPercent': self.config.BASE['service_maximum_percent'],
                    'minimumHealthyPercent': self.config.BASE['service_minimum_healthy_percent']
                },
            )
            print("[*] Update Service Done")
        except Exception as e:
            print(e)
            raise Exception('update_service() error')

    def stop_task(self, task_id: str) -> None:
        try:
            self.client.stop_task(
                cluster=self.config.BASE['cluster'],
                task=task_id,
                reason='For update'
            )
            print("[*] Stop Task : {}".format(task_id))
        except Exception as e:
            print(e)
            raise Exception('stop_task() error')

    def get_task_definition_list(self) -> dict:
        try:
            response = self.client.list_task_definitions(
                familyPrefix=self.config.BASE['task_family'],
                status='ACTIVE',
                sort='DESC',
                maxResults=10
            )
            print("[*] Get Task Definition List Done")
            return response
        except Exception as e:
            print(e)
            raise Exception('get_task_definition_list() error')

    def get_task_list(self, service_name: str) -> List[str]:
        try:
            response = self.client.list_tasks(
                cluster=self.config.BASE['cluster'],
                serviceName=service_name
            )['taskArns']
            print("[*] Get Task List Done")
            return response
        except Exception as e:
            print(e)
            raise Exception('get_task_list() error')

    def register_task_definition(self, combined_task_definition: List) -> str:
        try:
            response = self.client.register_task_definition(
                family=self.config.BASE['task_family'],
                containerDefinitions=combined_task_definition,
                requiresCompatibilities=[
                    'EC2',
                ]
            )
            print("[*] Register Task Definition : {}:{}".format(
                self.config.BASE['task_family'], response['taskDefinition']['revision']))
            return response['taskDefinition']['taskDefinitionArn']
        except Exception as e:
            print(e)
            raise Exception('register_task_definition() error')

    def run_first_stage(self) -> None:
        print("[*] First Stage Start")

        """서비스 목록"""
        self.get_service_list(stage='first')
        task_list = self.get_task_list(service_name=self.current_service)

        """기존 서비스에서 작업 2개 정지"""
        self.stop_task(task_id=task_list[0])
        self.stop_task(task_id=task_list[1])

        """기존 작업정의 가져오기"""
        new_task_definition = self.get_task_definition_list()['taskDefinitionArns'][0]

        """기존 작업정의를 바탕으로 서비스 업데이트(작업 개수 2개로 축소)"""
        self.update_service(
            count=self.config.BASE['decrease_instance_count'],
            target_service=self.current_service,
            task_definition=new_task_definition
        )

        """딜레이"""
        print("[*] Wait 10sec")
        time.sleep(10)

        """새로운 작업정의 생성"""
        web_obj = TaskDefinitionBuilder(self.config.WEB).make()
        nginx_obj = TaskDefinitionBuilder(self.config.NGINX).make()
        new_task_definition = self.register_task_definition(combined_task_definition=[web_obj, nginx_obj])

        """새로운 작업정의를 바탕으로 서비스 생성(작업 개수 2개)"""
        self.create_service(task_definition=new_task_definition)
        print("[*] Finish")

    def run_second_stage(self) -> None:
        print("[*] Second Stage Start")
        """이전 버전 서비스 가져오기"""
        self.get_service_list(stage='second')

        """이전 서비스 작업 가져오기"""
        task_list = self.get_task_list(service_name=self.old_service)

        """이전 서비스 작업 중단하기"""
        self.stop_task(task_id=task_list[0])
        self.stop_task(task_id=task_list[1])

        """이전 서비스 삭제하기"""
        self.delete_service()
        print("[*] Wait 5sec")
        time.sleep(5)

        """작업정의 가져오기"""
        new_task_definition = self.get_task_definition_list()['taskDefinitionArns'][0]

        """새로운 서비스 업데이트(작업 개수 4개로 증가)"""
        self.update_service(
            count=self.config.BASE['increase_instance_count'],
            target_service=self.new_service,
            task_definition=new_task_definition
        )
        print("[*] Finish")
