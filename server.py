from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is ready to receive")
while 1:
	message, clientaddress = serverSocket.recvfrom(2048)
	Message = message.upper()
	serverSocket.sendto(Message, clientaddress)
