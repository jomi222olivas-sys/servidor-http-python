import socket
import threading
import os
import mimetypes
import logging
from datetime import datetime

# --- LOGGING CONFIGURATION ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class HTTPWebServer:
    def __init__(self, host='127.0.0.1', port=8080, public_dir='public'):
        self.host = host
        self.port = port
        self.public_dir = public_dir
        self.server_socket = None

    def start(self):
        """Starts the server and listens for incoming connections."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            logging.info(f"🚀 Server started at http://{self.host}:{self.port}")
            logging.info(f"📂 Serving files from: {self.public_dir}/")
            
            while True:
                client_socket, client_address = self.server_socket.accept()
                logging.info(f"Incoming connection from: {client_address[0]}")
                
                # Handle client in a separate thread
                client_thread = threading.Thread(
                    target=self.handle_client, 
                    args=(client_socket,)
                )
                client_thread.start()
                
        except KeyboardInterrupt:
            logging.info("Stopping server...")
        except Exception as e:
            logging.error(f"Critical server error: {e}")
        finally:
            if self.server_socket:
                self.server_socket.close()

    def handle_client(self, client_socket):
        """Handles the request/response logic for a client."""
        try:
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                return

            # Parse the first line (e.g., GET /index.html HTTP/1.1)
            headers = request.split('\n')
            first_line = headers[0].split()
            
            if len(first_line) < 2:
                return
                
            method = first_line[0]
            path = first_line[1]

            if method == 'GET':
                self.handle_get(client_socket, path)
            elif method == 'POST':
                self.handle_post(client_socket)
            else:
                self.send_response(client_socket, 405, "Method Not Allowed")

        except Exception as e:
            logging.error(f"Error handling client: {e}")
        finally:
            client_socket.close()

    def handle_get(self, client_socket, path):
        """Handles GET requests to serve static files."""
        if path == '/':
            path = '/index.html'
        
        # Sanitize path
        filename = path.lstrip('/')
        file_path = os.path.join(self.public_dir, filename)

        if os.path.exists(file_path) and os.path.isfile(file_path):
            # Auto-detect MIME type
            content_type, _ = mimetypes.guess_type(file_path)
            if content_type is None:
                content_type = 'application/octet-stream'

            try:
                with open(file_path, 'rb') as file:
                    content = file.read()
                self.send_response(client_socket, 200, "OK", content, content_type)
            except Exception as e:
                logging.error(f"Could not read file: {e}")
                self.send_response(client_socket, 500, "Internal Server Error")
        else:
            self.send_response(client_socket, 404, "Not Found", b"<h1>404 - File Not Found</h1>")

    def handle_post(self, client_socket):
        """Handles simulated POST requests."""
        response_body = b"""
            <html><body>
                <h1>Data Received Successfully</h1>
                <p>The server processed your POST request.</p>
                <a href="/">Go Back</a>
            </body></html>
        """
        self.send_response(client_socket, 200, "OK", response_body)

    def send_response(self, client_socket, status_code, status_message, body=b"", content_type="text/html"):
        """Constructs and sends the raw HTTP response."""
        header = f"HTTP/1.1 {status_code} {status_message}\r\n"
        header += f"Content-Type: {content_type}\r\n"
        header += f"Content-Length: {len(body)}\r\n"
        header += "Server: Python-Custom-Server/1.0\r\n"
        header += "Connection: close\r\n\r\n"
        
        client_socket.send(header.encode('utf-8') + body)

if __name__ == "__main__":
    server = HTTPWebServer()
    server.start()