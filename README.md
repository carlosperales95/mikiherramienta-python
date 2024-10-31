# La Mikiherramienta
Este proyecto empezo como 3 diferentes scripts que hicimos en directo.

Al final los hemos unido en una sola aplicacion, y lo hemos dockerizado para facilitar la instalacion y el setup de este proyectillo.

## Como usarlo

Primero hay que clonar el repositorio:
```
git clone https://github.com/carlosperales95/mikiherramienta-python
```

Una vez tengamos los archivos clonados, hay dos opciones para instalar/ejecutar las dependencias y codigo.

### Virtual Environment (venv)
Los siguientes comandos nos ayudaran a crear y activar un entorno virtual para las depencias del proyecto.

Al sustituir `<nombre>` por el nombre que deseamos para nuestra carpeta de entorno virtual, los comandos estaran listos para su ejecucion:
```
python -m venv <nombre>
source /<nombre>/bin/activate
```

Una vez activado, podemos instalar las dependencias del archivo `requirements.txt` en nuestro entorno usando `pip`:
```
pip install -r ./requirements.txt
```

Ya estamos listos para ejecutar el programa:
```
python main.py
```

### Docker

Para ejecutar nuestro programa en un entorno containerizado, debemos instalar `docker`. Esta informacion se puede encontrar en la documentacion oficial de [Dockerdocs](https://docs.docker.com/engine/install/).

Una vez instalado, debemos crear la imagen para poder montarla en contenedores. COmo ejemplo de nombre de imagen he elegido `mikiherramienta`, pero este nombre puede ser cambiado:
```
docker build -t . mikiherramienta
```

Una vez nuestra imagen ha sido creada con exito, podemos usarla para crear un nuevo contenedor:
```
docker run -i -t mikiherramienta
```
