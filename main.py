import socket

host = ""
port = 0
m    = ""

host = str(input('      Informe o host: '))
port = int(input('      Informe a porta: '))
msg  = str(input('      Mensagem a ser enviada: '))
print('OK, vou conectar com: ', host,":", port)

HOST = host                  # Endereco IP do Servidor
PORT = port                  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Conectei')
tcp.send (msg.encode())
tcp.close()

