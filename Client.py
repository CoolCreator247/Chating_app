import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("your port is 4005 Your Computer IP Address is:" + IPAddr)
print("use this number to connect to others as your id")

def Main():
    port = input(" The person you're chatting with port number goes here>")
    ip = input("The IP for the person you're talking with goes here>")
    host=IPAddr #IP
    port = 4005
    
    server = (ip, port)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    
    message = input("-> ")
    while message !='q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server: " + data)
        message = input("-> ")
    s.close()

if __name__=='__main__':
    Main()