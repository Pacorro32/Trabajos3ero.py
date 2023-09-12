from collections import deque

cola=deque()

#Agregar elementos a la cola
cola.append(10)
cola.append(20)
cola.append(30)

#Eliminar y obtener elemento más antiguo de la cola
elemento=cola.popleft()
print(elemento) #Esto imprimirá 10