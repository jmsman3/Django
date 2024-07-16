from django.db import models
from catagories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)  #ekta post e multiple category thakte pare abar ekta category er under e multiple post thakte pare.
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title 