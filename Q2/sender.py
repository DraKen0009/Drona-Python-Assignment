import socket

def sender():
    host = 'localhost'
    port = 5000

    try:
        sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sender_socket.connect((host, port))

        while True:
            message = input("Enter message to send (type 'exit' to quit): ")
            sender_socket.sendall(message.encode())

            if message.lower() == 'exit':
                break

        sender_socket.close()

    except socket.error as e:
        print(f"Socket error: {e}")

if __name__ == "__main__":
    sender()
