# Telemedicion de energia - web

Plataforma de telemedición de energia en hogares. Se obtienen las mediciones desde un dispositivo IOT

## Tecnologías

Este proyecto contiene las sguientes tecnologías:

- Python 3.x
- Django 3.0.8
- PostgreSQL
- Base de py-helium-console-client
- Influxable

https://github.com/Javidjms/influxable

## Para trabajar de forma nativa

### Requisitos previos

Tenes instalado Python en el S.O.

Además será necesario tener instalado el motor de bases de datos postgreSQL y crear una base de datos y usuario acorde al archivo de configuración del proyecto.
Para hacerlo en un SO Linux: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04-es

https://linuxhint.com/postgresql_installation_guide_ubuntu_20-04/


### Instalación

1. Tener instalado Python 3 https://www.python.org/downloads/
1. Crear un entorno virtual https://docs.python.org/es/3.8/tutorial/venv.html (leer los primeros dos apartados)
1. Activar el entorno virtual y posicionarse en el directorio `/requirements`
1. Ejecutar por la terminal el comando `pip install -r requirements.txt` Finalizado tendremos instalado nuestras dependencias.

### Ejecución

1. Abrir una terminal y activar el entorno virtual
1. Posicionarse en el directorio ../src/
1. Levantar el proyecto con: `python manage.py runserver` (nota: se puede especificar `<IP>:<PUERTO>` luego de runserver)
1. Acceder al sitio donde se levanta localmente el proyecto

Abrir terminarl y ejecutar:
docker run -p 6379:6379 -d redis:5
celery worker -A OdynAPI.celery --loglevel=info

Esto son para tareas asincronas en el proyecto



## Archivo configuración

Para el despliegue de aplicación, se debe crear un archivo access.conf en el directorio de credentials
El mismo debe tener:

    [default]
    name=*******
    user=*******
    password=*******
    host=******
    port=*******
    
    [influxdb]
    INFLUXDB_URL=*********
    INFLUXDB_DATABASE_NAME=**********
    
    #Optional
    INFLUXDB_USER=**********
    INFLUXDB_PASSWORD=*********
    
    # OSS 2.0
    INFLUXDB_AUTH_TOKEN=mytoken
