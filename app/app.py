from flask import Flask, request, render_template
from confiDB import * #Importando conexion BD



app = Flask(__name__) 

#Creando mi Decorador para el Home
@app.route('/', methods=['GET','POST'])
def inicio():
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexión desde la función
    mycursor         = conexion_MySQLdb.cursor(dictionary=True)
    querySQL  = ("SELECT * FROM eventoscalendar")
    mycursor.execute(querySQL)
    dataEventos = mycursor.fetchall() #fetchall () Obtener todos los registros
    mycursor.close() #cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    totalEventos = mycursor.rowcount
    return render_template('public/index.html', dataEmpleados = dataEventos)


@app.route('/form', methods=['GET', 'POST'])
def registrarEvento():
    msg =''
    if request.method == 'POST':
        evento            = request.form['evento']
        f_inicio          = request.form['fecha_inicio']; 
        f_fin             = request.form['fecha_fin']
        color_evento      = request.form['color_evento']
        print(f_inicio, f_fin)
        
        '''
        Nota: Ambas fechas llegan en formato dia-mes-año,
        hay pasarlas a año, mes y dia
        '''
        fecha_inicio = datetime.strptime(f_inicio, '%m-%d-%Y').date()
        fecha_fin    = datetime.strptime(f_fin, '%m-%d-%Y').date()
        print(fecha_inicio, fecha_fin)
         
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO eventoscalendar(evento, fecha_inicio, fecha_fin, color_evento) VALUES (%s, %s, %s, %s)")
        valores     = (evento, fecha_inicio, fecha_fin, color_evento)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD

        return render_template('public/index.html', msg='Formulario enviado')
   
   
    

if __name__ == '__main__': 
    app.run(debug=True, port=5000) 