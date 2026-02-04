import time
for i in "sesion abierta yeeeey\n\n":
 print(i, end="",flush=True)
 time.sleep(.0)
with open("sesion_abierta/mostrar_proyectos.py","r",encoding="utf-8") as proyecto:
    script = proyecto.read()
    exec(script)
