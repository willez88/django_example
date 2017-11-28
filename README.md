# Ejemplo Básico Completo de Django

En este proyecto cada usuario puede registrar los datos de una persona, quedando relacionado para poder saber que datos han registrado ciertos usuarios. Tiene un gestor de usuarios completo que permite iniciar sesión, salir de la sesión y agregar nuevos usuarios por el panel administrativo de django. Todava no tiene habilitado la creación de nuevos usuarios mediante un formulario de registro.

# Pasos para crear el entorno de desarrollo

-    Crear las siguientes carpetas

~$ mkdir Programación

-    Desde el terminal, moverse a la carpeta Programación y ejecutar

~$ mkdir EntornosVirtuales ProyectosDjango Repositorios

-    Instalar virtualenv y python

~$ sudo apt install git python3.6-dev virtualenv

-    Desde el terminal, moverse a la carpeta EntornosVirtuales y ejecutar

~$ virtualenv -p python3.6 nombre_entorno

-    Para activar el entorno

~$ source nombre_entorno/bin/activate

-    Para salir del entorno usar: deactivate

-    Instalar django y otras aplicaciones en el entorno:

$ pip install nombre_aplicación

-    Si las aplicaciones requeridas están descritas en un archivo de texto

$ pip install -r requirements.txt

-    Crear proyectos en django. Desde el terminal, moverse a la carpeta ProyectosDjango y ejecutar

~$ django-admin startproject nombre_proyecto

-    Crear aplicaciones en un proyecto de django. Desde el terminal, moverse a la carpeta nombre_proyecto

~$ django-admin startapp nombre_app

-    Hacer las migraciones

~$ python manage.py makemigrations app-1 app-2 ... app-n

~$ python manage.py migrate

-    Crear usuario administrador

~$ python manage.py createsuperuser

-    Cargar datos predefinidos para poblar algunas tablas de la base de datos que lo requieran

~$ python manage.py loaddata nombre_archivo.json

-    Correr el servidor de django

~$ python manage.py runserver

-    En Repositorios se clonan todos los proyectos que estemos trabajando, por ejemplo

~$ git clone direccion_del_repositorio

-    Para los que no saben usar bien la herramienta git, se recomienda tener el repositorio y los proyectos que se desarrollan por separado y cuando se tienen versiones estables mezclar con el que esta en la carpeta Repositorios
