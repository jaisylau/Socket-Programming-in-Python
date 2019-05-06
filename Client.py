
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 2000                                  # Choose the port number your server is bound to
sock.connect(('localhost', port))           # Connects to given port number on the local machine

while True:
    cmd = input("")                         # Get command line input to send to server
    split = cmd.split(' ')                  # Split the command by the space characters
    if split[0].lower() != "quit":
        sock.send(cmd.encode("utf-8"))      # Send the command line to server
        print(sock.recv(1024).decode())     # Print the received messaged
    else:
        sock.send(cmd.encode("utf-8"))      # Send the quit message to server
        sock.close()                        # Close the program
        print('Connection Closed')
        break                               # Terminate the client program
