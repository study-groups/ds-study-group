import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 8000))
    print(f"Serving on port {PORT}")

    with TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()

