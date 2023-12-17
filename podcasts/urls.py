from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.podcasts, name="podcasts"),
    path("podcast/<str:pk>/", views.podcast, name="podcast"),
    path("episodes", views.episodes, name="episodes"),
    path("episode/<str:pk>/", views.episode, name="episode"),
    path("favorites", views.favorites, name="favorites"),
    path("watched", views.watched, name="watched"),
    

]
