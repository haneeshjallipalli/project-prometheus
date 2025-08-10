# Placeholder demo service (very small) - exposes /metrics
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/metrics':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; version=0.0.4')
            self.end_headers()
            # Minimal example metric
            self.wfile.write(b'# HELP demo_dummy_total A dummy counter\n')
            self.wfile.write(b'demo_dummy_total 42\n')
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')

if __name__ == '__main__':
    server = HTTPServer(('', 8080), Handler)
    print('Serving on 8080...')
    server.serve_forever()
