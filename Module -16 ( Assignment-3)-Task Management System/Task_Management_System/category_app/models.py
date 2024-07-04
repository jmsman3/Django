from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    Category_Name = models.CharField(max_length=100)
  

    def __str__(self):
        return f"{self.Category_Name}"