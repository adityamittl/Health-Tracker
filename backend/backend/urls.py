from django.contrib import admin
from django.urls import path,include
from blog.views import blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('diagnose.urls')),
    path('chat/',include('chat.urls')),
    path('', include('auth0login.urls')),
    path('blog',blog,name='blog')
]
