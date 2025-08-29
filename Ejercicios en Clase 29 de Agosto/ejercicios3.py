#Llamo dentro de una lista otra lista:
lista = ["Jose", "Miguel", "Luis", "Pablo", "Pedro", "Juan"]
lista2 = lista
print(lista2)


#llamo solo una parte de la lista:
lista = ["Jose", "Miguel", "Luis", "Pablo", "Pedro", "Juan"]
lista2 = lista [2:4] 
print(lista2)



#Invertir orden de lista:
lista = ["Jose", "Miguel", "Luis", "Pablo", "Pedro", "Juan"]
lista2 = lista [::-1] 
print(lista2)


#Llama al 3 indice inversamente:
lista = ["Jose", "Miguel", "Luis", "Pablo", "Pedro", "Juan"]
lista2 = lista [-3] 
print(lista2)


#cambia un elemento en una lista:
lista2 = [1,2,3,5,7,9,8,10,12,15,20,30]
lista2[6] = "pepe"
print(lista)