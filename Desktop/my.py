from http.server import HTTPServer, SimpleHTTPRequestHandler
PORT = 8000
server_address = ('127.0.0.1', PORT)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f"Serving on http://127.0.0.1:{PORT} (localhost only)")
httpd.serve_forever()