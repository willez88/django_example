/**
 * @brief Función que agrega los botones de descarga a una dataTable
 *
 * @author William Páez (paez.william8 at gmail.com)
 * @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
 * @date 03-08-2018
 * @param table Objeto que contiene la instancia de un Datatable
 */
function button_datatable(table) {
  new $.fn.dataTable.Buttons(table, {
    buttons: [
      {
        extend: 'copyHtml5',
      },
      {
        extend: 'csvHtml5',
        fieldBoundary: '',
        fieldSeparator: ';',
        title: 'django_example',
      },
      {
        extend: 'excelHtml5',
        title: 'django_example',
      },
      {
        extend: 'pdfHtml5',
        title: 'django_example',
      },
      {
        extend: 'print',
      },
    ],
  });
  table.buttons().container().appendTo(table.table().container());
}
