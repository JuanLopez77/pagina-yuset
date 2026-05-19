from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, 
            template_folder='../Frontend/templates', 
            static_folder='../Frontend/static')

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
    app.run(debug=True, port=5000)