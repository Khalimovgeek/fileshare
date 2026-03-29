from http.server import HTTPServer,BaseHTTPRequestHandler
import cgi
import qrcode
import socket
from zeroconf import Zeroconf,ServiceInfo
from io import BytesIO
import os
import json


# create directory if not exists
UPLOAD_DIRS = "uploads"
os.makedirs(UPLOAD_DIRS,exist_ok=True)

# Routes

ROUTES =  {
    "/": "serve_html",
    "/qr": "serve_qr",
    "/files": "list_files", 
}



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


    def calculate_speed():
        pass

    def calculate_progress():
        pass





class HelperFunctions:
        def __init__(self):
            self.url = "http://sharenet.local:8000/"
            self.ip = self.find_my_ip()
            self.info = ServiceInfo(
                "_http._tcp.local.",
                "ShareNet._http._tcp.local.",
                addresses=[self.ip],
                port=8000,
                server="sharenet.local."
            )
        
        
        # find mac adress / ip adress 
        @staticmethod
        def find_my_ip():
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

            try:
                s.connect(("8.8.8.8",80))
                return s.getsockname()[0]
            finally:
                s.close()

        # generate qr
        @staticmethod
        def generate_qr(url):
            qr = qrcode.make(url)
            buffer = BytesIO()
            qr.save(buffer,format="PNG")
            return buffer.getvalue()
        
        ip = socket.inet_aton(find_my_ip())









    
    
    
if __name__ == "__main__":
    ip = HelperFunctions.find_my_ip()
    
    print(f"Open on phone: http://{ip}:8000")

    HTTPServer(("0.0.0.0", 8000), SimpleUpload).serve_forever()