# SERVER_SSL

Este proyecto configura un servidor web con Nginx y Docker, proporcionando soporte para SSL/TLS para garantizar la seguridad en las conexiones entre los clientes y el servidor. Utiliza Docker Compose para desplegar los servicios y facilita la creación de un entorno de servidor web seguro y escalable.

## Características

- **Nginx**: Actúa como servidor web y proxy inverso.
- **SSL/TLS**: Configurado para habilitar conexiones seguras mediante HTTPS.
- **Docker & Docker Compose**: Facilita el despliegue y administración de servicios en contenedores.
  
## Requisitos previos

- **Docker**: Asegúrate de tener Docker instalado en tu máquina. Puedes obtener Docker desde [aquí](https://www.docker.com/).
- **Docker Compose**: También es necesario instalar Docker Compose. Más información sobre cómo instalarlo [aquí](https://docs.docker.com/compose/install/).

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/AndresJejen/SERVER_SSL.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd SERVER_SSL
    ```

3. (Opcional) Modifica las configuraciones SSL en el archivo `nginx/nginx.conf` o reemplaza los certificados SSL existentes en `nginx/certs/` con tus propios certificados y clave privada.

## Uso

1. Una vez en el directorio raíz del proyecto, levanta los servicios ejecutando:
    ```bash
    docker-compose up
    ```

2. El servidor Nginx estará disponible en `https://localhost`. Si deseas acceder desde otra máquina, reemplaza `localhost` por la dirección IP de tu servidor.

3. Para detener los contenedores, ejecuta:
    ```bash
    docker-compose down
    ```

## Estructura del Proyecto

- `nginx/`: Contiene la configuración de Nginx y los certificados SSL.
    - `nginx.conf`: Archivo de configuración principal de Nginx.
    - `certs/`: Directorio donde se almacenan los certificados SSL y claves privadas.
- `webapp/`: Archivos de la aplicación web servida.
- `docker-compose.yml`: Archivo de configuración de Docker Compose que define los servicios.

## Personalización

- **Certificados SSL**: Si necesitas tus propios certificados, puedes colocarlos en el directorio `nginx/certs/`. Asegúrate de configurar las rutas correctamente en `nginx/nginx.conf`.
- **Modificaciones a Nginx**: Puedes modificar las reglas de Nginx dentro del archivo `nginx.conf` para adaptarlo a las necesidades específicas de tu servidor o aplicación.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commits (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
