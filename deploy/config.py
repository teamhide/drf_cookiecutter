"""
Have to change below things

- cluster
- task_family
- version_prefix
- NGINX image url
- WEB image url
"""

class BaseConfig(object):
    BASE = {'region': 'ap-northeast-2',
            'cluster': 'CLUSTER_NAME_HERE',
            'task_family': 'TASK_FAMILY_HERE',
            'version_prefix': 'VERSION_PREFIX_HERE',
            'decrease_instance_count': 2,
            'increase_instance_count': 4,
            'service_maximum_percent': 200,
            'service_minimum_healthy_percent': 100,
            'ecs_service_role': 'ECS_SERVICE_ROLE_HERE',
            'alb_target_group': 'ALB_TARGET_GROUP_HERE'
            }


class ProductionConfig(BaseConfig):
    NGINX = {'name': 'nginx',
             'image': 'NGINX_IMAGE_HERE',
             'memory': 200,
             'cpu': 100,
             'port': 80,
             'aws_log_group': 'nginx',
             'aws_log_stream_prefix': 'nginx',
             'links': 'web_service'
             }
    WEB = {'name': 'web_service',
           'image': 'WEB_IMAGE_HERE',
           'memory': 200,
           'cpu': 100,
           'port': 5000,
           'aws_log_group': 'web_service',
           'aws_log_stream_prefix': 'web_service'
           }

    NGINX.update(BaseConfig.BASE)
    WEB.update(BaseConfig.BASE)


class TestingConfig(BaseConfig):
    NGINX = {'name': 'nginx',
             'image': 'NGINX_IMAGE_HERE',
             'memory': 200,
             'cpu': 100,
             'port': 80,
             'aws_log_group': 'nginx',
             'aws_log_stream_prefix': 'nginx',
             'links': 'web_service'
             }
    WEB = {'name': 'web_service',
           'image': 'WEB_IMAGE_HERE',
           'memory': 200,
           'cpu': 100,
           'port': 5000,
           'aws_log_group': 'web_service',
           'aws_log_stream_prefix': 'web_service'
           }

    NGINX.update(BaseConfig.BASE)
    WEB.update(BaseConfig.BASE)
