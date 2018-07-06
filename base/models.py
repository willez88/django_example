from django.db import models

# Create your models here.

class Country(models.Model):

    ## Nombre del pais
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class State(models.Model):

    ## Nombre del Estado
    name = models.CharField(max_length=50)

    ## Pais en donde esta ubicado el Estado
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Municipality(models.Model):

    ## Nombre del Municipio
    name = models.CharField(max_length=50)

    ## Estado en donde se encuentra el Municipio
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):

    ## Nombre de la Ciudad
    name = models.CharField(max_length=50)

    ## Estado en donde se encuentra ubicada la Ciudad
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Parish(models.Model):

    ## Nombre de la Parroquia
    name = models.CharField(max_length=50)

    ## Municipio en el que se encuentra ubicada la Parroquia
    municipality = models.ForeignKey(Municipality,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
