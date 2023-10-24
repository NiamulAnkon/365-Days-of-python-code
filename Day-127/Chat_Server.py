import socket
import threading


host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

clients = []

def handle_client(client):
  while True:
    try:
      message = client.recv(1024).decode("utf-8")
      
    except:
      clients.remove(client)
      client.close()
      break

def brodcast(message):
  for client in clients:
    try:
      client.send(message.encode("utf-8"))
    except:
      clients.remove(client)


def start_server():
  server.listen()
  print(f"Server is listening on {host}:{port}")
  while True:
    client, address = server.accept()
    print(f"Connected to {address[0]}:{address[1]}")
    clients.append(client)
    client.send("Welcome to the chat! Type your name and press Enter:".encode('utf-8'))
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()


if __name__ == "__main__":
  start_server()
    