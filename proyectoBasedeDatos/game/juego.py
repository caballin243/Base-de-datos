#Aqui cree un minijuego donde escoges a tu personaje y te mueves por un mapa para derrotar
# en un juego de piedra papel o tijeras a la carita enojada

import time
import batalla
print("busca y derrota a la carita enojada `-´")
personaje=input("escoge tu personaje: ")
piso2=["-","-","-","-","`-´","-"]
piso1=["-","-","-","-","-","-"]
pisos = [piso1,piso2]
m=1
piso1.pop(0)
piso1.insert(0,personaje)
salida = True
def arriba(pisoactual,otropiso,indice):
    pisoactual.pop(indice)
    pisoactual.insert(indice,"-")
    otropiso.pop(indice)
    otropiso.insert(indice,personaje)
    
def abajo(pisoactual,otropiso,indice):
    pisoactual.pop(indice)
    pisoactual.insert(indice,"-")
    otropiso.pop(indice)
    otropiso.insert(indice,personaje)  
    
def derecha(lista,indice):
    if indice == 5:
        indice=-1
    lista[indice] = "-"
    lista[indice+1] = personaje
    
def izquierda(lista, indice):
   
    lista[indice] = "-"
    if indice == 0:
      indice=6
    lista[indice-1] = personaje
print("CONTROLES:\n moverse hacia:\n w.arriba \n s.abajo \n a.izquierda \n d.derecha \n ")
while salida:
    if personaje in piso1:
        indice = piso1.index(personaje)
        direccion = input("-")
        if direccion == "d":
            derecha(piso1,indice)
        elif direccion == "a":
            izquierda(piso1,indice)
        elif direccion == "w":
            arriba(piso1,piso2,indice)
        elif direccion == "s":
            abajo(piso1,piso2,indice)
        else:
            pass
           
    elif personaje in piso2:
        indice = piso2.index(personaje)
        direccion = input("-")
        if direccion == "d":
            derecha(piso2,indice)
        elif direccion == "a":
            izquierda(piso2,indice)
        elif direccion == "w":
            arriba(piso2,piso1,indice)
        elif direccion == "s":
            abajo(piso2,piso1,indice)
        else:
            pass
          
    print(f"{piso2}\n{piso1}")
    time.sleep(.2)
    
    if ((personaje==piso2[4]) and (m==1)):
        print("batalla iniciada")
        resultado = batalla.batalla()    
        if resultado == True:
            m=2
            print("llego")
            salida = False