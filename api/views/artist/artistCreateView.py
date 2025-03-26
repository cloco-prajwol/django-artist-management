from rest_framework import generics
from api.models import Artist
from api.serializers.artist.artistSerializer import ArtistSerializer

class ArtistCreateView(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
