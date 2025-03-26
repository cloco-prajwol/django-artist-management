from rest_framework import generics
from django.contrib.auth import get_user_model
from api.serializers.users.userRetriveSerializer import UserRetriveSerializer
User = get_user_model()

from rest_framework import filters

class UserListView(generics.ListAPIView):
    serializer_class = UserRetriveSerializer
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^username', 'first_name','last_name']
        
