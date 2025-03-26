from rest_framework import generics
from django.contrib.auth import get_user_model
from api.serializers.users.userCreateSerializer import UserCreateSerializer
User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
