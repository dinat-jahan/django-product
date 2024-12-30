from django.http import JsonResponse
from base64 import b64decode
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.urls import resolve

class BasicAuthCheck:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_url = resolve(request.path_info).url_name
        if current_url in ['register', 'login']:
            return self.get_response(request)

        auth = request.META.get('HTTP_AUTHORIZATION')
        if auth and auth.startswith('Basic '):
            try:
                auth_decoded = b64decode(auth.split(' ')[1]).decode('utf-8')
                username, password = auth_decoded.split(':', 1)
                user = authenticate(username=username, password=password)
                if user is None:
                    raise AuthenticationFailed('Invalid credentials')
                request.user = user
            except Exception:
                raise AuthenticationFailed('Invalid authentication header')
        else:
            request.user = None
        
        response = self.get_response(request)
        return response
