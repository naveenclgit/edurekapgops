import socket

def main():
    host = "localhost"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by: {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received: {data}")

        response = input("Enter your response: ")
        conn.send(response.encode())

    conn.close()

if __name__ == "__main__":
    main()

