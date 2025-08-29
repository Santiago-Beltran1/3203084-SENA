#.append sirve para ingresar un nuevo indice (este que en el ultimo puesto de la lista):
lista = ["Jose", "Miguel", "Luis", "Pablo", "Pedro", "Juan"]
lista.append("Cristiano")
print(lista)


#.insert Inserta un nuevo indice en la posición que se le indique:
lista.insert(6, "Natalia")
print(lista)


#.extend Extiende la lista con los indices que se les indique:
lista.extend(["Jose", "Carlos", "Karen"])
print(lista)

#.remove Elimina el indice que se le indique:
lista.remove("Pedro")
print(lista)


#.pop Elimina el indice que se le indique:
lista.pop(3)
print(lista)

#.clear Limpia todos los indices:
lista.clear()
print(lista)