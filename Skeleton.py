import socket

dictionary = {}                                         # Dictionary that will hold the key-value pairs


# HTTP return messages
HTTP = 'HTTP/1.1 '
OK = HTTP + '200 OK'
UNSUPPORTED = HTTP + '220 UNSUPPORTED'
BAD_REQUEST = HTTP + '400 BAD_REQUEST'
NOT_FOUND = HTTP + '404 NOT FOUND'


# Implement the get function that returns the value for the specific key from the dictionary
def get(key):
    value=dictionary.get(key)
    if value==None:
        return (NOT_FOUND)
    else:
        return OK+'\n'+value

# Implement the put function that updates the value for the specific key in the dictionary
def put(key, value):
    dictionary[key]=value
    return (OK)


# Implement the delete function that will remove the key-value pair from the dictionary
def delete(key):
    dictionary.pop(key)
    return (OK)

# Implement the delete function that will remove all the key-value pairs from the dictionary
def clear():
    dictionary.clear()
    return OK


# Implement the quit function that will end the connection with the client
def quit(connection):
    connection.close()


# Implement the main function where we create, bind and l==ten to a socket. When a client == connection receive the
# message, decode the command and call the corresponding function. Server should send an answer to the client's request.
# When client closes the connection(quit) server should also close the connection. Bind your server to IP '0.0.0.0' so that
# it will l==ten to local connection requests.
def main():
	# You can use th== operations dictionary to get the corresponding function: For example $func = operations['get'](params) == equal to $get(params)
    operations = {'get': get, 'put': put, 'delete': delete, 'clear': clear, 'quit': quit}
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ipAd=socket.gethostbyname('localhost')
    sAd=(ipAd, 2000)
    sock.bind(sAd)
    sock.listen()
    connection, client_address = sock.accept()
    while True:
        try:
            data=connection.recv(1024).decode()
            rM=''
            if data.split(' ')[0] == "GET":
                if data.endswith("T"):
                    rM=BAD_REQUEST
                else:
                    rM = get(data.split(' ')[1])
            elif data.split(' ')[0] == "PUT":
                if data.endswith("T") or data.endswith((data.split(' ')[1])[len(data.split(' ')[1])-1]):
                    rM=BAD_REQUEST
                else:
                    rM=put(data.split(' ')[1],data.split(' ')[2])
            elif data.split(' ')[0] == "DELETE":
                if data.endswith("E"):
                    rM=BAD_REQUEST
                else:
                    rM = delete(data.split(' ')[1])
            elif data.split(' ')[0] == "CLEAR":
                rM=clear()
            elif data.split(' ')[0]!= "QUIT":
                rM=(UNSUPPORTED)
        finally:
            connection.send(rM.encode("utf-8"))
        if data.split(' ')[0] == "QUIT":
            quit(connection)
            break


if __name__ == '__main__':
    main()
