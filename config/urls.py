"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path
from api.views.artist.artistCreateView import ArtistCreateView
from api.views.artist.artistListView import ArtistListView
from api.views.artist.artistRetrieveUpdateDestroyView import ArtistRetrieveUpdateDestroyView
from api.views.artist.retriveWithMusicView import ArtistDetailWithMusicListView
from api.views.music.musicCreateView import MusicCreateView
from api.views.music.musicRetrieveUpdateDestroyView import MusicRetrieveUpdateDestroyView
from api.views.users.userCreateView import UserCreateView
from api.views.users.userListView import UserListView
from api.views.users.userDetailView import UserDetailView
from api.views.users.userUpdateView import UserUpdateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/artist/create/', ArtistCreateView.as_view(), name='artist_create'),
    path('api/artist/list/', ArtistListView.as_view(), name='artist_list'),
    path('api/artist/<int:pk>', ArtistRetrieveUpdateDestroyView.as_view(), name='artist_detail'),
    path('api/artist/<int:pk>/detail', ArtistDetailWithMusicListView.as_view(), name='artist_with_music_detail'),
    path('api/music/create/', MusicCreateView.as_view(), name='music_create'),
    path('api/music/<int:pk>', MusicRetrieveUpdateDestroyView.as_view(), name='music_detail'),
    path('api/user/register/', UserCreateView.as_view(), name='user_create'),
    path('api/user/list/', UserListView.as_view(), name='user_list'),
    path('api/user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('api/user/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),


]
