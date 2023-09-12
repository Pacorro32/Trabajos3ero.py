#Ejemplo de slicing en una lista
numeros=[0,1,2,3,4,5,6,7,8,9]

#Extraer una posición de la lista
sublista=numeros[2:6] #Extrae elementos desde el índice 2 hasta el 5(sin incluir en 6)
print(sublista) #Imprimirá[2,3,4,5]

#Usar paso para saltar elementos
saltados=numeros[1:9:2] #Extrae elementos desde el índice 1 hasta el 8, saltando de 2 en 2
print(saltados) #Imprimirá [1,3,5,7]

#Slicing sin inicio y fin (usará valores por defecto)
primeros=numeros[:5] #Extrae los primeros 5 elementos 
ultimos=numeros[5:] #Extrae desde el índice 5 hasta el final
print(primeros) #Imprimirá [0,1,2,3,4]
print(ultimos) #Imprimirá [5,6,7,8,9]