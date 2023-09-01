import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipaddress = input("Enter your ip address:")
port = int(input("Enter port number:"))

def portscanner(port):
    if sock.connect_ex((ipaddress,port)):
        print(f'PORT {port} is closed ')

    else:
        print(f'PORT {port} is open')


portscanner(port)
