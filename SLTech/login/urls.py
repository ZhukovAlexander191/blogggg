from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginU, name="login"),
    path('register/', views.registerU, name="register"),
    path('blog-main/', views.blog_main, name="blog-main"),
    path('logout/', views.logoutU, name="logout")
]
