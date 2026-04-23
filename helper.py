from http.server import HTTPServer,BaseHTTPRequestHandler
import cgi
import qrcode
import socket
from zeroconf import Zeroconf,ServiceInfo
from io import BytesIO
from server_script import SimpleUpload

class HelperFunctions:
        
        def __init__(self, appname):
            self.url = f"http:{appname}.local:8000/"
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
