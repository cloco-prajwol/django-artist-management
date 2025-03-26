from rest_framework import generics
from api.models import Artist
from api.serializers.artist.artistSerializer import ArtistSerializer
from rest_framework import filters

class ArtistListView(generics.ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name', 'first_release_year']
        
