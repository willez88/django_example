from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """!
    Clase que contiene los datos del perfil de un usuario del sistema

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Teléfono
    phone = models.CharField(
        'teléfono',
        max_length=15,
        validators=[
            validators.RegexValidator(
                r'^\+\d{2}-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números.")
            ),
        ]
    )

    # Establece la relación entre el usuario del sistema con el perfil
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Usuario'
    )

    def __str__(self):
        """!
        Función para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Una cadena de caracteres con el nombre y apellido del usuario
        """

        return "%s %s" % (self.user.first_name, self.user.last_name)

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        """

        verbose_name = _('Perfil')
        verbose_name_plural = _('Perfiles')
