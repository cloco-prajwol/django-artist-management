from rest_framework import generics
from api.models import Music
from api.serializers.music.musicSerializer import MusicSerializer

class MusicRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
