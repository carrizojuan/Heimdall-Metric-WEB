# Heimdall-Metric - API

Plataforma de telemedición. Servicio API-REST

## Tecnologías

Este proyecto contiene las sguientes tecnologías:

- Python 3.x
- Django 3.0.8
- Django Rest Framework 
- PostgreSQL
- Django Rest Knox 
- drf-yasg - Swagger generator
- Base de py-helium-console-client
- Influxable

https://github.com/Javidjms/influxable

## Para trabajar de forma nativa

### Requisitos previos

Tenes instalado Python en el S.O.

Además será necesario tener instalado el motor de bases de datos postgreSQL y crear una base de datos y usuario acorde al archivo de configuración del proyecto.
Para hacerlo en un SO Linux: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04-es

https://linuxhint.com/postgresql_installation_guide_ubuntu_20-04/

#### Instalando django knox

Fuente: https://james1345.github.io/django-rest-knox/installation/

Para Debian y Ubuntu:

```sh
sudo apt-get install build-essential
sudo apt-get install python3 python-dev python3-dev \
   build-essential libssl-dev libffi-dev \
   libxml2-dev libxslt1-dev zlib1g-dev \
   python-pip
```

Si se obtiene un error `error: command 'x86_64-linux-gnu-gcc'` correr los siguientes comandos:

```sh
sudo apt-get install python-dev
sudo apt-get install libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev
```

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



## Documentación API's
Al APi se encuentra documentado con drf-yasg (utiliza Swagger). 

Si se corre localmente:
    
    {IP}:{PUERTO}/api/v1/docs/ 
    visualiza la APi en forma dinámica y permite realizar operaciones

    {IP}:{PUERTO}/redoc/
    Documentación de la API
    
    {IP}:{PUERTO}/api/v1/docs.json
    Permite poder obtener una salida en formato json. De la misma manera soporta YAML

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
