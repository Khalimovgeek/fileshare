from http.server import HTTPServer,BaseHTTPRequestHandler
import cgi

class SimpleUpload(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("share.html","rb") as f:
            self.wfile.write(f.read())

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        file_item = form['file']

        if file_item.filename:
            with open(file_item.filename, "wb") as f:
                f.write(file_item.file.read())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Upload successful")

HTTPServer(("0.0.0.0", 8000), SimpleUpload).serve_forever()