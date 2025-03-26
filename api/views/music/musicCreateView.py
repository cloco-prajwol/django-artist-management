from rest_framework import generics
from api.models import Music
from api.serializers.music.musicSerializer import MusicSerializer

class MusicCreateView(generics.CreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
