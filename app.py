#importacion de librerias
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
#contenedor para llamar a principal.html
def index():
    return render_template('/principal.html')

@app.route('/winner')
#contenedor para llamar a principal.html
def winner():
    return render_template('/winner.html')
 #  Iniciando la aplicaciones
if __name__ == "__main__":
    app.run(debug=True)