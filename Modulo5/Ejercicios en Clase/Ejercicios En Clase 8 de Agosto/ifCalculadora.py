r = (input("Seleccione el tipo de operación (+, -, *, /) "))

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

if r == "+":
    print(n1+n2)
else:
    if r == "-":
        print(n1-n2)
    else:
        if r == "*":
            print(n1*n2)
        else:
            if r == "/":
                print(n1/n2)