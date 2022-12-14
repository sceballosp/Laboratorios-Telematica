import socket
import threading

PORT = 80
ENCONDING_FORMAT = "utf-8"
RECV_BUFFER_SIZE = 100000000
IP_SERVER = '44.209.218.161'

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = IP_SERVER

def main():
  print("***********************************")
  print("Server is running...")
  print("Dir IP:",server_address )
  print("Port:", PORT)
  server_execution()


# Handler for manage incomming clients conections...
def handler_client_connection(client_connection,client_address):

  print()
  print("***********************************")
  print(f'New incomming connection is coming from: {client_address[0]}:{client_address[1]}')
    
  data_recevived = client_connection.recv(RECV_BUFFER_SIZE)
  remote_string = str(data_recevived.decode(ENCONDING_FORMAT))
  remote_command = remote_string.split()

  request = remote_command[0]
  fileName = remote_command[1]
  fileName = fileName.lstrip('/')
  print (f'Data received from: {client_address[0]}:{client_address[1]}')
  print(request, fileName)

  if request == 'GET':
    
    try:
      header = 'HTTP/1.1 200 OK\r\n'
      header += '\r\n'
      header = header.encode(ENCONDING_FORMAT)
      client_connection.sendall(header)

      file = open(fileName, 'rb')
      readFile = file.read(RECV_BUFFER_SIZE)
      while (readFile):
        client_connection.sendall(readFile)
        readFile = file.read(RECV_BUFFER_SIZE)
      file.close()
    
    except FileNotFoundError:
      header = 'HTTP/1.1 404 Not Found\r\n'
      header += '\r\n'
      header = header.encode(ENCONDING_FORMAT)
      client_connection.sendall(header)

  print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...')
  client_connection.close()


#Function to start server process...
def server_execution():
  tuple_connection = (server_address, PORT)
  server_socket.bind(tuple_connection)
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  print ('Socket is bind to address and port...')
  server_socket.listen(5)
  print('Socket is listening...')
  while True:
    client_connection, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handler_client_connection, args=(client_connection,client_address))
    client_thread.start()
  print('Socket is closed...')
  server_socket.close()

if __name__ == "__main__":
  main()