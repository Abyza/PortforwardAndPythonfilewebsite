import socket

HOST = '0.0.0.0'
PORT = 80

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server is listening on port {PORT}...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Define a basic HTML response
    html_response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
    <html>
    <head><title>Hello</title></head>
    <body>
    <h1>Abyza's Server Code:duck1</h1>
    </body>
    </html>
    """

    # Send the HTML response to the client
    client_socket.sendall(html_response.encode('utf-8'))

    # Close the connection with the client
    client_socket.close()