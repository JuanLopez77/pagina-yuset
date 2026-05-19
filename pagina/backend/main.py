import os
from flask import Flask, render_template, request, redirect, url_for

# Definimos las rutas relativas basadas en la ubicación de este archivo (main.py)
# Como main.py está en 'pagina/backend', subimos un nivel con '../' para llegar a 'pagina'
# y luego entramos a 'frontend'
template_dir = os.path.join(os.path.dirname(__file__), '../frontend/templates')
static_dir = os.path.join(os.path.dirname(__file__), '../frontend/static')

app = Flask(__name__, 
            template_folder=template_dir, 
            static_folder=static_dir)

# Ruta Principal (Landing Page)
@app.route('/')
def index():
    return render_template('index.html')

# vista del curso 1
@app.route('/curso1')
def curso1():
    return render_template('curso1.html')

# vista del curso 2
@app.route('/curso2')
def curso2():
    return render_template('curso2.html')

# vista del curso 3
@app.route('/curso3')
def curso3():
    return render_template('curso3.html')

if __name__ == '__main__':
    # Nota: En Render, Gunicorn se encargará de ejecutar la app, 
    # esto solo es para que funcione en tu PC.
    app.run(debug=True, port=5000)