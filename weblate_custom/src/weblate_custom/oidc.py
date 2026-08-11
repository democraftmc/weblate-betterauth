from social_core.backends.oidc import BaseOIDCAuth

class CustomOidcPkceAuth(BaseOIDCAuth):
    """Custom OIDC authentication backend with mandatory PKCE support."""
    
    name = 'custom-oidc-pkce'
    EXTRA_DATA = [
        ('refresh_token', 'refresh_token'),
        ('expires_in', 'expires_in'),
        ('id_token', 'id_token'),
    ]

    def get_settings(self, name):
        """Override settings lookup to use custom prefix namespaces."""
        return super().get_settings(name)

    def auth_extra_arguments(self):
        """Inject any required custom parameters into the authorization request."""
        params = super().auth_extra_arguments()
        # You can add custom audience or prompt options here if needed, e.g.:
        # params['prompt'] = 'select_account'
        return params

    def compute_code_challenge(self):
        """Indicate that PKCE should be used by providing code challenge settings."""
        return True
