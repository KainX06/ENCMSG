import server
import client

program_running = True
server_running = False
client_running = False

## Commands ##

"""
List of commands:
/start_client /sc ~ starts the client
/start_server /ss ~ starts the server
/disconnect /d ~ disconnects the client and server
/refresh /r ~ checks for new messages
/close /c ~ closes the program
"""

def enter_text():
  entered_text = input()

  if entered_text[0] == "/":
    if entered_text in ("/start_client", "/sc"):
      client.start_client()
      client_running = True
      
    elif entered_text in ("/start_server", "/ss"):
      server.start_server()
      server_running = True
      
    elif entered_text in ("/disconnect", "/d"):
      pass
      
    elif entered_text in ("/refresh", "/r"):
      server.recieve_message()

    elif entered_text in ("/close", "/c"):
      program_running = False
      
    else:
      print("Invalid command")
  else:
    if client_running:
      client.send_message(entered_text)
    else:
      print("Client not connected")

## ON RUN ##
while program_running:
  enter_text()
  
