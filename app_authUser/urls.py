from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.LoginView, name='LoginView'),
    path('signup/', views.SignupView, name='SignupView'),
    path('logout/', views.LogoutView, name='LogoutView'),
]
