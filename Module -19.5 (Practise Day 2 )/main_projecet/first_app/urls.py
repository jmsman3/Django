from django.urls import path , include
from .import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    # path('person/', views.person , name= 'person_page'),                   
    # path('album/', views.album , name= 'album_page' ),                   
    path('', views.home , name= 'home_page' ),       
    path('profile/', views.profile , name= 'profile_page' ),    

    # path('signup/', views.SignUp , name= 'signup_page' ),                   
    # path('login/', views.login_system , name= 'login_page' ),                   
    # path('logout/', views.logout_system , name= 'logout_page' ),   
    #                 
    # path('album_edit/<int:id>', views.album_edit , name= 'album_edit_page' ),                   
    # path('person_edit/<int:id>', views.edit_person , name= 'person_edit_page' ),                   
    # path('delete_musician/<int:id>', views.delete_musician , name= 'delete_musician' ),  
       

    path('signup/', views.SignupClass.as_view() , name= 'signup_page' ),   
    path('login/', views.LoginClass.as_view() , name= 'login_page' ),   
    path('logout/', LogoutView.as_view() , name= 'logout_page'),                  
    path('person_edit/<int:id>', views.Edit_PersonCLass.as_view() , name= 'person_edit_page' ),  
    path('album_edit/<int:id>', views.Edit_albumClass.as_view() , name= 'album_edit_page' ),   
    path('delete_musician/<int:id>', views.Delete_MusicianClass.as_view() , name= 'delete_musician' ),  

    path('person/', views.PersonView.as_view() , name= 'person_page'), 
    path('album/', views.AlbumView.as_view() , name= 'album_page' ),    
                     
]
