from http.server import HTTPServer,BaseHTTPRequestHandler
import cgi
import qrcode
import socket
from zeroconf import Zeroconf,ServiceInfo
from io import BytesIO
import os
import json

from routes import ROUTES
from helper import HelperFunctions


# create uploads directory if not exists
UPLOAD_DIRS = "uploads"
os.makedirs(UPLOAD_DIRS,exist_ok=True)
class SimpleUpload(BaseHTTPRequestHandler):
    def do_GET(self):
        handler = ROUTES.get(self.path)
        if handler:
            getattr(self,handler)()

        elif self.path.startswith("/download"):
            self.download_file()
        else:
            self.send_error(404)



    def do_POST(self):
        if self.path == "/upload":
            self.handle_upload()
        else:
            self.send_error(404)

    def serve_html(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        
        self.end_headers()

        with open ("share.html","rb") as file:
            self.wfile.write(file.read())

    def handle_upload(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        file_item = form['file']

        if file_item.filename:
            filename = os.path.basename(file_item.filename)
            path = os.path.join(UPLOAD_DIRS, filename)

            with open(path, "wb") as f:
                f.write(file_item.file.read())

        self.send_response(200)
        self.end_headers()

    def list_files(self):
        files = os.listdir(UPLOAD_DIRS)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(files).encode())
    
    
    def download_file(self):
        filename = self.path.split("?file=")[-1]
        path = os.path.join(UPLOAD_DIRS, filename)

        if not os.path.exists(path):
            self.send_error(404)
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/octet-stream")
        self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
        self.end_headers()

        with open(path, "rb") as f:
            self.wfile.write(f.read())


    def serve_qr(self):
        ip = HelperFunctions.find_my_ip()
        url = f"http://{ip}:8000"

        img_bytes = HelperFunctions.generate_qr(url)

        self.send_response(200)
        self.send_header("Content-Type", "image/png")
        self.end_headers()

        self.wfile.write(img_bytes)
