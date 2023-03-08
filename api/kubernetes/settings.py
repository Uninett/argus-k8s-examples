
import os  # for SERVER_EMAIL

from argus.site.settings.prod import *

###
# Environment variables to set:
# DATABASE_URL
# ARGUS_FRONTEND_URL
# ARGUS_DATAPORTEN_KEY
# ARGUS_DATAPORTEN_SECRET
# ARGUS_SEND_NOTIFICATIONS

# Fixed settings

ADMINS = [
    ('Hanne Moa', 'REDACTED@REDACTED.REDACTED'),
    ('Morten Brekkevold', 'REDACTED@REDACTED.REDACTED'),
]

DEBUG = True
# TEMPLATES[0]["OPTIONS"]["debug"] = True
# TEMPLATES[0]["DIRS"] += [FRONTEND_BUILDDIR]


ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".paas2.uninett.no",
    "*",
]

AUTH_TOKEN_EXPIRES_AFTER_DAYS = 180

SERVER_EMAIL = "argus@{}".format(os.uname()[1])
#SECURE_HSTS_SECONDS = 3600

SMS_GATEWAY_ADDRESS = "REDACTED@REDACTED.REDACTED"

MEDIA_PLUGINS = [
    'argus.notificationprofile.media.email.EmailNotification',
    'argus.notificationprofile.media.sms_as_email.SMSNotification',
]

SOCIAL_AUTH_REDIRECT_IS_HTTPS = get_bool_env("SOCIAL_AUTH_REDIRECT_IS_HTTPS", True)

CORS_ALLOWED_ORIGINS = [
    "https://argus.uninett.no",
    "https://test-argus.uninett.no",
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"https://argus-[-\w]+.paas2.uninett.no",
    r"https://test-argus-[-\w]+.paas2.uninett.no",
    r"https://[\w-]*.?argus.uninett.no",
]
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    "argus.uninett.no",
    "api.argus.uninett.no",
]
CSRF_COOKIE_SAMESITE = None

ARGUS_FALLBACK_FILTER = {"acked": False, "stateful": True}

if COOKIE_DOMAIN:
    COOKIE_URL = f"https://{COOKIE_DOMAIN}"
    if COOKIE_DOMAIN not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(COOKIE_DOMAIN)
    if COOKIE_URL not in CORS_ALLOWED_ORIGINS:
        CORS_ALLOWED_ORIGINS.append(COOKIE_URL)

SOCIAL_AUTH_IMMUTABLE_USER_FIELDS = ('id', 'pk',)
