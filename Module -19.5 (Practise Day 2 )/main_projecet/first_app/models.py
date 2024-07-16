from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.
class MusicianModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(help_text='Enter a valid email address')
    phone = models.CharField(max_length=12 , help_text='Enter a phone number maximum 12 digits')
    instrument = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class AlbumModel(models.Model):
    album_name = models.CharField(max_length=30)
    musician = models.ForeignKey(MusicianModel , on_delete= models.CASCADE)
    album_release_date = models.DateField()
    rate_choices =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"),) 

  
    rating = models.CharField( max_length=1, choices= rate_choices)


    def __str__(self):
        return f'{self.album_name} - {self.musician}'
