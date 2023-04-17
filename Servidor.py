import socket
import threading

# Definir el host y el puerto en el que se ejecutará el servidor
HOST = '127.0.0.1'
PORT = 5000

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket del servidor al host y puerto especificados
server_socket.bind((HOST, PORT))

# Escuchar nuevas conexiones entrantes
server_socket.listen()

# Lista para almacenar los clientes conectados
clients = []

# Función para enviar mensajes a todos los clientes
def broadcast(message, sender):
    for client in clients:
        # Enviar el mensaje a todos los clientes, excepto al que lo envió
        if client != sender:
            client.sendall(message)
        elif client == sender:
            client.sendall(message)

# Función para manejar la conexión de un cliente
def handle_client(client_socket, client_address):
    print(f'Nuevo cliente conectado: {client_address}')
    # Agregar el cliente a la lista de clientes
    clients.append(client_socket)

    # Loop para recibir y enviar mensajes
    while True:
        # Recibir el mensaje del cliente
        data = client_socket.recv(1024)
        if not data:
            # Si no hay datos, se rompe el bucle
            break
        # Enviar el mensaje a todos los demás clientes
        broadcast(data, client_socket)

    # Cerrar la conexión del cliente
    client_socket.close()
    # Eliminar el cliente de la lista de clientes
    clients.remove(client_socket)
    print(f'Cliente desconectado: {client_address}')

# Función para esperar nuevas conexiones
def wait_for_connections():
    while True:
        # Esperar una nueva conexión entrante
        client_socket, client_address = server_socket.accept()
        # Iniciar un hilo para manejar la conexión del cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Iniciar un hilo para esperar nuevas conexiones
connection_thread = threading.Thread(target=wait_for_connections)
connection_thread.start()

