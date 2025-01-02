from rest_framework_simplejwt.tokens import RefreshToken

def get_token(user):
    """
    @user take the user instance.
    @response -> return refresh token and access token.
    """
    refresh = RefreshToken.for_user(user)
    return str(refresh), str(refresh.access_token)