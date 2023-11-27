from functools import wraps
from django.shortcuts import render
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, BlacklistMixin
from rest_framework.exceptions import AuthenticationFailed


def authenticate_tokens(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        access_token_cookie = request.COOKIES.get('access_token')
        refresh_token_cookie = request.COOKIES.get('refresh_token')

        if access_token_cookie is None or refresh_token_cookie is None:
            return render(request, 'main.html')

        try:
            access_token_obj = AccessToken(access_token_cookie)
            refresh_token_obj = RefreshToken(refresh_token_cookie)

        except Exception as e:
            try:
                refresh_token_obj = RefreshToken(refresh_token_cookie)
                new_access_token = refresh_token_obj.access_token

                response = render(request, 'home_page.html')
                response.set_cookie('access_token', str(new_access_token), httponly=True)

                return response
            except Exception as e:
                raise AuthenticationFailed({'detail': 'Invalid tokens'})

        if isinstance(access_token_obj, BlacklistMixin) and access_token_obj.blacklisted:
            raise AuthenticationFailed({'detail': 'Token is blacklisted'})
        
        return view_func(request, *args, **kwargs)
    
    return wrapper
        
