from .models import Playlist
from rest_framework import serializers

from account.serializers import UserSerializer
class PlaylistSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Playlist
        fields = ('id', 'name', 'created_by', 'created_at_formatted')