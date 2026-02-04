#Aqui se smula una batalla por un juego de piedra papel o tijera

import random
def batalla():
  a=random.randint(1,3)
  b = 0
  respuestas = [1,2,3]
  while not(b in respuestas):
    try: 
      b=float(input("1:piedra, 2:papel o 3:tijeras"))
    except:
      b=0
  g=False
  
  
  if a==b:
      print("empate") 
  elif (not a==b)  and (b==1 or b==2 or b==3):
   if a==1:
       if b==2:
          print("ganaste")
          g=True    
       elif b==3:
          print("perdiste") 
   elif(a==2):
        if(b==1):
          print("perdiste")    
        elif(b==3):
          print("ganaste") 
          g=True
   elif(a==3):
        if(b==1):
          print("ganaste")  
          g=True  
        elif(b==2):
          print("perdiste") 
  else:
    print("lee pedasito de chocoTavo")
    quit()
  print(f"tu oponente escogio {a}")
  return g