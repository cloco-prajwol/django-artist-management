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
from api.views.artist.create import ArtistCreateView
from api.views.artist.list import ArtistListView
from api.views.artist.retriveUpdateDestroy import ArtistDetailView
from api.views.artist.retriveWithMusic import ArtistDetailWithMusicListView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/artist/create/', ArtistCreateView.as_view(), name='artist_create'),
    path('api/artist/list/', ArtistListView.as_view(), name='artist_list'),
    path('api/artist/<int:pk>', ArtistDetailView.as_view(), name='artist_detail'),
    path('api/artist/<int:pk>/detail', ArtistDetailWithMusicListView.as_view(), name='artist_with_music_detail'),




]
