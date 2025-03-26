from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()
class UserCreateSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
          write_only=True,
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
        fields = ['id','username','last_name','email','is_active','first_name','phone','dob','gender','address','password'] 
    
    
    def __init__(self, instance=None, data=..., **kwargs):
      super().__init__(instance, data, **kwargs)
      if self.context['request'].method == 'PUT':
            print('here')
            self.fields.pop('password')

            
    def create(self, validated_data):
      user = get_user_model()(**validated_data)
      if self.context['request'].method == 'POST':
            user.set_password(validated_data['password'])
      user.save()
      return user

