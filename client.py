import socket


client_socket: socket.socket = socket.socket()


client_socket.connect(("bytemonk", 6060))




def main():
    while True:
        msg = input("-> ")
        
        client_socket.send(msg.encode("utf-8"))
        data = client_socket.recv(1024).decode("utf-8")
        
        if data and len(data) > 0:
            print("You: ", msg)
            print(f"Server: {data}")
            
        if data.lower() == "exit":
            print("Exiting...")
            client_socket.close()
            break


if __name__ == "__main__":
    main()
