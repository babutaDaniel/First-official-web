from django.urls import path
from . import views


urlpatterns = [
    path('login_users', views.login_user, name='login'),
    path('logout_users', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register')

]