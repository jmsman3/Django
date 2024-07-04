from django.db import models
from django.core.validators import MinValueValidator ,MaxValueValidator
# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(help_text='enter a valid mail address')
    phone = models.CharField( max_length=12,help_text='enter a phone number maximum 12 digits')
    insturment = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class AlbumModel(models.Model):
    album_name = models.CharField(max_length=50)

    musician  = models.ForeignKey(Musician , on_delete=models.CASCADE )
    Album_Realease_Date = models.DateField()
    rating = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5)])
    def __str__(self):
        return f'{self.album_name}'

        
