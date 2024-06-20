import socket

#42070 as port
#main port (CHAD PORT CUZ WE CHADS)
CHAD_PORT = 443

## SERVER ##
def start_server():
  #creates server socket
  listen_socket = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
  
  #binds server socket to port and computer's ip
  listen_socket.bind(('127.0.0.1', CHAD_PORT))
  
  #starts listening for incoming connections
  listen_socket.listen()
  print("Server listening on port", CHAD_PORT)
  
  #Creates new connection socket (conn) and addr (contains both IP and port of connection)
  conn , addr = listen_socket.accept()
  
#recieves data from message
def recieve_message():
  recieved_data = conn.recv(4096)
  if message is not None:
    message = recieved_data.decode('utf-8')
    print("Client: " + message)

