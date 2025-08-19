#Ámbito de las variables - locales y globales.

x = "global"

def ejemplo_ambito():
    x = "local"
    print("Dentro de la función:", x)

ejemplo_ambito()
print("Fuera de la función:", x)
