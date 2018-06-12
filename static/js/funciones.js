/**
 * @brief Función que agrega los botones para exportar en un dataTable
 * @param tabla dataTable al cual se le agregan los botones
 */
function inicializar_boton_datatable(tabla) {
    new $.fn.dataTable.Buttons(tabla, {
        buttons: [
            {
                extend: 'copyHtml5',
            },
            {
                extend: 'csvHtml5',
                fieldBoundary: '',
            },
            {
                extend: 'excelHtml5',
            },
            {
                extend: 'pdfHtml5',
            },
            {
                extend: 'print',
            },
        ],
      });
      tabla.buttons().container().appendTo(tabla.table().container());
}
