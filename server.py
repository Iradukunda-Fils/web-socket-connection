import socket


def main():
    server_socket: socket.socket = socket.socket()
    
    server_socket.bind(("localhost", 6060))
    
    server_socket.listen(1)
    print("Server is listening on port 6060...")
    
    conn, addr = server_socket.accept()
    
    print("Connection from address:", addr, "has been established!")
    print("conn:", conn)
    
    while True:
        data = conn.recv(1024).decode("utf-8")
        
        if data and len(data) > 0:
            print("client: ", data)
            conn.send(data.encode("utf-8"))
            
        if data.lower() == "exit":
            print("Exiting...")
            
            conn.send("exit".encode("utf-8"))
            conn.close()
            break

if __name__ == "__main__":
    main()
