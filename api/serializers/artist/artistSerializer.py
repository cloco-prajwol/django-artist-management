from rest_framework import serializers
from api.models import Artist
from rest_framework.validators import UniqueValidator

class ArtistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Artist.objects.all())]
    )
    class Meta:
        model = Artist
        fields = ['id','name','first_release_year','no_of_album_release','dob','gender','address'] 



