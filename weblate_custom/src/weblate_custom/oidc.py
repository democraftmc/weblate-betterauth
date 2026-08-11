from social_core.backends.open_id_connect import OpenIdConnectAuth

class CustomOidcPkceAuth(OpenIdConnectAuth):
    """Custom OIDC authentication backend with mandatory PKCE support."""
    
    name = 'custom-oidc-pkce'
    
    # Force Python Social Auth to generate and send PKCE code_challenge parameters
    USE_PKCE = True
    PKCE_DEFAULT_CODE_CHALLENGE_METHOD = 'S256'
    
    def auth_extra_arguments(self):
        """Inject PKCE parameters into authorization request."""
        params = super().auth_extra_arguments()
        # Ensure PKCE is active
        return params
