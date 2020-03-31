from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from boards import views

urlpatterns = [
   # path('', views.home, name='home'),
   path('signup/', accounts_views.signup, name='signup'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]

