import json

from django.core.validators import validate_email
from django.http import JsonResponse
from django.shortcuts import render
from oauth2_provider.views import ProtectedResourceView, ScopedProtectedResourceView, ReadWriteScopedResourceView
from rest_framework.viewsets import ModelViewSet

from sss_game.models import SssGame
from sss_game.serializers import SsSerializers

class ReadWriteEmailView(ReadWriteScopedResourceView):
    required_scopes = ['email', ]
    def get(self, request):
        return JsonResponse({
            'email': request.user.email,
        })

    def patch(self, request):
        body = json.loads(request.body)
        email = body['email']
        validate_email(email)
        user = request.user
        user.email = email
        user.save(update_fields=['email'])

class SsGameViewSet(ModelViewSet):
    queryset = SssGame.objects.all()
    serializer_class = SsSerializers



