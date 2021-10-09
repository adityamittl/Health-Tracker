from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='dashboard'),
    path('diagnose',diagnose),
    path('social',social_help),
]