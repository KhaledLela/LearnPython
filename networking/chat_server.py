import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Use your host IP or 'localhost'
PORT = 8000  # Choose an available port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# List to store connected clients
clients = []


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # Remove the client if no message is received
                clients.remove(client_socket)
                print("Client disconnected")
                break

            print(f"Received: {message}")
            # Broadcast the message to all clients
            for client in clients:
                if client != client_socket:
                    client.send(message.encode('utf-8'))
        except:
            # Remove the client in case of errors
            clients.remove(client_socket)
            print("Client disconnected")
            break


while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f"Connected with {client_address}")

    # Start a thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
