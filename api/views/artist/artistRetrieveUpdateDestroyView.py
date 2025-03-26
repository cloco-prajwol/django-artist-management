from rest_framework import generics
from api.models import Artist
from api.serializers.artist.artistSerializer import ArtistSerializer

class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
