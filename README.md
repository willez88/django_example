# Ejemplo Básico Completo de Django

En este proyecto cada usuario puede registrar los datos de una persona, quedando relacionado para poder saber que datos han registrado ciertos usuarios. Tiene un gestor de usuarios completo que permite iniciar sesión, salir de la sesión y agregar nuevos usuarios por el panel administrativo de django. Todavía no tiene habilitado la creación de nuevos usuarios mediante un formulario de registro.

# Pasos para crear el entorno de desarrollo

Cuando somos un usuario normal del sistema, en el terminal se mostrará el siguiente símbolo: ~$

Cuando accedemos al usuario root del sistema, en el terminal se mostrará el siguiente símbolo: ~#

Crear las siguientes carpetas

    ~$ mkdir Programación

Desde el terminal, moverse a la carpeta Programación y ejecutar

    ~$ mkdir EntornosVirtuales ProyectosDjango

Instalar git phppgadmin postgresql python y virtualenv

    ~# apt install git postgresql phppgadmin python3.6-dev virtualenv

Desde el terminal, moverse a la carpeta EntornosVirtuales y ejecutar

    ~$ virtualenv -p python3.6 nombre_entorno

Para activar el entorno

    ~$ source nombre_entorno/bin/activate

Para salir del entorno usar: deactivate

Nos movemos a la Carpeta ProyectosDjango para descargar el sistema con el siguiente comando

    ~$ git clone direccion_del_repositorio

Tendremos las carpetas estructuradas de la siguiente manera

    // Entorno virtual
    Programación/EntornosVirtuales/nombre_proyecto

    // Servidor de desarrollo
    Programación/ProyectosDjango/nombre_proyecto

Crear la base de datos para __nombre_proyecto__

    // Acceso al usuario postgres
    ~# su postgres

    // Acceso a la interfaz de comandos de postgresql
    postgres@xxx:$ psql

    // Creación del usuario de a base de datos
    postgres=# CREATE USER admin WITH ENCRYPTED PASSWORD '123' CREATEDB;
    postgres=# \q

    // Desautenticar el usuario postgres y regresar al usuario root
    postgres@xxx:$ exit

    // Salir del usuario root
    ~# exit

Puedes crear la base de datos usando la interfaz gráfica phppgadmin

    // Desde algún navegador ir al siguiente sitio y entrar con el usuario que se acaba de crear
    localhost/phppgadmin

    // Nombre de la base de datos: nombre_proyecto

Instalar django y otras aplicaciones en el entorno:

    (nombre_entorno) ~$ pip install nombre_aplicación

Si las aplicaciones requeridas están en un archivo de texto

    (nombre_entorno) ~$ pip install -r requirements.txt

Crear proyectos en django. Desde el terminal, moverse a la carpeta ProyectosDjango y ejecutar

    (nombre_entorno) ~$ django-admin startproject nombre_proyecto

Crear aplicaciones en un proyecto de django. Desde el terminal, moverse a la carpeta nombre_proyecto

    (nombre_entorno) ~$ django-admin startapp nombre_app

Hacer las migraciones

    (nombre_entorno) ~$ python manage.py makemigrations app-1 app-2 ... app-n

    (nombre_entorno) ~$ python manage.py migrate

Crear usuario administrador

    (nombre_entorno) ~$ python manage.py createsuperuser

Cargar datos predefinidos para poblar algunas tablas de la base de datos que lo requieran

    (nombre_entorno) ~$ python manage.py loaddata nombre_archivo.json

Correr el servidor de django

    (nombre_entorno) ~$ python manage.py runserver
