from django.db import models

# Create your models here.
class Perro(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField()
    genero = models.CharField(max_length=1)

    def ladrar(self):
        print("Guau")

    def __str__(self):
        return self.nombre
