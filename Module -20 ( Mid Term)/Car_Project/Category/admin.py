from django.contrib import admin
from Category.models import CarModel ,CategoryModel ,Comment ,Order
# Register your models here.
admin.site.register(CarModel)
# admin.site.register(CategoryModel )

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name' ,)}
    list_display = ['name' , 'slug']

admin.site.register( CategoryModel , CategoryAdmin)
admin.site.register( Comment)
admin.site.register( Order)
