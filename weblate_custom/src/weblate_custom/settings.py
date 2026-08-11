import os
# Import * to ensure all base Docker settings, database configurations, and static definitions load correctly
from weblate.settings_docker import *

AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + (
    'weblate_custom.oidc.CustomOidcPkceAuth',
)

# Pull secrets safely from the environment
SOCIAL_AUTH_CUSTOM_OIDC_PKCE_KEY = os.environ.get('SOCIAL_AUTH_CUSTOM_OIDC_PKCE_KEY')
SOCIAL_AUTH_CUSTOM_OIDC_PKCE_SECRET = os.environ.get('SOCIAL_AUTH_CUSTOM_OIDC_PKCE_SECRET')
SOCIAL_AUTH_CUSTOM_OIDC_PKCE_OIDC_ENDPOINT = os.environ.get('SOCIAL_AUTH_CUSTOM_OIDC_PKCE_OIDC_ENDPOINT')
