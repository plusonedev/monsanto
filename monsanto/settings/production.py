from defaults import *

DEBUG = False
ALLOWED_HOSTS = [os.environ['ALLOWED_HOSTS']]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


