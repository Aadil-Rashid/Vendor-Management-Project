from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from rest_framework import exceptions


class CustomAuthentication(BaseAuthentication):

    def authenticate(self, request):
        try:
            header = request.META.get('HTTP_AUTHORIZATION')
            if not header:
                raise exceptions.AuthenticationFailed(
                    'ACCESS_TOKEN is required')
            access_token = str(header.split(' ')[1])
            if access_token == settings.ACCESS_TOKEN:
                return
            raise exceptions.AuthenticationFailed('Invalid ACCESSTOKEN key')
        except Exception as e:
            raise exceptions.AuthenticationFailed(str(e))
