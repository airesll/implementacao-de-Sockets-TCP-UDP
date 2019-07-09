from socket import *
import time

#A UDP Client Socket
#criar socket(ipv4,udp)
clientSocket = socket(AF_INET, SOCK_DGRAM)

#endereco do servidor
host = 'localhost'
port = 12000
serverAddress = (host, port)

#esperar o tempo de 1 segundo
clientSocket.settimeout(1)

#mandar 10 pings
ping = 0
while ping < 10:

    #pegando o instante em segundos
    tempoDeEnvio = time.time()
    #criando mensagem
    mensagem = 'Ping: ' + str(ping) + " " + str(time.strftime("%H:%M:%S"))
    #encaminhando mensagem codificada para servidor
    clientSocket.sendto(mensagem.encode(), serverAddress)
    
    try:

        #confirmacao que o cliente esta recebendo uma resposta
        confirmacao,server = clientSocket.recvfrom(1024)
        tempoDeChegada = time.time()
        rtt = (tempoDeChegada - tempoDeEnvio)
        print (str(confirmacao.decode()) + ", rtt: " + str(rtt) + " s.")
    except timeout:
        print ("solicitacao expirada")
    ping = ping + 1