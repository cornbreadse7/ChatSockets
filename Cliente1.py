import socket
import threading
import tkinter as tk

# Definir el host y el puerto en el que se ejecuta el servidor
HOST = '127.0.0.1'
PORT = 5000

# Crear una ventana de chat
root = tk.Tk()
root.title('Chat - Cliente 1')

# Crear una caja de entrada para el nombre de usuario
username_label = tk.Label(root, text='Usuario:')
username_label.pack(side=tk.LEFT)
username_entry = tk.Entry(root)
username_entry.pack(side=tk.LEFT)

# Crear una caja de entrada para los mensajes
message_label = tk.Label(root, text='Mensaje:')
message_label.pack(side=tk.LEFT)
message_entry = tk.Entry(root)
message_entry.pack(side=tk.LEFT)

# Función para enviar un mensaje al servidor
def send_message(event=None):
    username = username_entry.get()
    message = message_entry.get()
    # Enviar el mensaje al servidor
    client_socket.sendall(f'{username}: {message}'.encode())
    # Borrar la caja de entrada del mensaje
    message_entry.delete(0, tk.END)

# Configurar el botón de enviar mensaje
send_button = tk.Button(root, text='Enviar', command=send_message)
send_button.pack(side=tk.LEFT)

# Función para recibir mensajes del servidor
def receive_messages():
    while True:
        # Recibir datos del servidor
        data = client_socket.recv(1024)
        # Decodificar los datos recibidos
        message = data.decode()
        # Agregar el mensaje a la caja de texto
        chat_box.insert(tk.END, f'{message}\n')

# Conectar al servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Iniciar un hilo para recibir mensajes del servidor
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Crear una caja de texto para mostrar los mensajes
chat_box = tk.Text(root)
chat_box.pack()


# Iniciar la ventana de chat
root.mainloop()

# Cerrar la conexión del cliente
client_socket.close()
