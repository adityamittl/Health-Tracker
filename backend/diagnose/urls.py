from django.urls import path
from .views import *
urlpatterns = [
    path('',index),
    path('diagnose',diagnose),
    path('social',social_help),
]