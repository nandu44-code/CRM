from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_registration,name='user-registration'),
    path('user-login',views.user_login,name='user-login'),
    path('user-logout',views.user_logout,name='user-logout'),
    path('home',views.home,name='home'),
    path('special-user-home',views.special_user_home,name='special-user-home'),
    path('create-client',views.create_client,name='create-client'),
    path('update-client/<int:client_id>/', views.update_client, name='update-client'),
    path('delete-client/<int:client_id>/', views.delete_client, name='delete-client'),
    path('get-clients', views.get_clients, name='get-clients'),
    path('error-page', views.error, name='error-page'),

]