
from django.urls import path ,include
from .import views


urlpatterns = [

    path('profile/', views.profile ,name='profile'), 

    path('category/<slug:category_slug>/',views.home  , name='category_wise_post'),
    path('carpost/', views.carpost ,name='carpost'),
    path('brandpost/', views.brandpost ,name='brandpost'),
    path('detail/<int:id>/', views.DetailPostView.as_view(),name='detail'),
    
    path('buy_car/<int:id>/', views.buy_car,name='buy_car'),
]
