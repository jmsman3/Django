
from django.urls import path , include
from . import views
urlpatterns = [
    path('profile/', views.profile , name = 'profile'),
    path('signup/', views.signup , name = 'signup'),
    path('login/', views.user_login , name = 'login'),
    path('logout/', views.user_logout , name = 'logout'),
    path('passchange/', views.pass_change , name = 'pass_change'),
    path('passchange2/', views.pass_change2 , name = 'pass_change2'),
   
]