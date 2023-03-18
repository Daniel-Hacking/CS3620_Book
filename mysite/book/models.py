from django.db import models

# Create your models here.

class BookData (models.Model):


    def __str__(self):
        return self.Name

    Name=models.CharField(max_length=125)
    Category=models.CharField(max_length=30)
    Description=models.CharField(max_length=255)
    Rating=models.FloatField()
    Image=models.ImageField(upload_to='Images')