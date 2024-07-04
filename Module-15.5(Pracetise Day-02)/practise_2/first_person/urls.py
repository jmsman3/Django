from django.urls import path , include
from . import views
urlpatterns = [
 
    path('person_template/',views.person  , name='personpage' ),
    path('album_template/',views.album  , name='albumpage' ),
    path('',views.home  , name='homepage' ),
    path('person_edit/<int:id>',views.edit_person , name='edit_person' ),
    path('delete/<int:id>',views.delete_musician  , name='delete_post' ),
    path('album_edit/<int:id>',views.album_edit  , name='album_edit' ),
]
