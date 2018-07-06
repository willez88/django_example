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
