import os
import subprocess
import sys
from guardar_sesion import name
import pandas as pd
import sqlite3

conn = sqlite3.connect("cuentas.db")
cursor = conn.cursor()
accion = int(input("""
                Mostrar proyecto:
                 1.Juego
                -"""))
if(accion==1):
    
      
    ruta_juego = os.path.join("game", "juego.py")    
    print(f"Lanzando: {ruta_juego}...")
    subprocess.run([sys.executable, ruta_juego])
    
    #decir mi nombre
    with open("cuentas.db"):
      querry = ("select nombre_cuenta from cuentas where nombre_cuenta = '?'",name)  
      nombre = cursor.execute(querry)
      identidad = pd.read_sql_query(querry,conn)
      print(identidad)
    
    
    