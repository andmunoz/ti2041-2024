from django.db import models
from django.utils import timezone


class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, null=False)


class Apoderado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, null=False)
    contacto = models.TextField(null=False)


class Mascota(models.Model):
    GENEROS_MASCOTA = {
        "H": "Hembra",
        "M": "Macho"
    }

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, default="Sin nombre")
    apoderado = models.OneToOneField(Apoderado, null=False, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, null=False, on_delete=models.CASCADE)
    raza = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=GENEROS_MASCOTA)
    tamano = models.FloatField(null=False)
    peso = models.FloatField(null=False)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(default=timezone.now)


class DatosComunes(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(null=False)

    class Meta:
        abstract = True


class Medicamento(DatosComunes):
    id = models.AutoField(primary_key=True)


class Procedimiento(DatosComunes):
    id = models.AutoField(primary_key=True)


class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(Mascota, null=False, on_delete=models.CASCADE)
    medicamentos = models.ManyToManyField(Medicamento, through="Prescripcion")
    procedimientos = models.ManyToManyField(Procedimiento, through="Prescripcion")
    fecha_receta = models.DateField(default=timezone.now)

    class Meta: 
        ordering = ["fecha_receta"]


class Prescripcion(models.Model):
    mascota = models.ForeignKey(Mascota, null=False, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta)
    dosis = models.CharField(max_length=100)
    examen = models.ForeignKey(Procedimiento)

