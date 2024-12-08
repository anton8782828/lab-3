import ssl
import socket


HOST = '127.0.0.1'
PORT = 80  


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server_certificate.pem", keyfile="server_private.key")
context.load_verify_locations("ca_certificate.pem")
context.verify_mode = ssl.CERT_REQUIRED  


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("Сервер очікує підключення...")

    with context.wrap_socket(server_socket, server_side=True) as tls_server_socket:
        conn, addr = tls_server_socket.accept()
        print(f"Підключено до {addr}")
        data = conn.recv(1024).decode()
        print("Отримано:", data)
        conn.sendall(b"Hello, Client!")
        conn.close()
