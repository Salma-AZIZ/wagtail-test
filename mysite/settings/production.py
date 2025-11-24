from .base import *
import os
import dj_database_url


DEBUG = False

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/5.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STORAGES["staticfiles"][
    "BACKEND"
] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(1p*7z_$$v1xy_1ydgefm_(%nb@-2t_*!bv(s&h#u^!^2ibj%e"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]


# === DATABASE : SQLite en Production sur Render ===
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


try:
    from .local import *
except ImportError:
    pass
