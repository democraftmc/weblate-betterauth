from weblate.settings_docker import AUTHENTICATION_BACKENDS

AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + (
    'custom_backends.CustomOidcPkceAuth',
)
