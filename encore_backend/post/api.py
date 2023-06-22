from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PlaylistSerializer
from .models import Playlist
# Create your views here.
from .forms import PlaylistForm
@api_view(['GET'])
def playlist_list(request):
    playlists = Playlist.objects.all()

    serialzer = PlaylistSerializer(playlists, many=True)

    return JsonResponse(serialzer.data, safe=False)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def playlist_item(request, name):
    try:
        playlist = Playlist.objects.get(name=name)
        print(playlist)
    
    
        serialzer = PlaylistSerializer(playlist, many=False)
        
        return JsonResponse(serialzer.data, safe=False)
    except Playlist.DoesNotExist as e:
        print(e)
        return JsonResponse({'error': 'Some error, add later'})


    

@api_view(['POST'])
def playlist_create(request):
    
    form = PlaylistForm(request.data)

    if form.is_valid():

        post = form.save(commit=False)
        post.created_by = request.user
        post.save()
        serializer = PlaylistSerializer(post)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'Some error, add later'})
