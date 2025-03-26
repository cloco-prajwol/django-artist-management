from rest_framework import serializers
from api.models import Music
from rest_framework.validators import UniqueValidator

class MusicSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        validators=[UniqueValidator(queryset=Music.objects.all())]
    )
    class Meta:
        model = Music
        fields = ['id','title','album_name','artist','genre'] 



