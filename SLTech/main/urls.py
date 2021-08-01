from django.urls import path
from . import views


urlpatterns = [
    path('main', views.index, name='main'),
    path('about-us', views.about),
]