try:
    Archivo = open("datos1.txt", "r")
    lineas = Archivo.readlines()
    Archivo.close()
except:
    if len(lineas) == 0:
       print("no hay registros")
       exit()
       for numero, linea in enumerate (lineas,1):
          dato = linea.strip().split(",")
          print(f"{numero}.{dato[0]}-{dato[1]}")
          print()
    numeroregistro = input("Que numero de registro quieres borrar")
    numeroregistro = int(numeroregistro)
    if numeroregistro < 1 or numeroregistro < len(lineas):
       print("NUmero de registro no valido")
       exit()
    dato_borrar = lineas[numeroregistro - 1].strip().split(",")
    print(f"\n vas a borrar un registro{numeroregistro}")
    print(f"\n nombre a borrar{dato_borrar[0]}")
    print(f"\n apellido a borrar{dato_borrar}")