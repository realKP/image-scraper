import socket
import image_scraper

# Creates server and begins listening
s = socket.socket()
print ("Server successfully created")
port = 12345
s.bind(('', port))
print ("Server binded to %s" %(port))
s.listen(5)

while True:
    # Connects to client
    c, addr = s.accept()
    print("Got connection from", addr )

    # Receives request and calls image scraper
    keywords = c.recv(2048).decode()
    number_of_images = 3
    urls = image_scraper.image_scrape(keywords, number_of_images)

    # Sends response to client and closes connection
    c.send(str(urls).encode())
    print("Response sent. Closing connection...")
    c.close()
    break
