import os

django_configuration = os.getenv('DJANGO_CONFIGURATION', 'local')

if django_configuration == 'production.py':
    from .production import *
elif django_configuration == 'test':
    from .test import *
elif django_configuration == 'local':
    from .local import *
else:
    raise Exception('Setting Error')


def get_database_setting():
    return DATABASES
