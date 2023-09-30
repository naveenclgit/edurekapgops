import socket

def sender(message_socket):
    message = "Hello, Receiver!"
    message_socket.send(message.encode())
    message_socket.close()

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Waiting for Receiver to connect...")
    conn, addr = server_socket.accept()
    print("Receiver connected from:", addr)

    sender(conn)

