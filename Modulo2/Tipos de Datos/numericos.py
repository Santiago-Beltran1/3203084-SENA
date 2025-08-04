#Variables Y Tipos De Datos

#1.Númericos

#-int (Enteros): números enteros (positivos o negativos).
año = 2025
siglo = 100
s = año + siglo
print(s)
print(type(s))

#float (Flotantes): Números de punto flotante o con decimales.
altura = 1.70
cm = 0.10
s2 = altura - cm
print(s2)
print(type(s2))

#decimal (Precisión decimal alta): Para cálculos más exactos que float.
from decimal import Decimal

precio = Decimal('2.50')   
cantidad = Decimal('4')            

total = precio * cantidad

print("Total a pagar:", total)        
print(type(total))                   

#complex (Números complejos): Estos tienen parte real e imaginaria.
n = 200 + 3j
print(n, type(n))  
