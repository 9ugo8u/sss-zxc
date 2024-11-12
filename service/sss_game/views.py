from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from sss_game.models import SssGame
from sss_game.serializers import SsSerializers


class SsGameViewSet(ModelViewSet):
    queryset = SssGame.objects.all()
    serializer_class = SsSerializers

