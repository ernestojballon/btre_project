#SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1234s3ii&cjmkwi0v_y0(%29wav8_^7k6@p8*21uu&b9n0vc@v5)ez'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['167.99.225.57']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'btredb',
        'USER': 'btre_django',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# EMAIL config
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ernestoballono@gmail.com'
EMAIL_HOST_PASSWORD = 'sgkm2323'


