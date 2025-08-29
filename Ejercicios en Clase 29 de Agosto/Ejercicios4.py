#Imprime la posición en el que esta cada indice:
lista = ["Jose", "Miguel", "Luis", "Pablo", "Pedro", "Juan"]
for i in range(len(lista)):
    print(i, ":", lista[i] )

#Según el valor que se le indique dirá si esta o no en la lista:
    lista3 = "percento" in lista
print(lista3)

#.count Indica cuántas veces esta un indice en una lista:
lista4 = ["a","a","b","b","c", "c", "a"]
cantidad = lista4.count ("a")
print(cantidad)


#.sort Ordena todos los indices de la lista en orden alfabetico:
lista.sort()
print(lista)

lista2 = [1,2,3,5,7,9,8,10,12,15,20,30]
lista2.sort()
print(lista2)


#sorted También ordena elementos
lista6 = sorted(lista)
print(lista6)


#.reverse pone los indices de la lista de forma contraria
lista.reverse()
print(lista)

#.copy crea una nueva lista a partir de la original y con list se crea una copia pero dentro de una misma lista
lista6 = lista.copy()
lista7 = list(lista)
print(lista6)
print(lista7)