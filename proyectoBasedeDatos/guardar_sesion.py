#Creas una cuenta(si no tenias una ya) para poder iniciar sesion y ver el resto de proyectos

import sqlite3
import pandas as pd
import time

conn = sqlite3.connect("cuentas.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cuentas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_cuenta TEXT NOT NULL,
        contraseña TEXT NOT NULL
    )
''')
conn.commit()
accion = int(input("""¿Que deseas hacer?\n\n
                   1.iniciar sesion\n
                   2.crear cuenta\n
                -"""))

if accion == 1:
  print("iniciando sesion: ")
  name = str(input("nombre: "))
  contra = str(input("contraseña: "))
  cursor.execute("SELECT * FROM cuentas WHERE nombre_cuenta = ? AND contraseña = ?", (name, contra))
  resultado = cursor.fetchone()
    
  if resultado == None:
    print("contraseña incorrecta")
  else:
    print("\n",resultado,"\n abriendo sesion...") 
    time.sleep(3)
    with open("sesion_abierta//sesion_iniciada.py","r",encoding="utf-8") as codigo:
      script = codigo.read()
      exec(script)
    
elif accion == 2:
  print("Registrarse:")
  nombre = str(input("nombre de la cuenta: "))
  cursor.execute("SELECT * FROM cuentas WHERE nombre_cuenta = ?", (nombre,))
  if cursor.fetchone():
    print("ya existe este nombre, escoja otro:")
  else:
    contraseña = str(input("contraseña de la cuenta: ")) 
    cursor.execute("INSERT INTO cuentas (nombre_cuenta, contraseña) VALUES (?, ?)", (nombre, contraseña))
      # 3. ¡ESTO ES VITAL! Sin commit, los datos no se guardan en el archivo .db
    conn.commit()
    querry2 ="""SELECT * FROM cuentas"""
    texto = pd.read_sql_query(querry2,conn)
    print(texto)