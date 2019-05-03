from .base import *  # noqa

debug = DEBUG  # Prevent import optimization

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'mongo': {
        'NAME': 'product',
        'CONNECTION': '127.0.0.1:27017'
    }
}
