import socket 
serverName = 'hostname'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Enter lowercase sentence:')
clientSocket.sendto(message,(serverName, serverPort))
Message, serverAddress = clientSocket.recvfrom(2048)
print(Message)
clientSocket.close()