from django.forms import ModelForm

from .models import Playlist

class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ('name',)