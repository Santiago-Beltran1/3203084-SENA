try:
    Archivo = open("datos.txt","r")
    lineas = Archivo.readlines()
    Archivo.close()
    if (len(lineas)) == 0 :
        print("no registros guardados")
except:
    lineas = Archivo.readlines()
    Archivo.close()
    if (len(lineas)) == 0 :
        print("no registros guardados")
    else :
        print(f"se creo {len(lineas)}") 