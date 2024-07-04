from django.urls import path , include
from . import views
urlpatterns = [
    path('add_task/',views.add_task , name='TaskPage'),
    path('show_task/',views.show_task , name='ShowPage'),
    path('edit_post/<int:id>/',views.edit_post , name='EditPage'),
    path('delete_post/<int:id>/',views.delete_post , name='delete_post'),
]
