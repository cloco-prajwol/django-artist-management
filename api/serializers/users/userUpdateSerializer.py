from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()
class UserUpdateSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    last_name = serializers.CharField(
          required=True,
    )
    first_name = serializers.CharField(
          required=True,
    )
    phone = serializers.CharField(
          required=True,
    )
    dob = serializers.CharField(
          required=True,
    )
    address = serializers.CharField(
          required=True,
    )
    gender = serializers.CharField(
          required=True,
    )

    class Meta:
        model = User
        fields = ['id','username','last_name','email','is_active','first_name','phone','dob','gender','address'] 
            
    def create(self, validated_data):
      user = get_user_model()(**validated_data)
      user.update()
      return user

