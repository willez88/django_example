from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Person al panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Mostrar los campos de la clase
    list_display = (
        'user', 'first_name', 'last_name', 'identification_card', 'phone'
    )

    # Seleccionar campo para filtrar
    list_filter = ('user',)

    # Seleccionar campo para ordenar
    ordering = ('first_name',)


admin.site.register(Person, PersonAdmin)
