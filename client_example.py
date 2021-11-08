import socket

def send_request(keywords, client):
    """
    Sends request with keywords to server.
    """
    client.send(keywords.encode())

def recv_response(client):
    """
    Receives image URLs as payload from server response.
    """
    urls = client.recv(2048).decode()
    client.close()
    return urls


if __name__ == "__main__":
    # Creates client and connects to server
    s = socket.socket()
    port = 12345
    s.connect((socket.gethostname(), port))

    # Sends request and receives response
    keyword = "Oregon State University"
    send_request(keyword, s)
    print(recv_response(s))
