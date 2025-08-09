edad = 10
permiso = True 

# AND: ambas condiciones deben cumplirse
and_ = (edad > 12) and permiso
print("Con AND:", and_)  # False → porque la edad no cumple

# OR: con que una condición sea verdadera, es suficiente
or_ = (edad > 12) or permiso
print("Con OR:", or_)  # True → porque tiene permiso

# NOT: invierte el valor lógico
menor = edad < 12
print("Es menor:", menor)       # True
print("NOT Es menor:", not menor)  # False → porque lo invierte
