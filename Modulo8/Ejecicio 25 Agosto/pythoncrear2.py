try:
    Archivo = open("datos1.txt","r")
    print(Archivo.read())
    Archivo.close()
except:
    print("ERROR. no se encontro el archivo")
linea=Archivo=open("datos1.txt","r")
linea=Archivo.read()
Archivo.close()
if len(linea) == 0:
    print("el archivo esta vacio")
else:
    print(f"el archivo tiene {len(linea)} caracteres")
for numero,lineas in enumerate(linea,1):
    lineas_limpiar = linea.strip()
    dato = lineas_limpiar.split(",")
    print(f"registro #{numero}:")
    print(f"nombre :{dato[0]}")
    print(f"apellido:{dato[1]}")
    print(f"edad:{dato[2]}")
    print("fin de la transimision")