# Importar las bibliotecas necesarias:
# numpy para operaciones con arrays y matrices
# Image y ImageOps de la biblioteca PIL para manipulación de imágenes
# Flask, render_template y request de Flask para crear la aplicación web

import numpy as np 
from PIL import Image, ImageOps
from flask import Flask, render_template, request

# Función para convertir un color RGB a formato hexadecimal
def rgb_to_hex(rgb):
	"""
	Convierte un valor de color RGB en un código de color hexadecimal.
	Args:
		rgb (tuple): Tupla que representa un color RGB (rojo, verde, azul).
	Returns:
		str: Código de color hexadecimal.
	"""
	return '%02x%02x%02x' % rgb

# Función para obtener los colores más frecuentes en una imagen
def give_most_hex(file_path, code):
	"""
	Analiza una imagen y devuelve los 10 colores más frecuentes en formato RGB o hexadecimal.
	Args:
		file_path (str): Ruta de la imagen a analizar.
		code (str): Código que indica el formato de salida ('hex' para hexadecimal, otro para RGB).
	Returns:
		list: Lista de colores en formato RGB o hexadecimal, según el código especificado.
	"""

	# Abrir imagen y convertirla a modo RGB
	my_image = Image.open(file_path).convert('RGB')

	# Redimensionar la imagen si es necesario para mejorar la velocidad de procesamiento
	size = my_image.size
	if size[0] >= 400 or size[1] >= 400:
		my_image = ImageOps.scale(image=my_image, factor=0.2)
	# ... (lógica similar para imágenes más grandes)

	# Reducir la profundidad del color utilizando la posterización
	my_image = ImageOps.posterize(my_image, 2)

	# Convertir la imagen a un array NumPy para facilitar su procesamiento
	image_array = np.array(my_image)

	# Inicializar un diccionario para almacenar colores únicos y sus conteos
	unique_colors = {}  # (r, g, b): count

	# Recorrer cada píxel y contar las ocurrencias de colores únicos
	for column in image_array:
		for rgb in column:
			t_rgb = tuple(rgb)  # Convertir píxel individual a una tupla
			if t_rgb not in unique_colors:
				unique_colors[t_rgb] = 0
			unique_colors[t_rgb] += 1

	# Ordenar el diccionario por conteo de color (orden descendente)
	sorted_unique_colors = sorted(
		unique_colors.items(), key=lambda x: x[1], reverse=True)
	converted_dict = dict(sorted_unique_colors)

	# Obtener los 10 colores más frecuentes
	values = list(converted_dict.keys())
	top_10 = values[0:10]

	# Convertir los 10 colores principales a hexadecimal si se solicita (code='hex')
	if code == 'hex':
		hex_list = []
		for key in top_10:
			hex = rgb_to_hex(key)
			hex_list.append(hex)
		return hex_list
	else:
		return top_10

# Crea la aplicación Flask
app = Flask(__name__)

# Define la ruta principal de la aplicación
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# Obtener el archivo subido y el código de color solicitado del formulario
		f = request.files['file']
		colour_code = request.form['colour_code']
		# Procesar la imagen y obtener los colores principales
		colours = give_most_hex(f.stream, colour_code)
		# Renderizar la plantilla index.html, pasando los colores y el código de color
		return render_template('index.html',
							colors_list=colours,
							code=colour_code)
	return render_template('index.html')

# Ejecuta la aplicación Flask en modo debug
if __name__ == '__main__':
	app.run(debug=True)
