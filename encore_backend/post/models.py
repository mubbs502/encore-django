import uuid
from django.db import models
from account.models import User
from django.utils.timesince import timesince
# Create your models here.
from django.utils import timezone
class Song(models.Model):
    id = models.CharField(primary_key=True, max_length=255, unique=True, editable=True)
    
    

'''
{
  "type": "track",
  "id": "tra.187005746",
  "index": 3,
  "disc": 1,
  "href": "https://api.napster.com/tracks/tra.187005746",
  "playbackSeconds": 114,
  "isAvailableInHiRes": false,
  "isExplicit": false,
  "name": "Ride",
  "isrc": "USAT11500598",
  "shortcut": "twenty-one-pilots/blurryface/ride",
  "blurbs": [],
  "artistName": "twenty one pilots",
  "artistId": "art.47489397",
  "albumName": "Blurryface",
  "formats": [
    {
      "type": "format",
      "bitrate": 310,
      "name": "AAC",
      "sampleBits": 16,
      "sampleRate": 44100
    },
    {
      "type": "format",
      "bitrate": 191,
      "name": "AAC",
      "sampleBits": 16,
      "sampleRate": 44100
    },
    {
      "type": "format",
      "bitrate": 64,
      "name": "AAC PLUS",
      "sampleBits": 16,
      "sampleRate": 44100
    }
  ],
  "losslessFormats": [
    {
      "type": "format",
      "bitrate": 44100,
      "name": "FLAC",
      "sampleBits": 16,
      "sampleRate": 44100
    }
  ],
  "albumId": "alb.187005743",
  "contributors": {
    "primaryArtist": "art.47489397"
  },
  "links": {
    "artists": {
      "ids": [
        "art.47489397"
      ],
      "href": "https://api.napster.com/artists/art.47489397"
    },
    "albums": {
      "ids": [
        "alb.187005743"
      ],
      "href": "https://api.napster.com/albums/alb.187005743"
    },
    "genres": {
      "ids": [
        "g.351",
        "g.1045",
        "g.33"
      ],
      "href": "https://api.napster.com/genres/g.351,g.1045,g.33"
    },
    "tags": {
      "ids": [
        "tag.151196505"
      ],
      "href": "https://api.napster.com/tags/tag.151196505"
    }
  },
  "previewURL": "https://listen.hs.llnwd.net/g3/1/7/4/7/6/1174767471.mp3",
  "isStreamable": true
}
'''

class Playlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    
    # upvotes
    # upvotes_count
    # downvotes
    # downvotes_count
    # saves
    # saves_count
    # plays
    # plays_count
    # tags
    # tags_count

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='playlists', on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, blank=True)

    class Meta:
        ordering = ('-created_at',)
    
    def created_at_formatted(self):
        return timesince(self.created_at)
        
