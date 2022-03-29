from base.models import Parish
from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    """!
    Clase que contiene las personas

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Nombre
    first_name = models.CharField('nombres', max_length=100)

    # Apellido
    last_name = models.CharField('apellidos', max_length=100)

    # Cédula de identidad
    identification_card = models.CharField(
        'cédula de identidad',
        max_length=9,
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _('Introduzca un número de cédula válido. Solo se permiten\
                números y una longitud de 8 carácteres. Se agrega un 0 si la \
                longitud es de 7 carácteres.')
            ),
        ], unique=True
    )

    # Número telefónico
    phone = models.CharField(
        'teléfono',
        max_length=15,
        validators=[
            validators.RegexValidator(
                r'^\+\d{2}-\d{3}-\d{7}$',
                _('Número telefónico inválido. Solo se permiten números.')
            ),
        ]
    )

    # Correo electrónico
    email = models.CharField(
        'correo electrónico', max_length=100, help_text=('correo@correo.com')
    )

    # Dirección
    address = models.CharField('dirección', max_length=100)

    # Relación entre la persona y la parroquia
    parish = models.ForeignKey(
        Parish, on_delete=models.CASCADE, verbose_name='parroquia'
    )

    # Relación entre la persona y el usuario del sistema
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='usuario'
    )

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return string <b>{object}</b> Objeto con el nombre, apellido y la
            cédula de identidad
        """

        return '%s %s, %s' % (
            self.first_name, self.last_name, self.identification_card
        )

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        """

        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')
