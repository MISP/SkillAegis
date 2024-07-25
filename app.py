#!/usr/bin/env python3
import http.server
import socketserver
import os
import config

HOST = ""
PORT = 8001

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'application/welcome.html'
            with open(self.path, 'r') as file:
                html = file.read()
                html = html.replace('{{url_dashboard}}', config.url_dashboard).replace('{{url_editor}}', config.url_editor)
                # Write the modified HTML to the response
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(html, "utf8"))
        elif self.path == '/skillaegis-logo.svg':
            image_path = 'application/skillaegis-logo.svg'
            if os.path.exists(image_path):
                self.send_response(200)
                self.send_header("Content-type", "image/svg+xml")
                self.end_headers()
                with open(image_path, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                self.send_error(404, "File not found")
        elif self.path == '/skillaegis-logo.png':
            image_path = 'application/skillaegis-logo.png'
            if os.path.exists(image_path):
                self.send_response(200)
                self.send_header("Content-type", "image/png")
                self.end_headers()
                with open(image_path, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                self.send_error(404, "File not found")
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print('Serving main server on port 8001')
    httpd.serve_forever()

