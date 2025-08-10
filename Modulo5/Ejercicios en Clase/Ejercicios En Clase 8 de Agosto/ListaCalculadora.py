lista=["suma", "resta", "multiplicar", "dividir"]

ingresar = (int(input("ingrese el numero (1=suma 2=resta 3=multiplicar 4=dividir: ")))
n1 =(float(input("ingrese el primer numero: ")))
n2 =(float(input("ingrese el segundo numero: ")))

if ingresar == 1:
    print("Usted eligió: ", lista[0])
    print("Resultado de la operación: ", n1+n2)
else:
    if ingresar == 2:
        print("Usted eligió: ", lista[1])
        print("Resultado de la operación: ", n1-n2)
    else:
        if ingresar == 3:
            print("Usted eligió: ", lista[2])
            print("Resultado de la operación: ", n1*n2)
        else:
            if ingresar == 4:
                print("Usted eligió: ", lista[3])
                print("Resultado de la operación: ", n1/n2)