from django.contrib import admin
from first_app.models import MusicianModel , AlbumModel
# Register your models here.
admin.site.register(MusicianModel)
admin.site.register(AlbumModel)