from social_core.backends.open_id_connect import OpenIdConnectAuth

class CustomOidcPkceAuth(OpenIdConnectAuth):
    """Custom OIDC authentication backend with mandatory PKCE support."""
    
    name = 'custom-oidc-pkce'
    
    # social_core handles standard OIDC discovery, token exchange, 
    # and automatic PKCE/S256 code verifier generation out-of-the-box.
