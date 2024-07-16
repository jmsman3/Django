from django.urls import path ,include
from . import views
urlpatterns = [
  
    # path('', views.home ),
    # path('get/', views.get_cookie ),
    # path('del/', views.get_cookie ),

     
    path('', views.set_session ),
    path('get/', views.get_session ),
    path('del/', views.delete_session ),
]
