from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Persona(models.Model):

    ## Nombre de la Persona
    nombre = models.CharField(max_length=100)

    ## Apellido de la Persona
    apellido = models.CharField(max_length=100)

    ## Cédula de la Persona
    cedula = models.CharField(
        max_length=9,
        help_text=_("Cédula de Identidad del usuario"),
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agrega un 0 si la longitud es de 7 carácteres.")
            ),
        ],unique=True
    )

    telefono = models.CharField(
        max_length=18, help_text=_("Número telefónico de contacto con el usuario"),
        validators=[
            validators.RegexValidator(
                r'^\(\+\d{3}\)-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números y los símbolos: ( ) - +")
            ),
        ]
    )

    ## Establece el correo de la persona
    correo = models.CharField(
        max_length=100, help_text=("correo@correo.com")
    )

    user = models.ForeignKey(User)
