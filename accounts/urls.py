from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_registration,name='user-registration'),
    path('user-login',views.user_login,name='user-login'),
    path('user-logout',views.user_logout,name='user-logout'),
    path('home',views.home,name='home'),

]