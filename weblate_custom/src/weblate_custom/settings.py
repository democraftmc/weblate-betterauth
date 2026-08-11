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
SOCIAL_AUTH_CUSTOM_OIDC_PKCE_ALGORITHMS = ['RS256', 'HS256', 'ES256', 'EdDSA']

# Prevent Python Social Auth from requesting default ['openid', 'profile', 'email']
# SOCIAL_AUTH_CUSTOM_OIDC_PKCE_IGNORE_DEFAULT_SCOPE = True

# Define the exact scope(s) allowed by your Better Auth setup
# SOCIAL_AUTH_CUSTOM_OIDC_PKCE_SCOPE = ['openid']  # or [] if no scopes are required

