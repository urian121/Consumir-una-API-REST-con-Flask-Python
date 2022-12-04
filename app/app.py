from flask import Flask, request, render_template, url_for, redirect
import requests #Importando libreria Request para hacer peticiones HTTP
import json 
 
#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__) 
app.secret_key = '97110c78ae5105da20fe'


#Creando mi Decorador para el Home
@app.route('/', methods=['GET','POST'])
def inicio():
    URL_API = 'https://fakestoreapi.com/products?limit=8'
    solic_req = requests.get(URL_API)
    #print(solic_req.json()) #convirtiendo solicitu en formato json
    data_API = solic_req.json();
    #Toda la información sobre nuestra petición está ahora almacenada en un objeto Response llamado solic_req
    #print(res.status_code) #comprobar el estado de la peticion
    #print(res.headers)
    #print(res.text)
    #json = res.json()
    #print(json)
    '''parametros = dict(key=API_KEY, text='Hello', lang='en-es')
        res = requests.get(URL_API, parametros=parametros)
        
        query = {'q': 'Forest', 'order': 'popular', 'min_width': '800', 'min_height': '600'}
        req = requests.get('https://pixabay.com/en/photos/', params=query)
        req.url
    '''


    if solic_req:
        print('Respuesta OK')
    else:
        print('Respuesta Fallida')

    return render_template('public/index.html', miData= data_API)


#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))
       
    
#Arrancando mi Aplicacion
if __name__ == '__main__': 
    app.run(debug=True, port=5000) 