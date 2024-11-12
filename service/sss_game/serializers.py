from rest_framework import serializers

from sss_game.models import SssGame


class SsSerializers(serializers.ModelSerializer):
    class Meta:
        model =  SssGame
        fields = ('__all__')

