from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.podcasts, name="podcasts"),
    path("podcast/<str:pk>/", views.podcast, name="podcast"),
]
