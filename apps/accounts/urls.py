from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='registration/login.html')),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]