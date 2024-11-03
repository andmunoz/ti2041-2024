from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, verbose_name="Nombre", help_text="Obligatorio")

    def __str__(self):
        return self.description
    

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, verbose_name="Nombre", help_text="Obligatorio")   

    def __str__(self):
        return self.description


class Post(models.Model):    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    publish_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title + " (" + self.author.get_username() + ")"
