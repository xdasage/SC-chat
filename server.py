import socket
import threading 
def handle_client(c, addr):
    print(f"[NEW CONNECTION] Connected to {addr}")

    while True:    
        message = c.recv(1024).decode()
        if not message:
                print(f"[DISCONNECTED] {c} disconnected.")
                break
        print(f"Client: {message}")

            
        reply = input("Server: ")
        c.send(reply.encode())
    c.close()

def start():
    obj=socket.socket()
    print("created")
    host = '127.0.0.1'
    port=12345

    obj.bind((host,port))
    print(f"Socket binded to {port}")

    obj.listen(5)
    print("listening")

    while True:
        c,addr=obj.accept()
        handle_client(c,addr)
        print(f"got connection from{addr}")
if __name__=="__main__":
     start()
    


