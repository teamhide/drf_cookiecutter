from .base import *  # noqa

debug = DEBUG  # Prevent import optimization

DATABASES = {
    'default': {},
    'mongo': {
        'NAME': 'develop',
        'CONNECTION': '127.0.0.1:27017'
    }
}
