#Ejemplo de diccionario de edades 
edades={"Juan":25,"María":30,"Pedro":22}

#Ejemplo de diccionario de información de una persona
persona={
    "nombre":"Ana",
    "edad":28,
    "ciudad":"Madrid"
}

#Accediendo a valores en el diccionario por clave
print(edades["Juan"]) #Imprimirá 25
print(persona["ciudad"]) #Imprimirá "Madrid"

#Modificando valores en el diccionario
edades["Laura"]=23
persona["profesion"]="Ingeniera"

#Eliminado elementos del diccionario
del edades["Pedro"]
persona.pop("ciudad")

#Verificando si una clave existe en el diccionario
if "Laura" in edades:
    print("Laura está en el diccionario")
    
#Obteniendo todas las claves y valores del diccionario
claves=edades.keys()
valores=edades.values()

#Longitud del diccionario
print(len(persona)) #Imprimirá 3