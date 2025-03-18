import socket
import threading
def receive_messages(client_socket):
    while True:
        
            
            message = client_socket.recv(1024).decode()
            if not message:
                print("[DISCONNECTED] Server disconnected.")
                break

            print(f"Server: {message}")

def start():
    obj=socket.socket()
    port=12345
    obj.connect(('127.0.0.1',port))
    print(f"[CONNECTED] Connected to server at 127.0.0.1:{port}")
    t=threading.Thread(target=receive_messages,args=(obj,))
    t.start()
    while True:
         m=input(" ")
         print(" : Client")
         obj.send(m.encode())
if __name__=="__main__":
     start()
