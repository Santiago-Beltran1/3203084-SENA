linea=Archivo=open("datos.txt","r")
linea=Archivo.read()
Archivo.close()
if len(linea)==0:
    print("el archivo esta vacio")
else:
    print(f"el archivo tiene {len(linea)} caracteres")