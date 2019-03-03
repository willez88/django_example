from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Profile al panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-07-2018
    """

    ## Mostrar los campos de la clase
    list_display = ('user','phone')

    ## Seleccionar campo para filtrar
    #list_filter = ('user',)

    ## Seleccionar campo para ordenar
    ordering = ('user',)

admin.site.register(Profile, ProfileAdmin)
