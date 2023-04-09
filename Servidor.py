import socket
import threading

# Definir el host y el puerto en el que se ejecutará el servidor
HOST = '127.0.0.1'
PORT = 5000

# Crear un socket para el servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket con el host y el puerto
server_socket.bind((HOST, PORT))

# Escuchar conexiones entrantes
server_socket.listen()

# Lista para almacenar todos los clientes conectados
clients = []

# Función para enviar un mensaje a todos los clientes
def broadcast(message):
    for client in clients:
        client.sendall(message.encode())

# Función para manejar la conexión de un cliente
def handle_client(client_socket, client_address):
    # Agregar al cliente a la lista de clientes conectados
    clients.append(client_socket)
    print(f'New connection from {client_address}')
    while True:
        # Recibir datos del cliente
        data = client_socket.recv(1024)
        if not data:
            break
        # Decodificar los datos recibidos
        message = data.decode()
        print(message)
        # Enviar el mensaje a todos los clientes conectados
        broadcast(message)
    # Cerrar la conexión con el cliente
    client_socket.close()
    # Eliminar al cliente de la lista de clientes conectados
    clients.remove(client_socket)
    print(f'Connection from {client_address} closed')

# Función para aceptar conexiones entrantes
def accept_connections():
    while True:
        # Aceptar conexiones entrantes
        client_socket, client_address = server_socket.accept()
        # Iniciar un hilo para manejar la conexión del cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Iniciar un hilo para aceptar conexiones entrantes
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()
