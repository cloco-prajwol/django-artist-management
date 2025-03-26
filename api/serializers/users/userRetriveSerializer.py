from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
class UserRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','last_name','email','is_active','first_name','phone','dob','gender','address'] 
    