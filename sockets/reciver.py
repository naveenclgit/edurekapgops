import socket

def receiver(message_socket):
    received_message = message_socket.recv(1024).decode()
    message_socket.close()
    return received_message

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    received_message = receiver(client_socket)
    print("Receiver received:", received_message)

