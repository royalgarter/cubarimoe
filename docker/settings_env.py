from cubarimoe.settings.base import *
import os

ALLOWED_HOSTS = ["*"]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": os.getenv('MEMCACHED') or "localhost:11211",
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv('DB_NAME') or "kacubarimoe",
        "USER": os.getenv('DB_USER') or "POSTGRES_USER",
        "HOST": os.getenv('DB_HOST') or "localhost",
        "PORT": os.getenv('DB_PORT') or "",
        "PASSWORD": os.getenv('DB_PASS') or "POSTGRES_PASSWORD",
    }
}
