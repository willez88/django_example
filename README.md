# Ejemplo Django

Este sistema permite a un usuario registrarse, iniciar sesión, salir, recuperar contraseña, cambiar contraseña, actualizar perfil. También cada usuario puede gestionar
el registro de personas.

# Pasos para crear el entorno de desarrollo

Cuando somos un usuario normal del sistema, en el terminal se mostrará el siguiente símbolo: ~$

Cuando accedemos al usuario root del sistema, en el terminal se mostrará el siguiente símbolo: ~#

Probado en Debian y Ubuntu. Instalar los siguientes programas

    ~# apt install curl git graphviz graphviz-dev libmysqlclient-dev mariadb-server postgresql python3-dev virtualenv

Crear las siguientes carpetas

    ~$ mkdir Programación

Desde el terminal, moverse a la carpeta Programación y ejecutar

    ~$ cd Programación/

    ~$ mkdir python

Entrar a la carpeta python y hacer lo siguiente

    ~$ cd python/

    ~$ mkdir entornos_virtuales proyectos_django

Entrar a entornos_virtuales

    ~$ cd entornos_virtuales/

    ~$ mkdir django

Desde el terminal, moverse a la carpeta django y ejecutar

    ~$ cd django/

    ~$ virtualenv -p python3 django_example

Para activar el entorno

    ~$ source django_example/bin/activate

Nos movemos a la carpeta proyectos_django, descargamos el sistema y entramos a la carpeta con los siguientes comandos

    (django_example) ~$ cd ../../proyectos_django/

    (django_example) ~$ git clone https://github.com/willez88/django_example.git

    (django_example) ~$ cd django_example/

    (django_example) ~$ cp django_example/settings.default.py django_example/settings.py

Tendremos las carpetas estructuradas de la siguiente manera

    // Entorno virtual
    Programación/python/entornos_virtuales/django/django_example

    // Servidor de desarrollo
    Programación/python/proyectos_django/django_example

Crear la base de datos para __django_example__ usando PostgresSQL

    // Acceso al usuario postgres
    ~# su postgres

    // Acceso a la interfaz de comandos de PostgreSQL
    postgres@xxx:$ psql

    // Creación del usuario de a base de datos
    postgres=# CREATE USER admin WITH LOGIN ENCRYPTED PASSWORD '123' CREATEDB;

    // Crear la base de datos y asignarle el propietario
    postgres=# CREATE DATABASE django_example OWNER admin;

    postgres=# \q

    // Desautenticar el usuario PostgreSQL y regresar al usuario root
    postgres@xxx:$ exit

    // Salir del usuario root
    ~# exit

Puedes crear la base de datos usando la interfaz gráfica de pgadmin4

    // Nombre de la base de datos: django_example

Opcional:

    Crear la base de datos para __django_example__ usando MariaDB

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

        // Si phpmyadmin no abre, ejecutar el siguiente comando
        ~# ln -s /usr/share/phpmyadmin /var/www/html

        // Nombre de la base de datos: django_example

Instalamos los requemientos que el sistema necesita en el entorno virtual

    (django_example) ~$ pip install -r requirements/dev.txt

Hacer las migraciones

    (django_example) ~$ python manage.py makemigrations base user person

    (django_example) ~$ python manage.py migrate

    (django_example) ~$ python manage.py loaddata 1_country.json 2_state.json 3_municipality.json 4_city.json 5_parish.json

Crear usuario administrador

    (django_example) ~$ python manage.py createsuperuser

Correr el servidor de django

    (django_example) ~$ python manage.py runserver

Poner en el navegador la url que sale en el terminal para entrar el sistema

Llegado hasta aquí el sistema ya debe estar funcionando

Para salir del entorno virtual se puede ejecutar desde cualquier lugar del terminal: deactivate

__Algunos comandos básicos__

Crear proyectos en django. Desde el terminal, moverse a la carpeta proyectos_django y ejecutar

    (nombre_entorno) ~$ django-admin startproject nombre_proyecto

Crear aplicaciones en un proyecto de django. Desde el terminal, moverse a la carpeta nombre_proyecto

    (nombre_entorno) ~$ django-admin startapp nombre_app

Cargar datos predefinidos para poblar algunas tablas de la base de datos que lo requieran

    (nombre_entorno) ~$ python manage.py loaddata nombre_archivo_1.json nombre_archivo_2.json ... nombre_archivo_n.json

Exportar datos a json

    (nombre_entorno) ~$ python manage.py dumpdata nombre_app.NombreModelo --indent 4 -o initial_data_nombre_archivo.json

Subir cambios al repositorio

    // Prepara todos los cambios para subirlos
    ~$ git add .

    // Descripción de lo que se sube
    ~$ git commit -m "descripción específica acerca del cambio que se está subiendo"

    // Con este comando pedirá las credenciales de la cuenta
    ~$ git push origin master

    // Actualizar los cambios de un repositorio
    ~$ git pull

Cuando un proyecto tiene varios desarrolladores se deben usar ramas

    // Crear rama a partir de la master (nueva funcionalidad)
    ~$ git checkout -b nombre_rama

    // Subir cambios a nombre_rama
    ~$ git push origin nombre_rama

    // Terminada y probada la funcionalidad, moverse a la rama master para hacer la fusión
    ~$ git checkout master

    // Fusionar nombre_rama con la rama master
    ~$ git merge nombre_rama

