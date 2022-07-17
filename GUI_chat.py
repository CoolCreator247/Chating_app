from tkinter import *
import socket
insertText = Tk()
Label(insertText, text='->').grid(row=0)
message = Entry(insertText)
message.grid(row=0, column=1)
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print("Welcome to GUI chat")
print("Your Computer IP Address is:" + IP)
print("use this number to connect to others as your id")

def Main():
    port = 4005
    ip = input("The IP for the person you're talking with goes here>")
 
    
    server = (ip,port) #tells us who to send it to
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((IP,port))
    
    while message !='q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server: " + data)
        message = input("-> ")
    s.close()

if __name__=='__main__':
    Main()

mainloop()