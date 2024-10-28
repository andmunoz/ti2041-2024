from django.db import models
from django.utils import timezone

# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre", help_text="Obligatorio")   
    class Meta:
        abstract: True
        
    def __str__(self):
        return self.name

class Category(CommonInfo):
    id_category = models.AutoField(primary_key=True)
    

class Tag(CommonInfo):
    id_tag = models.AutoField(primary_key=True)


class Post(models.Model):    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    author = models.CharField(max_length=3)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    publish_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title + " (" + self.author + ")"
