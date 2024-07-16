from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100 , unique=True , null=True , blank=True)
    
    def __str__(self):
        return self.name

class CarModel(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    description = models.TextField()
    quantity = models.IntegerField(blank=True , null= True )
    brand = models.ForeignKey(CategoryModel , on_delete=models.CASCADE)
    author = models.ForeignKey( User , on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'Category/media/uploads/' , blank=True , null= True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(CarModel , on_delete=models.CASCADE , related_name= 'comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()     #unique=True dele ,ekta email deye matro ekta comment e kora jabe
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Comment by {self.name}"

class Order(models.Model):
    buyer = models.ForeignKey(User , on_delete=models.CASCADE , related_name='orders')
    car = models.ForeignKey(CarModel , on_delete=models.CASCADE , related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Order by {self.buyer.username} of this  Car - {self.car.title}"
    

