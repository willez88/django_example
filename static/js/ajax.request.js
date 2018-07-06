/**
 * @brief Función que actualiza los datos de combos dependientes
 * @param option Código del elemento seleccionado por el cual se filtrarán los datos en el combo dependiente
 * @param app Nombre de la aplicación en la cual buscar la información a filtrar
 * @param mod Modelo del cual se van a extraer los datos filtrados según la selección
 * @param field Nombre del campo con el cual realizar el filtro de los datos
 * @param n_value Nombre del campo que contendra el valor de cada opción en el combo
 * @param n_text Nombre del campo que contendrá el texto en cada opción del combo
 * @param combo_target Identificador del combo en el cual se van a mostrar los datos filtrados
 * @param bd Nombre de la base de datos, si no se específica se asigna el valor por defecto
 */
function combo_update(option, app, mod, field, n_value, n_text, combo_target, bd) {
    /* Verifica si el parámetro esta definido, en caso contrario establece el valor por defecto */
    bd = typeof bd !== 'undefined' ? bd : 'default';
    $.ajaxSetup({
        async: false
    });
    $.getJSON(URL_COMBO_UPDATE, {
        option:option, app:app, mod:mod, field:field, n_value:n_value, n_text: n_text, bd:bd
    }, function(data) {

        var combo = $("#"+combo_target);

        if (data.result) {

            if (data.combo_disabled == "false") {
                combo.removeAttr("disabled");
            }
            else {
                combo.attr("disabled", "true");
            }

            combo.html(data.combo_html);
        }
        else {
            //bootbox.alert(data.error);
            console.log(data.error);
        }
    }).fail(function(jqxhr, textStatus, error) {
        var err = textStatus + ", " + error;
        //bootbox.alert( "{% trans 'Petición fallida. Verifique el error: ' %}" + err );
        console.log("{% trans 'Petición fallida. Verifique el error: ' %}" + err)
    });
}
