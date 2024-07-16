from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('register/', views.register , name= 'register'),
    path('login/', views.user_login , name= 'user_login'),
    path('logout/', views.user_logout , name= 'user_logout'),
    path('profile/', views.profile , name= 'profile'),
    path('edit/', views.edit_profile , name= 'edit_profile'),
    path('edit/passchange/', views.change_pass , name= 'passchange'),
]