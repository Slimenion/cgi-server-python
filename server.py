from http.server import HTTPServer, CGIHTTPRequestHandler

server_adress = ("", 8081)
httpd = HTTPServer(server_adress, CGIHTTPRequestHandler)
httpd.serve_forever()
