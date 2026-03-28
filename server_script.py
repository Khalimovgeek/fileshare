from http.server import HTTPServer,BaseHTTPRequestHandler
import cgi
import qrcode
import socket
from zeroconf import Zeroconf,ServiceInfo
class SimpleUpload(BaseHTTPRequestHandler,HelperFunctions):
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

        # send response to frontend
        self.send_response(200)
        self.end_headers()

    def get_QR(self):
        qr = HelperFunctions.generate_qr()
        
        self.send_response(201)
    

    def calculate_speed():
        pass

    def calculate_progress():
        pass





class HelperFunctions():
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
        # generate qr
        def generate_qr(self):
            qr = qrcode.make(self.url)
            return qr
        
        # find mac adress / ip adress 
        
        def find_my_ip():
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

            try:
                s.connect(("8.8.8.8",80))
                return s.getsockname()[0]
            finally:
                s.close()

        ip = socket.inet_aton(find_my_ip())









    
    
    
if __name__ == "main":

    HTTPServer(("0.0.0.0", 8000), SimpleUpload).serve_forever()