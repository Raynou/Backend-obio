from conf.common import *

DEBUG = True

# SESSION_COOKIE_SECURE = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_REDIRECT_EXEMPT = []
# SECURE_SSL_REDIRECT = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_XFORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['https://back-obio.herokuapp.com/', '127.0.0.1', '187.161.188.177']

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dabt9nr97sb8g7',
        'USER': 'upojxeufbjpedx',
        'PASSWORD': 'b58a0ba354680db668d30a85a76fa11061f487785b10de584788f9db5f1b4f49',
        'HOST': 'ec2-35-169-188-58.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}
