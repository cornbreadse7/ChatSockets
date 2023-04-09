import socket
import threading
import tkinter as tk

# Definir el host y el puerto en el que se ejecuta el servidor
HOST = '127.0.0.1'
PORT = 5000

# Crear una ventana de chat
root = tk.Tk()
root.title('Chat - Cliente 2')

# Crear una caja de entrada para el nombre de usuario
username_label = tk.Label(root, text='Username:')
username_label.pack(side=tk.LEFT)
username_entry = tk.Entry(root)
username_entry.pack(side=tk.LEFT)

# Crear una caja de entrada para los mensajes
message_label = tk.Label(root, text='Message:')
message_label.pack(side=tk.LEFT)
message_entry = tk.Entry(root)
message_entry.pack(side=tk.LEFT)

# Crear una caja de texto para mostrar la conversación
conversation_box = tk.Text(root, height=20, width=50)
conversation_box.pack()

# Crear una caja de texto para escribir el mensaje
message_box = tk.Text(root, height=2, width=50)
message_box.pack()

# Función para enviar un mensaje al servidor
def send_message():
    # Obtener el mensaje de la caja de texto y limpiar la caja
    message = message_box.get('1.0', tk.END).strip()
    message_box.delete('1.0', tk.END)

    # Enviar el mensaje al servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(message.encode('utf-8'))

# Crear un botón para enviar el mensaje
send_button = tk.Button(root, text='Enviar', command=send_message)
send_button.pack()

# Función para recibir mensajes del servidor
def receive_message(sock):
    while True:
        # Recibir un mensaje del servidor
        message = sock.recv(1024).decode('utf-8')

        # Mostrar el mensaje en la caja de texto de conversación
        conversation_box.insert(tk.END, message)

# Conectar con el servidor y empezar a recibir mensajes
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    receive_thread = threading.Thread(target=receive_message, args=(sock,))
    receive_thread.daemon = True
    receive_thread.start()

    # Ejecutar la ventana de chat
    root.mainloop()
import socket
import threading
import tkinter as tk

# Definir el host y el puerto en el que se ejecuta el servidor
HOST = '127.0.0.1'
PORT = 5000

# Crear una ventana de chat
root = tk.Tk()
root.title('Chat - Cliente 2')
root.geometry('400x500')

# Crear una caja de texto para mostrar la conversación
conversation_box = tk.Text(root, height=20, width=50)
conversation_box.grid(row=0, column=0, padx=10, pady=10)

# Crear una caja de texto para escribir el mensaje
message_box = tk.Text(root, height=2, width=50)
message_box.grid(row=1, column=0, padx=10, pady=10)

# Función para enviar un mensaje al servidor
def send_message():
    # Obtener el mensaje de la caja de texto y limpiar la caja
    message = message_box.get('1.0', tk.END).strip()
    message_box.delete('1.0', tk.END)

    # Enviar el mensaje al servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(message.encode('utf-8'))

# Crear un botón para enviar el mensaje
send_button = tk.Button(root, text='Enviar', command=send_message)
send_button.grid(row=2, column=0, padx=10, pady=10)

# Función para recibir mensajes del servidor
def receive_message(sock):
    while True:
        # Recibir un mensaje del servidor
        message = sock.recv(1024).decode('utf-8')

        # Mostrar el mensaje en la caja de texto de conversación
        conversation_box.insert(tk.END, message)

# Conectar con el servidor y empezar a recibir mensajes
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    receive_thread = threading.Thread(target=receive_message, args=(sock,))
    receive_thread.daemon = True
    receive_thread.start()

    # Ejecutar la ventana de chat
    root.mainloop()
