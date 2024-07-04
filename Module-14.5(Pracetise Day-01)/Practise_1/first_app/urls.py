from django.urls import path,include
from . import views
urlpatterns = [
    path('index/', views.index , name='homepage'),
    path('model/', views.modell , name='homepage'),
]
