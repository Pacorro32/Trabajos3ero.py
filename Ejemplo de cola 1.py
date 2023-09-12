from collections import deque

class Tienda:
    def __init__(self):
        self.cola_clientes = deque()  

    def agregar_cliente(self, cliente):
        self.cola_clientes.append(cliente)  
        print(f"{cliente} se unió a la cola.")

    def atender_siguiente_cliente(self):
        if self.cola_clientes:
            cliente = self.cola_clientes.popleft()  
            print(f"Atendiendo a {cliente}.")
        else:
            print("No hay clientes en la cola.")

            
#Crear una instancia de la tienda
tienda=Tienda()

#Agregar clientes a la cola
tienda.agregar_cliente("Cliente 1")
tienda.agregar_cliente("Cliente 2")
tienda.agregar_cliente("Cliente 3")

#Atender a los clientes en orden
tienda.atender_siguiente_cliente()
tienda.atender_siguiente_cliente()
tienda.atender_siguiente_cliente()
tienda.atender_siguiente_cliente()