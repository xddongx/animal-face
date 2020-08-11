from . import awskey

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': awskey.DB_NAME,
        'USER': awskey.DB_USER,
        'PASSWORD': awskey.DB_PASSWORD,
        'HOST': '54.180.2.233',
        'PORT': '3306',
    }
}