from django.views import View
from django.utils.translation import ugettext_lazy as _
from django.apps import apps
import json
from django.http import HttpResponse
from .constant import MSG_NOT_AJAX

class ComboUpdateView(View):
    """!
    Clase que actualiza los datos de un select dependiente de los datos de otro select

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 06-07-2018
    """

    def get(self, request, *args, **kwargs):
        """!
        Función que obtiene los datos recibidos por el método get

        @author William Páez (paez.william8 at gmail.com)
        @date 06-07-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene los datos de la petición
        @param *args <b>{tuple}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return response <b>{response}</b> Respuesta con los datos en formato json
        """

        try:
            if not request.is_ajax():
                return HttpResponse(json.dumps({'result': False, 'error': str(MSG_NOT_AJAX)}))

            ## Valor del campo que ejecuta la acción
            cod = request.GET.get('option', None)

            ## Nombre de la aplicación del modelo en donde buscar los datos
            app = request.GET.get('app', None)

            ## Nombre del modelo en el cual se va a buscar la información a mostrar
            mod = request.GET.get('mod', None)

            ## Atributo por el cual se va a filtrar la información
            field = request.GET.get('field', None)

            ## Atributo del cual se va a obtener el valor a registrar en las opciones del combo resultante
            n_value = request.GET.get('n_value', None)

            ## Atributo del cual se va a obtener el texto a registrar en las opciones del combo resultante
            n_text = request.GET.get('n_text', None)

            ## Nombre de la base de datos en donde buscar la información, si no se obtiene el valor por defecto es default
            bd = request.GET.get('bd', 'default')

            filter = {}

            if app and mod and field and n_value and n_text and bd:
                model = apps.get_model(app, mod)

                if cod:
                    filter = {field: cod}

                out = "<option value=''>%s...</option>" % str(_("Seleccione"))

                combo_disabled = "false"

                if cod != "" and cod != "0":
                    for o in model.objects.using(bd).filter(**filter).order_by(n_text):
                        out = "%s<option value='%s'>%s</option>" \
                              % (out, str(o.__getattribute__(n_value)),
                                 o.__getattribute__(n_text))
                else:
                    combo_disabled = "true"

                return HttpResponse(json.dumps({'result': True, 'combo_disabled': combo_disabled, 'combo_html': out}))

            else:
                return HttpResponse(json.dumps({'result': False,
                                                'error': str(_('No se ha especificado el registro'))}))

        except Exception as e:
            return HttpResponse(json.dumps({'result': False, 'error': e}))
