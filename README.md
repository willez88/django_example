# Ejemplo Básico Completo de Django

En este proyecto cada usuario puede registrar los datos de una persona, quedando relacionado para poder saber que datos han registrado ciertos usuarios. Tiene un gestor de usuarios completo que permite iniciar sesión, salir de la sesión y agregar nuevos usuarios por el panel administrativo de django. Todavía no tiene habilitado la creación de nuevos usuarios mediante un formulario de registro.

# Pasos para crear el entorno de desarrollo

Cuando somos un usuario normal del sistema, en el terminal se mostrará el siguiente símbolo: ~$

Cuando accedemos al usuario root del sistema, en el terminal se mostrará el siguiente símbolo: ~#

Crear las siguientes carpetas

    ~$ mkdir Programación

Desde el terminal, moverse a la carpeta Programación y ejecutar

    ~$ mkdir EntornosVirtuales ProyectosDjango

Instalar curl git graphviz graphviz-dev phppgadmin postgresql python y virtualenv

    ~# apt install curl git graphviz graphviz-dev postgresql phppgadmin python3-dev virtualenv

Para instalar npm hacer lo siguiente

    ~# curl -sL https://deb.nodesource.com/setup_10.x | bash -

    ~# apt install -y nodejs

Desde el terminal, moverse a la carpeta EntornosVirtuales y ejecutar

    ~$ virtualenv -p python3 django_ejemplo_basico

Para activar el entorno

    ~$ source django_ejemplo_basico/bin/activate

Nos movemos a la Carpeta ProyectosDjango para descargar el sistema con el siguiente comando

    (django_ejemplo_basico) ~$ git clone https://github.com/willez88/django_ejemplo_basico.git

Tendremos las carpetas estructuradas de la siguiente manera

    // Entorno virtual
    Programación/EntornosVirtuales/django_ejemplo_basico

    // Servidor de desarrollo
    Programación/ProyectosDjango/django_ejemplo_basico

Instalar las dependencias de css y js: moverse a la carpeta static y ejecutar

    // Usa el archivo package.json para instalar lo que ya se configuro allí
    (django_ejemplo_basico) ~$ npm install

    // Terminado el proceso volver a la carpeta raíz del proyecto

Crear la base de datos para __django_ejemplo_basico__ usando PostgresSQL

    // Acceso al usuario postgres
    ~# su postgres

    // Acceso a la interfaz de comandos de PostgreSQL
    postgres@xxx:$ psql

    // Creación del usuario de a base de datos
    postgres=# CREATE USER admin WITH LOGIN ENCRYPTED PASSWORD '123' CREATEDB;
    postgres=# \q

    // Desautenticar el usuario PostgreSQL y regresar al usuario root
    postgres@xxx:$ exit

    // Salir del usuario root
    ~# exit

Puedes crear la base de datos usando la interfaz gráfica phppgadmin

    // Desde algún navegador ir al siguiente sitio y entrar con el usuario que se acaba de crear
    localhost/phppgadmin

    // Nombre de la base de datos: django_ejemplo_basico

Crear la base de datos para __django_ejemplo_basico__ usando MariaDB

    // Acesso al usuario root del sistema
    # mysql

    // Crea el usuario
    CREATE USER 'admin'@'localhost' IDENTIFIED BY '123';

    // Se Otorgan todos los permisos
    GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';

    FLUSH PRIVILEGES;

Puedes crear la base de datos usando la interfaz gráfica phpmyadmin

    // Desde algún navegador ir al siguiente sitio y entrar con el usuario que se acaba de crear
    localhost/phpmyadmin

    // Nombre de la base de datos: django_ejemplo_basico

Instalamos los requemientos que el sistema necesita en el entorno virtual

    (django_ejemplo_basico) ~$ pip install -r requirements.txt

A veces pygraphviz da errores cuando se instala en sistemas operativos x86, cuando esto ocurra revisar el siguiente archivo

    // En este archivo se indica que hacer en caso de error
    requirements/dev.txt

Hacer las migraciones

    (django_ejemplo_basico) ~$ python manage.py makemigrations base persona

    (django_ejemplo_basico) ~$ python manage.py migrate

Crear usuario administrador

    (django_ejemplo_basico) ~$ python manage.py createsuperuser

Correr el servidor de django

    (django_ejemplo_basico) ~$ python manage.py runserver

Poner en el navegador la url que sale en el terminal para entrar el sistema

Llegado hasta aquí el sistema ya debe estar funcionando

Para salir del entorno virtual se puede ejecutar desde cualquier lugar del terminal: deactivate

__Algunos comandos básicos__

Crear proyectos en django. Desde el terminal, moverse a la carpeta ProyectosDjango y ejecutar

    (nombre_entorno) ~$ django-admin startproject nombre_proyecto

Crear aplicaciones en un proyecto de django. Desde el terminal, moverse a la carpeta nombre_proyecto

    (nombre_entorno) ~$ django-admin startapp nombre_app

Cargar datos predefinidos para poblar algunas tablas de la base de datos que lo requieran

    (nombre_entorno) ~$ python manage.py loaddata nombre_archivo_1.json nombre_archivo_2.json ... nombre_archivo_n.json

Exportar datos a json

    (nombre_entorno) ~$ python manage.py dumpdata nombre_app.NombreModelo --indent 4 -o initial_data_nombre_archivo.json

Subir cambios al repositorio

    ~$ git add .

    ~$ git commit -m "descripción específica acerca del cambio que se está subiendo"

    // Con este comando pedirá las credenciales de la cuenta
    ~$ git push origin master

Actualizar los cambios de un repositorio

    ~$ git pull

Cuando un proyecto tiene varios desarrolladores se deben usar ramas

Generar modelo de datos relacional del proyecto completo. Crea la imagen en la raíz del proyecto

    (nombre_entorno) ~$ python manage.py graph_models -a -g -o nombre_proyecto.svg

Generar modelo de datos relacional de una aplicación del proyecto

    (nombre_entorno) ~$ python manage.py graph_models nombre_app -g -o nombre_app.svg

Instalar django y otras aplicaciones en el entorno:

    (nombre_entorno) ~$ pip install nombre_aplicación
