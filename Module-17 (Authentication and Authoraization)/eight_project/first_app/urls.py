from django.urls import path ,include
from . import views
urlpatterns = [
    path('',  views.home ,name='home'),
    path('signup/',  views.signup ,name='signup'),
    path('profile/',  views.profile ,name='profile'),
    path('login/',  views.user_login ,name='login'),
    path('logout/',  views.user_logout ,name='logout'),
    path('pass_change/',  views.pass_change ,name='passchange'),  
    path('pass_change2/',  views.pass_change2 ,name='passchange2'),  
]