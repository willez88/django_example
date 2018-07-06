from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from base.models import Parish

# Create your models here.

class Person(models.Model):

    ## Nombre de la Persona
    first_name = models.CharField(max_length=100)

    ## Apellido de la Persona
    last_name = models.CharField(max_length=100)

    ## Cédula de la Persona
    identification_card = models.CharField(
        max_length=9,
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agrega un 0 si la longitud es de 7 carácteres.")
            ),
        ],unique=True
    )

    phone = models.CharField(
        max_length=15,
        validators=[
            validators.RegexValidator(
                r'^\+\d{2}-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números.")
            ),
        ]
    )

    ## Establece el correo de la persona
    email = models.CharField(
        max_length=100, help_text=("correo@correo.com")
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    address = models.CharField(max_length=100)

    parish = models.ForeignKey(Parish,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s, %s' % (self.first_name, self.last_name, self.identification_card)

    class Meta:
        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')
