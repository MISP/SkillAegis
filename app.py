#!/usr/bin/env python3
import argparse
import http.server
import socketserver
import os

HOST = ""
PORT = 8001

DASHBOARD_URL=""
EDITOR_URL=""

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global DASHBOARD_URL, EDITOR_URL

        if self.path == '/':
            self.path = 'application/welcome.html'
            with open(self.path, 'r') as file:
                html = file.read()
                html = html.replace('{{url_dashboard}}', DASHBOARD_URL).replace('{{url_editor}}', EDITOR_URL)
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


def main():
    global DASHBOARD_URL, EDITOR_URL
    parser = argparse.ArgumentParser(description='Parse command-line arguments for SkillAegis Dashboard.')

    parser.add_argument('--dashboard_url', type=str, required=True, help='The URL of the dashboard application')
    parser.add_argument('--editor_url', type=str, required=True, help='The URL of the editor application')
    parser.add_argument('--host', type=str, required=False, default=HOST, help='The host to listen to')
    parser.add_argument('--port', type=int, required=False, default=PORT, help='The port to listen to')

    args = parser.parse_args()

    if not args.dashboard_url.startswith('http'):
        parser.error(f"The dashboard URL is not valid: {args.dashboard_url}")
    else:
        DASHBOARD_URL = args.dashboard_url

    if not args.editor_url.startswith('http'):
        parser.error(f"The editor URL is not valid: {args.editor_url}")
    else:
        EDITOR_URL = args.editor_url

    Handler = MyHttpRequestHandler

    with socketserver.TCPServer((args.host, args.port), Handler) as httpd:
        print(f'Serving main server on {args.host}:{args.port}')
        httpd.serve_forever()

if __name__ == '__main__':
    main()
