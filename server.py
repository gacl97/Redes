#!/usr/bin/python

import socket
import _thread as td

address = ("localhost", 20000)

# Create sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect sockets
server_socket.bind(address)
server_socket.listen(1)

def client(server_input, address):

  while True:

    response = server_input.recv(1024)
    response = response.rstrip()
    if (response.decode() == "sair" or not response.decode()):
      # server_input.close()
      server_socket.close()
      break
    else:
      print ("Mensagem do cliente:(",address[1],")", response.decode())



# Print
while True:
  server_input, address = server_socket.accept()
  print ("Nova conexao recebida de ", address)
  td.start_new_thread(client, (server_input, address))
  
    

