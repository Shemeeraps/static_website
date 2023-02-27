from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="pictures")
    desc=models.TextField()

class actors(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="pictures")
    desc=models.TextField()
