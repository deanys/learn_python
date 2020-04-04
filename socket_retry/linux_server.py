from socket import *
HOST=""
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
while True:
    print("waiting for connection")
    tcpCliSock,addr=tcpSerSock.accept()
    print("accecpt is from",addr)

    while True:
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        data_str="serverce {}".format(data).encode()
        tcpCliSock.send(data_str)
tcpCliSock.close()
tcpSerSock.close()
