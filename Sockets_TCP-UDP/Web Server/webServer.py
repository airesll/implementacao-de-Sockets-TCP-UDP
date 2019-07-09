#import socket module
from socket import *
import sys # para terminar o programa

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepara o socket servidor
serverSocket.bind(('localhost', 12000))  
serverSocket.listen(1) 

while True:
    #Estabelece a conexao
    print ('Ready to serve...')   
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:],'r')
        outputdata = f.read()
        connectionSocket.send('HTTP/1.0 200 OK')
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
            connectionSocket.send(outputdata.encode())
            connectionSocket.close()
    except IOError:
        connectionSocket.send('404 Not Found')
        connectionSocket.close()
        serverSocket.close()
        break 
    sys.exit()#Termina o programa depois de enviar os dados
    