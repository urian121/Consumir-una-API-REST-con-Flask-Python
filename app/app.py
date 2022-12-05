from flask import Flask, render_template, url_for, redirect, jsonify
import requests #Importando libreria Request para hacer peticiones HTTP
import json #Importando json desde python
 
 
#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__) 
app.secret_key = '97110c78ae5105da20fe'


#Creando mi Decorador para el Home
@app.route('/API', methods=['GET','POST'])
def api():
    URL_API = 'https://jsonplaceholder.typicode.com/users/'
    solic_req = requests.get(URL_API)
    data_API = solic_req.json(); #Este método es conveniente cuando la API devuelve JSON
    #Toda la información sobre nuestra petición está ahora almacenada en un objeto Response llamado solic_req
    print(solic_req.json())
    #print(solic_req.status_code) #comprobar el estado de la peticion


    if solic_req.status_code == 200:
        print('Respuesta OK')
        return jsonify({'resp': data_API })
    else:
        print('Respuesta Fallida')



#Creando mi Decorador para el Home
@app.route('/', methods=['GET','POST'])
def inicio():
    URL_API = 'https://fakestoreapi.com/products'
    solic_req = requests.get(URL_API)
    print(solic_req)
    #print(solic_req.json()) #convirtiendo solicitud en formato json
    data_API = solic_req.json(); #Este método es conveniente cuando la API devuelve JSON
    #Toda la información sobre nuestra petición está ahora almacenada en un objeto Response llamado solic_req
    print(solic_req.status_code) #comprobar el estado de la peticion

    if solic_req.status_code == 200:
        print('Respuesta OK 1')
    else:
        print('Respuesta Fallida')

    return render_template('public/index.html', miData = data_API)

    


#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))
       
    
#Arrancando mi Aplicacion
if __name__ == '__main__': 
    app.run(debug=True, port=5000) 