import socket

def receiver():
    host = 'localhost' 
    port = 5000

    try:
        receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        receiver_socket.bind((host, port))
        receiver_socket.listen(1)
        conn, addr = receiver_socket.accept()
        print(f"Connection established with {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received message: {data.decode()}")

        conn.close()
        receiver_socket.close()

    except socket.error as e:
        print(f"Socket error: {e}")

if __name__ == "__main__":
    receiver()
