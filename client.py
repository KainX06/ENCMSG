import socket




#42070 as port
#main port (CHAD PORT CUZ WE CHADS)
CHAD_PORT = 443

global destination_ip
destination_ip = "placeholder"

# Gets destination IP from user
def ask_for_destination():
  global destination_ip 
  input("Destination IP Address: ")

## CLIENT ##
#creates client socket
def start_client():
  ask_for_destination()
  send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  #attempts to connect to server
  try:
    send_socket.connect((destination_ip, CHAD_PORT))
    
  except socket.error as e:
    print(f"Failed to connect to server: {e}")
    return()

  print(f"Connected to {destination_ip}")

def send_message(message_to_send):
  send_socket.send(message_to_send.encode('utf-8'))
  print("Sent!")
  