# Web Server
## Soquetes para conexões TCP em Python vinculádo a um endereço e porta específicos, enviando e recebendo um pacote HTTP.
* O servidor Web desenvolvido manipula apenas uma
solicitação HTTP por vez, aceita solicitações
HTTP, obtem páginas solicitadas pelo cliente, e também cria
mensagens de resposta HTTP, constituída do arquivo solicitado
precedido pelas linhas de cabeçalho e, então, envia a resposta ao
cliente. Se o arquivo solicitado não estiver presente no servidor, o
servidor envia uma mensagem HTTP “404 Not Found” de
volta ao cliente.
