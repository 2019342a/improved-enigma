from .base import *  # noqa

# GENERAL
# -----------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(  # noqa F405
    "SECRET_KEY", default="SET SECRET KEY"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# APPS
# -----------------------------------------------------------------------------------
INSTALLED_APPS += ["debug_toolbar", "django_extensions"]  # noqa F405

# django-debug-toolbar
# -----------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

# MIDDLEWARE
# -----------------------------------------------------------------------------------
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
