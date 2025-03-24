from rest_framework import serializers
from api.models import Artist,Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['title','album_name','genre']

class ArtistMusicSerializer(serializers.ModelSerializer):
    music = MusicSerializer(many= True, read_only=True)
    class Meta:
        model = Artist
        fields = ['name','first_release_year','no_of_album_release','dob','gender','address','music'] 
