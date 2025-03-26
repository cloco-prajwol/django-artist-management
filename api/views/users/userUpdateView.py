from rest_framework import generics
from django.contrib.auth import get_user_model
from api.serializers.users.userUpdateSerializer import UserUpdateSerializer
User = get_user_model()

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
