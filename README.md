
# Color Palette Generator


Este sencillo proyecto web desarrollado con Flask, genera paletas de colores a partir de imágenes subidas por el usuario. Utiliza Pillow para la manipulación de imágenes y NumPy para manejar operaciones de matriz.

## Tecnologías Utilizadas

- Python 3.x
- Flask
- Pillow
- NumPy

## Estructura del Proyecto
- **app.py:** Archivo principal de la aplicación Flask.
- **templates/index.html:** Plantilla HTML para la interfaz de usuario.
- **requirements.txt:** Archivo de dependencias del proyecto.

## Demostración
Puedes observar una demostración de la aplicación en el siguiente enlace: http://cdavidbm.pythonanywhere.com/

# Para explorar la aplicacion localmente

## Instalación de un Entorno Virtual de Python

Para examinar este proyecto, te recomiendo crear y activar un entorno virtual en Python. Sigue los siguientes pasos:

### Paso 1: Instalación de `venv`

Python 3 incluye el módulo `venv` por defecto. Si estás usando Python 3.3 o superior, no necesitas instalar nada adicional. Simplemente asegúrate de tener Python 3 instalado en tu sistema. Puedes verificar esto ejecutando:

```sh
python3 --version
```

### Paso 2: Crear un Entorno Virtual

Navega hasta el directorio de tu proyecto y crea un entorno virtual ejecutando el siguiente comando:

```sh
python3 -m venv nombre_del_entorno
```

Reemplaza `nombre_del_entorno` con el nombre que quieras darle a tu entorno virtual.

### Paso 3: Activar el Entorno Virtual

Después de crear el entorno virtual, debes activarlo. El comando para activar el entorno virtual varía según el sistema operativo que estés utilizando.

- **En Windows**:

  ```sh
  .\nombre_del_entorno\Scripts\activate
  ```

- **En macOS y Linux**:

  ```sh
  source nombre_del_entorno/bin/activate
  ```

### Paso 4: Verificar que el Entorno Virtual está Activado

Cuando el entorno virtual esté activado, deberías ver el nombre del entorno en el prompt de tu terminal, algo como esto:

```sh
(nombre_del_entorno) $
```

### Paso 5: Instalar Dependencias

Con el entorno virtual activado, puedes instalar las dependencias de tu proyecto. Por ejemplo, para instalar las dependencias listadas en un archivo `requirements.txt`, usa:

```sh
pip install -r requirements.txt
```

### Paso 6: Desactivar el Entorno Virtual

Para desactivar el entorno virtual y volver al entorno global de Python, simplemente ejecuta:

```sh
deactivate
```

## Descargar el código

Para obtener una copia local y ponerla en funcionamiento, sigue estos simples pasos:

1. **Clona el repositorio**
   ```sh
   git clone https://github.com/cdavidbm/Color-Palette-Generator.git
   ```
2. **Instala las dependencias**
   ```sh
   pip install -r requirements.txt
   ```
   Contenido del archivo `requirements.txt`:
   ```
   flask==2.3.2
   pillow==10.0.0
   numpy==1.25.0
   ```

3. **Ejecuta la aplicación**
   ```sh
   python app.py
   ```

## Uso

- Acceder a la Aplicación: Abre tu navegador web y ve a http://127.0.0.1:5000/.

- Subir una Imagen: Utiliza el formulario en la página principal para subir una imagen.

- Elegir el Código de Color: Selecciona el formato de color (HEX) para la paleta generada.

- Ver los Resultados: La página se actualizará para mostrar la imagen subida y la paleta de colores generada en el formato seleccionado.


## Contribuciones

Las contribuciones son lo que hace que la comunidad de código abierto sea un lugar increíble para aprender. Cualquier modificación que quieras sugerir es **muy apreciada**.

#### 1. Haz un fork del proyecto.
#### 2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`).
#### 3. Realiza tus cambios (`git commit -m 'Add some AmazingFeature'`).
#### 4. Push a la rama (`git push origin feature/AmazingFeature`).
#### 5. Abre un Pull Request.

