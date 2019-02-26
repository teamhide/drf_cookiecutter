class TaskDefinitionBuilder:
    def __init__(self, obj):
        self.obj = obj

    def make(self) -> dict:
        class_obj = {
            'name': self.obj['name'],
            'image': self.obj['image'],
            'cpu': self.obj['cpu'],
            'memory': self.obj['memory'],
            'portMappings': [
                {
                    'containerPort': self.obj['port'],
                    'hostPort': self.obj['port'],
                    'protocol': 'tcp'
                }
            ],
            'essential': True,
            'privileged': False,
            'readonlyRootFilesystem': False,
            'logConfiguration': {
                'logDriver': 'awslogs',
                'options': {
                    'awslogs-group': self.obj['aws_log_group'],
                    'awslogs-region': self.obj['region'],
                    'awslogs-stream-prefix': self.obj['aws_log_stream_prefix']
                }
            }
        }
        if 'links' in self.obj:
            class_obj['links'] = [self.obj['links']]
        return class_obj
