from rest_framework import generics
from api.models import Artist
from api.serializers.artist.artistWithMusic import ArtistMusicSerializer

class ArtistDetailWithMusicListView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistMusicSerializer
