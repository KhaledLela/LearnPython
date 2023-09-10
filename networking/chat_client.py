import socket
import threading

# Server configuration
HOST = 'localhost'  # Use the server's IP or 'localhost'
PORT = 8000  # Use the same port as the server

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred while receiving messages.")
            break


# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main loop to send messages
while True:
    message = input()
    client_socket.send(message.encode('utf-8'))
