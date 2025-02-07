# conversor_contactos_thunderbird_outlook
Conversor de Contactos de Thunderbird a Outlook

Este proyecto permite convertir un CSV de Thunderbird al formato de Outlook mediante una aplicación web desarrollada con Flask.

# Acceso:

    URL: http://192.168.1.11:5000

# Requisitos:

    Python3
    pip
    venv

# Instalación:

    Clonar o descargar el proyecto
    Coloca el proyecto en el directorio /var/www/conversor_contactos.

    Crear el entorno virtual
    Accede al directorio del proyecto y crea un entorno virtual:

cd /var/www/conversor_contactos
python3 -m venv venv

## Activar el entorno virtual:

source venv/bin/activate

## Instalar dependencias:
Asegúrate de que el archivo requirements.txt contenga lo siguiente:

Flask==2.2.2

Luego, instala las dependencias:

    pip install -r requirements.txt

# Uso:

Ejecución de la Aplicación: La aplicación se inicia mediante el script run_app.sh, que activa el entorno virtual, establece la variable de entorno FLASK_APP y ejecuta Flask:

   source /var/www/conversor_contactos/venv/bin/activate
   export FLASK_APP=/var/www/conversor_contactos/app.py
   flask run --host=0.0.0.0 --port=5000

## ARRANCAR SERVICIO
Puedes ejecutar el script con:

   bash run_app.sh

## SUSPENDER SERVICIO
Si deseas suspender el proceso y ejecutarlo en segundo plano:

    Presiona Ctrl+z para suspenderlo.
    Luego, usa bg para reanudarlo en background.

Desactivación del Módulo: Para detener la aplicación, utiliza htop o cualquier otro gestor de procesos para matar el proceso de Flask.

# Descripcion de los archivos
## Descripción del Archivo app.py
El archivo app.py contiene la aplicación Flask encargada de:

    Mostrar un formulario HTML para subir el archivo CSV de Thunderbird.
    Convertir los encabezados del CSV según un mapeo definido para Outlook.
    Enviar el CSV convertido como descarga al usuario.

# Metodo Alternativo
Ejecución Directa con Flask: Alternativamente, puedes ejecutar la aplicación directamente con Flask:

   export FLASK_APP=/var/www/conversor_contactos/app.py
   flask run --host=0.0.0.0 --port=5000

# Notas:

    Asegúrate de que el CSV de Thunderbird contenga los encabezados esperados para que el mapeo funcione correctamente.
    Personaliza el mapeo en app.py según tus necesidades.

¡Disfruta del Conversor de Contactos!
