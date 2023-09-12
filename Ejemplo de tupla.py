#Ejemplo de tupla de números
numeros=(1,2,3,4,5)

#Ejemplo de tupla de cadenas de texto 
frutas=("manzana","banana","naranja","uva")

#Ejemplo de tupla mixta
mixta=(1,"hola",3.14,"mundo")

#Accediendo a elementos de la tupla por índice
print(numeros[0]) #Imprimirá 1
print(frutas[2]) #Imprimirá "naranja"

#Las tuplas son inmutables, por lo que no puedes modificar sus elementos
#mixta[1]="saludos" #Esto generará un error 

#Longitud de una tupla 
print(len(frutas)) #Imprimirá 4