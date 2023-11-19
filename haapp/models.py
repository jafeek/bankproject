from django.db import models

# Create your models here.


class place(models.Model):
     name= models.CharField(max_length=100)
     img= models.ImageField(upload_to='pic')
     desc= models.TextField()
     loan= models.IntegerField()
     offer= models.BooleanField(default=False)