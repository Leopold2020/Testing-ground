import socket

# figure out my ip adress

HOST = ""
# localhost or 127.0.0.1 if you want to do local

# choose a port to 
PORT = 9090


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"server is listening on {HOST, PORT}")

while True:
    communication_socket, adress = server.accept()
    print(f"someone has conected from {adress}")
    message = communication_socket.recv(1024)


    decoded_message = message.decode("utf-8")
    
    print(f"Message: {decoded_message}")
    communication_socket.send(f"You said: {decoded_message}".encode("utf-8"))
    communication_socket.close()
    print("")