En caso que hayan conflictos en la fusión, probar lo siguiente

    // Ver los archivos que tienen conflicto
    git status

    git add archivos ó git add .

    git commit -m "solución de los conflictos en la fusión"

    git merge nombre_rama

    //ver el estado
    git status

    git push

Arreglar los archivos en donde hubo conflictos durante la fusión, luego suba los cambios

    git add .

    git commit -m "fusion completada"

    git push origin master

Si la fusión se completó con éxito, eliminar la rama de manera local

    ~$ git branch -d nombre_rama

    // Eliminar la rama remota
    ~$ git push origin :nombre_rama

    // Limpiar lista de las ramas eliminadas en local
    ~$ git fetch --prune

Establecer una rama como principal

    ~$ git remote set-head origin nombre_rama

Para git con dos repositorios remotos (Ejemplo)

    // Clonar el repositorio donde se hacen cambios constantes (repositorio que será privado)
    ~$ git clone https://github.com/usuario/principal.git

    // Agregar el repositorio remoto
    ~$ git remote add secundario https://github.com/usuario/segundario.git

    // Repo principal es: origin
    // Repo secundario es: secundario

    // Funcionalidades incompletas se sincronizan con el remoto principal usando los comandos normales

    // Funcionalidades completas se pueden sincronizar con el repo secundario
    ~$ git fetch secundario
    ~$ git merge secundario/master
    // Estos dos comandos también se puede usar de esta forma:
    ~$ git pull secundario master

    // En caso de conflictos en la mezcla, solucionarlos

    // La sincronización está con origin/master, por lo tanto,
    // para subir cambios al remoto secundario es con el siguiente comando
    ~$ git push -u secundario

    // Luego de ejecutar ese comando la sincronización cambia a secundario/master
    // para volver a la sincronización con origin/master, ejecutar lo siguiente
    ~$ git push -u origin

Generar modelo de datos relacional del proyecto completo. Crea la imagen en la raíz del proyecto

    (nombre_entorno) ~$ python manage.py graph_models -a -g -o nombre_proyecto.svg

Generar modelo de datos relacional de una aplicación del proyecto

    (nombre_entorno) ~$ python manage.py graph_models nombre_app -g -o nombre_app.svg

Instalar django y otras aplicaciones en el entorno:

    (nombre_entorno) ~$ pip install nombre_aplicación

# Pasos para crear el entorno de desarrollo en Windows

Instalar los siguientes programas

    // Descargar git
    git: https://git-scm.com/downloads

    // Descargar wampserver o xampp
    wampserver: http://www.wampserver.com/en/
    xampp: https://www.apachefriends.org/es/index.html

    // Descargar python y cuando se instale seleccionar la opción de agregar al path
    python: https://www.python.org/downloads/windows/

    // Descargar BD Browser para visualizar las bases de datos si se usa sqlite3
    DB Browser: https://sqlitebrowser.org/dl/

Con python instalado, abrir el terminal de windows y ejecutar

    pip install virtualenv

Desde el mismo terminal, crear estas carpetas usando el siguiente comando

    mkdir Programacion\python\entornos_virtuales\django
    mkdir Programacion\python\proyectos_django

Moverse a la siguiente carpeta para crear el entorno virtual del proyecto

    cd Programacion\python\entornos_virtuales\django
    virtualenv django_example

Creado el entorno virtual, se puede activar y desactivar (dejarlo activado)

    // Activa el entorno virtual
    django_example\Scripts\activate.bat

    // Desactiva el entorno virtual
    django_example\Scripts\deactivate.bat

Con git instalado, abrirlo y en esa nueva terminal, moverse a la carpeta proyectos_django

    cd Programacion/python/proyectos_django

Desde el terminal de git, clonar el proyecto desde el repositorio

    git clone https://github.com/willez88/django_example.git

Moverse al proyecto django_example

    cd django_example

Configurar el settings.default.py del proyecto

    // Se hace una copia del settings.default.py con el nombre settings.py
    cp django_example/settings.default.py django_example/settings.py

    // Se abre el archivo django_example/settings.py con un editor de texto y hacer lo siguiente
    // Comentar las líneas de PostgreSQL y descomentar las líneas de sqlite3

Deben haber dos terminales abiertos

    // Terminal del entorno virtual
    // Terminal del git

Volvemos al terminal del entorno virtual y nos movemos a la carpeta del proyecto

    // Pararse en la carpeta del proyecto
    cd ..\..\proyectos_django\django_example

    // antes de ejecutar este comando, comentar las lineas 4, 5 y 6 del archivo requirements\dev.txt
    pip install -r requirements\dev.txt

Hacer las migraciones desde el terminal de virtualenv

    python manage.py makemigrations base user person

    python manage.py migrate

    python manage.py loaddata 1_country.json 2_state.json 3_municipality.json 4_city.json 5_parish.json

Crear usuario administrador

    python manage.py createsuperuser

Iniciar el servidor de python

    python manage.py runserver

Poner en el navegador la url que sale en el terminal para entrar el sistema

Llegado hasta aquí el sistema ya debe estar funcionando
