from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shortsurls', views.shorten_url, name='shorten_url'),
]