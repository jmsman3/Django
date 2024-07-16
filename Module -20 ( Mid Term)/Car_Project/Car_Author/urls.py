
from django.urls import path ,include
from .import views
urlpatterns = [

    # path('signup/', views.signup_user ,name='signup'),
    path('login/', views.login_user ,name='login'),
    path('logout/', views.logout_user ,name='logout'),
    # path('edit_profile/', views.edit_profile ,name='edit_profile'),
    # path('edit_profile/', views.edit_profile ,name='edit_profile'),
    path('password_change/', views.password_change ,name='password_change'),

    path('edit_profile/<int:id>', views.Edit_PersonCLass.as_view() , name= 'edit_profile' ),  
    path('signup/', views.SignupClass.as_view() , name= 'signup' ),   

]

