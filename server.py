import socket
server = socket.socket()
host = socket.gethostname()
port = 8080
server.bind((host,port))
server.listen(5)
while True:
    conn, addr = server.accept()
    print("Connection successful from:", addr)
    conn.send(bytes("hi", 'utf-8'))
    conn.close
