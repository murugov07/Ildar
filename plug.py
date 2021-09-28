from http.server import HTTPServer, BaseHTTPRequestHandler
import sys


class PlugServer(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        post = post_body.decode('utf-8')
        print(post)
        self.wfile.write(b"Hello world")


if __name__ == "__main__":
    port = sys.argv[1:]
    httpd = HTTPServer((port[0], int(port[1])), PlugServer)
    print("Сервер запущен на ip:", port[0], "на порту:", port[1])
    httpd.serve_forever()
