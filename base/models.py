from django.db import models

# Create your models here.

class Pais(models.Model):

    ## Nombre del pais
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Estado(models.Model):

    ## Nombre del Estado
    nombre = models.CharField(max_length=50)

    ## Pais en donde esta ubicado el Estado
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):

    ## Nombre del Municipio
    nombre = models.CharField(max_length=50)

    ## Estado en donde se encuentra el Municipio
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Parroquia(models.Model):

    ## Nombre de la Parroquia
    nombre = models.CharField(max_length=50)

    ## Municipio en el que se encuentra ubicada la Parroquia
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):

    ## Nombre de la Ciudad
    nombre = models.CharField(max_length=50)

    ## Estado en donde se encuentra ubicada la Ciudad
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
