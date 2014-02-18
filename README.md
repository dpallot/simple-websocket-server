<h2>A very simple WebSocket Server written in Python</h2>
<h3>No package installation, just one file, enjoy</h3>

Supports
  - Hixie 76 (Safari and iPhone)
  - RFC 6455 (All latest browsers)
  - TLS/SSL

<h3><a href = http://opiate.github.io/SimpleWebSocketServer>Click for the fancy Website</a></h3>

<h4>A Simple Echo Server Example</h4>

1) Write the client code by extending WebSocket
`````python
    from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
    
    class SimpleEcho(WebSocket):
        
        def handleMessage(self):
            if self.data is None:
                self.data = ''
                
            # echo message back to client
            self.sendMessage(str(self.data))
        
        def handleConnected(self):
            print self.address, 'connected'
              
        def handleClose(self):
            print self.address, 'closed'

    server = SimpleWebSocketServer('', 8000, SimpleEcho)
    server.serveforever()
`````

2) Run your code

3) Open up <i>websocket.html</i> and connect to the server

<h4>Want to get up and running faster?</h4>

There is an example which provides a simple echo and chat server

Echo Server

    python SimpleExampleServer.py --example echo

Chat Server (open up multiple <i>websocket.html</i> files)
    
    python SimpleExampleServer.py --example chat


<h4>TLS/SSL Example</h4>

1) Generate a certificate with key

    openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.pem
    
2) Run the secure TSL/SSL server (in this case the cert.pem file is in the same directory)

    python SimpleExampleServer.py --example chat --ssl 1 --cert ./cert.pem
    
3) Offer the certificate to the browser by serving <i>websocket.html</i> through https. 
The HTTPS server will look for cert.pem in the local directory. 
Ensure the <i>websocket.html</i> is also in the same directory to where the server is run. 

    sudo python SimpleHTTPSServer.py

4) Open a web browser to: <i>https://localhost:443/websocket.html</i>

5) Change <i>ws://localhost:8000/</i> to <i>wss://localhost:8000</i> and click connect. 

Note: if you are having problems connecting, ensure that the certificate is added in your browser against the exception https://localhost:8000 or whatever host:port pair you want to connect to. 

<h4>For the Programmers</h4>

def handleConnected(): called when handskake is complete

def handleClose(): called when the endpoint is closed or there is an error

def handleMessage(): gets called when there is an incoming message from the client endpoint
 - self.opcode: the WebSocket frame type (STREAM, TEXT, BINARY)
 - self.data: bytearray payload or None if there was no payload
 - self.address: TCP address port tuple of the endpoint
 - self.request: HTTP details from the WebSocket handshake (refer to BaseHTTPRequestHandler)
 - self.server.connections: map containing all the clients connected to the server

def sendMessage(buffer): send some text or binary data to the client endpoint
 - sending a buffer as str() will send a text based WebSocket frame otherwise a binary frame
 
def sendClose() : send close frame to endpoint


---------------------
The MIT License (MIT)

Copyright (c) 2013 Dave P.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
