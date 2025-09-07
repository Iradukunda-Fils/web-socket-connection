# web-socket-connection

A simple socket-based client-server communication example built in Python using the `socket` module.  
This project demonstrates how to establish a connection between a client and a server, send messages, and handle responses.

---

## 📂 Project Structure

```bash
├── client.py          # Client-side implementation
├── server.py          # Server-side implementation
├── main.py            # Entry point (optional for orchestration)
├── pyproject.toml     # Project dependencies (managed by uv)
├── uv.lock            # Lock file (managed by uv)
└── README.md          # Project documentation
```

## ⚡ Requirements

- Python 3.10+

- [uv](https://github.com/astral-sh/uv)


## 🚀 Setup

### Clone the repository
---

```bash
git clone https://github.com/your-username/web-socket-connection.git
cd web-socket-connection
```


### Install dependencies using uv

```bash
uv sync
```


### Run the server

```bash
python server.py
```


### Run the client in another terminal

```bash
python client.py
```

--- 

## 🖥️ Usage Example

Server Output
---

```bash
Server is listening on port 6060...
Connection from address: ('127.0.0.1', 54321) has been established!
client: Hello Server
client: exit
Exiting...
```

Client Output
---

```bash
-> Hello Server
You: Hello Server
Server: Hello Server
-> exit
You: exit
Server: exit
Exiting...
```

---

## 📜 Code Overview

Client (`client.py`)
---

```python
import socket

client_socket: socket.socket = socket.socket()
client_socket.connect(("localhost", 6060))

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
```


Server (`server.py`)
---

```python
import socket

def main():
    server_socket: socket.socket = socket.socket()
    server_socket.bind(("localhost", 6060))
    server_socket.listen(1)
    print("Server is listening on port 6060...")

    conn, addr = server_socket.accept()
    print("Connection from address:", addr, "has been established!")

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
```

---

## 📌 Notes

Replace "`localhost`" with "`127.0.0.1`" if running locally.

Communication stops when either client or server sends exit.

This is a basic blocking socket example (no concurrency or threading).