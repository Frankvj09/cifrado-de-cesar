# Importamos las funciones necesarias del framework web Flask
# - Flask: para crear la aplicación web
# - render_template: para cargar archivos HTML desde la carpeta "templates"
# - request: para manejar los datos enviados desde formularios HTML (método POST)
from flask import Flask, render_template, request

# Creamos una instancia de la aplicación Flask
# __name__ indica que este archivo será el punto de entrada principal
app = Flask(__name__)

# Función que implementa el algoritmo del Cifrado César
def cifrado_cesar(texto, desplazamiento):
    resultado = ""  # Aquí guardaremos el texto cifrado final

    # Recorremos cada carácter del texto original
    for char in texto:
        # Si el carácter es una letra del alfabeto
        if char.isalpha():
            # Determinamos si es mayúscula o minúscula para obtener su código base
            base = ord('A') if char.isupper() else ord('a')
            # Calculamos la nueva letra aplicando el desplazamiento
            # ord() convierte la letra en número Unicode, chr() lo convierte de nuevo en letra
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            # Si no es letra (espacio, número, signo, etc.), lo dejamos igual
            resultado += char

    # Devolvemos el texto cifrado
    return resultado

# Ruta principal de la aplicación: http://localhost:5500/ http://127.0.0.1:5500/
# Permitimos dos métodos: GET (abrir la página) y POST (enviar el formulario)
@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = ""  # Variable para almacenar el resultado del cifrado

    # Si el usuario envió el formulario (POST)
    if request.method == 'POST':
        # Obtenemos los datos enviados desde el formulario HTML
        texto = request.form['texto']
        desplazamiento = int(request.form['desplazamiento'])

        # Llamamos a la función de cifrado y guardamos el resultado
        mensaje = cifrado_cesar(texto, desplazamiento)

    # Renderizamos el archivo HTML 'index.html' y le pasamos la variable 'mensaje'
    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    # Render necesita que la app escuche en host 0.0.0.0 y el puerto que Render le asigne
    import os
    port = int(os.environ.get("PORT", 5500))
    app.run(host="0.0.0.0", port=port, debug=False)
    # Ejecutamos la aplicación en modo debug para facilitar el desarrollo
    # app.run(debug=True)
