
from flask import Flask, render_template,request,json
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='Datos',
                             charset='utf8mb4')
                         
app = Flask(__name__)




@app.route("/")
def entrar():
    return render_template('index.html')



@app.route('/',methods=['POST', 'GET'])
def ingresardatos():
    if request.method=='POST':
     name=request.form['Name']
     color=request.form['Color']
     pets=request.form['Pets']
     try:
      with connection.cursor() as cursor:
        sql = "INSERT INTO Informacion (name,color, pets) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name,color, pets))
        connection.commit()
     finally:
      return render_template('index.html')
    else:
      return "error"
       

if __name__ == "__main__":
    app.run(debug = True)

