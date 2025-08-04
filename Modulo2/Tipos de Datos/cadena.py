#Variables Y Tipos De Datos

#3.Cadenas de texto

#Una variable de tipo cadena guarda texto encerrando el dato entre comillas "" los cuales son de tipo string(cadena)

texto = "Hola Mundo"

print(texto.upper(), type(texto.upper()))         
print(texto.lower(), type(texto.lower())) 
print(texto.capitalize(), type(texto.capitalize())) 
print(texto.title(), type(texto.title()))         
print(texto.swapcase(), type(texto.swapcase())) 
print(texto.replace("Hola", "Adiós"), type(texto.replace("Hola", "Adiós")))  
print(len(texto), type(len(texto)))            

#El último aunque es entero representa una longitud de texto.