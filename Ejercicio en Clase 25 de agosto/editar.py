try:
    Archivo = open("datos1.txt", "r")
    lineas = Archivo.readlines()
    Archivo.close()
    for numero,lineas in enumerate(lineas,1):
        datos = lineas.strip().split(",")
        print(f"{numero}. {datos[0]}-{datos[1]}")
    for numero,lineas in enumerate(lineas,1):
       lineas_limpiar = lineas.strip()
       datos = lineas_limpiar.split(",")

       print(f"registro#{numero}")
       print(f"nombre{datos[0]}")
       print(f"apellido#{datos[1]}")
       print(f"edad#{datos[2]}")
       print("fin de la transmision")

       datos_actuales = lineas [numero -1] .strip() .split (",")
       print(f"\n editando registro {numero }")
       print(f"\n nombre actual {datos_actuales[0] }")
       print(f"\n apellido {datos_actuales[1] }")
       print(f"ingrese los nuevos datos")

       nuevo_nombre = input("ingrese dato")
       nuevo_apellido = input("ingrese dato")
       lineas[numero -1] = nuevo_nombre
       Archivo = open ("datos1.txt", "w")
       Archivo.writelines(lineas)
       Archivo.close()
       print("Registro editado")
except:
    if len(lineas) == 0:
     print("No hay archivo para editar")
     for numero,lineas in enumerate(lineas,1):
        datos = lineas.strip().split(",")
        print(f"{numero}.{datos[0]}-{datos[1]}")
     for numero,lineas in enumerate(lineas,1):
       lineas_limpiar = lineas.strip()
       datos = lineas_limpiar.split(",")

       print(f"registro#{numero}")
       print(f"nombre{datos[0]}")
       print(f"apellido#{datos[1]}")
       print(f"edad#{datos[2]}")
       print("fin de la transmision")

       datos_actuales = lineas [numero-1] .strip() .split (",")
       print(f"\n editando registro {numero }")
       print(f"\n nombre actual {datos_actuales[0] }")
       print(f"\n apellido {datos_actuales[1] }")
       print(f"ingrese los nuevos datos")

       nuevo_nombre = input("ingrese dato")
       nuevo_apellido = input("ingrese dato")
       lineas[numero -1] = nuevo_nombre
       Archivo = open ("datos1.txt", "w")
       Archivo.writelines(lineas)
       Archivo.close()
       print("Registro editado")