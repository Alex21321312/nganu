from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu' ),
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/<str:username>/', views.edit_user, name='edit_user'),
    path('delete_user/<str:username>/', views.delete_user, name='delete_user'),
    path('logout/', views.logout_view, name='logout')
]