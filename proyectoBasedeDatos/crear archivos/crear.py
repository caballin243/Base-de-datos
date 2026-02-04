#Este programa srive para crear archivo con texto

def archivo(extension,name,texto):
    documento = name+extension
    with open(ubicacion+documento,"w") as archivo:
        archivo.write(texto)
        print("se leyo")
    
    
    
tipo = int(input("""que quieres crear: 
                       1.Excel
                       2.WORD
                                _"""))

nombre = str(input("Nombre del archivo(no incluir extension): "))

texto = str(input("""que dira en el archivo:
                            """))
ubicacion = "crear archivos/" 
if tipo == 1:
    archivo(".csv",nombre,texto)
    documento = (nombre+".csv")
    
elif tipo == 2:
    archivo(".docx",nombre,texto)
    documento = (nombre+".docx")


with open(ubicacion+documento,"r") as abrir:
    print(abrir.read())
    