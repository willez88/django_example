from django.utils.translation import ugettext_lazy as _

## Mensaje a mostrar al usuario cuando el registro de datos haya sido ejecutado correctamente
CREATE_MESSAGE = _("Los datos fueron registrados correctamente.")

## Mensaje a mostrar cuando los datos hayan sido actualizados correctamente
UPDATE_MESSAGE = _("Los datos fueron actualizados correctamente.")

## Mensaje a mostrar cuando los datos hayan sido eliminados correctamente
DELETE_MESSAGE = _("El registro seleccionado fue eliminado correctamente.")

## Mensaje de error para peticiones AJAX
MSG_NOT_AJAX = _("No se puede procesar la petición. "
                 "Verifique que posea las opciones javascript habilitadas e intente nuevamente.")
