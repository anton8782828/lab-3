import ssl
import socket


HOST = '127.0.0.1'  
PORT = 80        


context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.verify_mode = ssl.CERT_REQUIRED 
context.load_cert_chain(certfile="client_certificate.pem", keyfile="client_private.key")
context.load_verify_locations("ca_certificate.pem") 


with socket.create_connection((HOST, PORT)) as client_socket:
    with context.wrap_socket(client_socket, server_hostname=HOST) as tls_client_socket:
        try:
            print("Підключено до сервера.")

        
            data = tls_client_socket.recv(1024).decode()
            print("Отримано від сервера:", data)
        except ssl.SSLError as e:
            print("SSL помилка:", e)

