from rest_framework import generics
from django.contrib.auth import get_user_model
from api.serializers.users.userRetriveSerializer import UserRetriveSerializer
User = get_user_model()

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetriveSerializer
