import socket
import threading
import time

server_socket = None
client_socket = None

def start_server():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    accept_connections()

def accept_connections():
    global client_socket
    client_socket, client_address = server_socket.accept()
    while True:
        data = client_socket.recv(1024).decode()
        print("Cliente: " + data)

def connect_as_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input ("Ingresa la dirección IP del servidor: ")
    connected = False
    while not connected:
        try:
            client_socket.connect(('192.168.8.102', 12345))
            connected = True
        except Exception as e:
            print("Error al conectar:", e)
            time.sleep(1)

    while True:
        send_message()
        data = client_socket.recv(1024).decode()
        print("Servidor: " + data)

def send_message():
    if client_socket:
        message = input("Yo: ")
        client_socket.send(message.encode())

server_selected = False
while not server_selected:
    choice = input("Selecciona una opción:\n1. Iniciar como servidor 2. Conectar como cliente")

    if choice == '1':
        start_server()
        server_selected = True
    elif choice == '2':
        connect_as_client()
        server_selected = True
    else:
        print("Opción inválida. Inténtalo de nuevo.")

send_thread = threading.Thread(target=send_message)
send_thread.start()

