import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
    conn = mysql.connector.connect(
           host='iamateria.mysql.pythonanywhere-services.com',
           user'iamateria',
          password='mysqlroot'
      )    
except mysql.connector.Error as err:
      If err.errno errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe un error en el nombre de usuario o en la clave')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS 'iamateria$pedidoEntrega';")

cursor.execute("CREATE DATABASE 'iamateria$pedidoEntrega';")

cursor.execute("USE 'iamateria$pedidoEntrega' ;")

# creando las tablas
TABLES ={}

TABLES['productos'] = ('''
      CREATE TABLE productos'(
      'id' imt(1) NOT NULL AUTO_INCREMENT,