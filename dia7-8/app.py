from flask import Flask, render_template, url_for # Importamos las librerias a ser usadas
import requests

app = Flask(__name__) # Creabamos el objeto app

@app.route("/") # Llamabamos al metodo route y le pasamos el argumento slug o url 
def inicio(): #Creabamos la funcion inicio
    return render_template('inicio.html') #Retornamos la renderizacion de un doc html

@app.route("/contacto")
def contacto():
    API_KEY= "595695c3" # API key que se consigue en ombdapi.com tras registro
    titulo = "Avengers" 
    basic_call= "http://www.omdbapi.com/?apikey=" + API_KEY +"&t="+titulo # Concatenación de URL a la que se realizará la búsqueda
    datos= requests.get(basic_call) # Se ingresa en datos los datos de respuests
    datos=datos.json() # Se convierte a JSON
    titulo_de_pelicula = datos['Title'] # Extraigo el título
    director_de_pelicula = datos['Director'] # Extraigo el director
    datos_filtrados = {'titulo' : titulo_de_pelicula , 'director': director_de_pelicula  }
    return render_template('contacto.html', datos = datos_filtrados)


if __name__ == "__main__":
    app.run(debug=True)