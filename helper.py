import qrcode
import socket
from io import BytesIO

class HelperFunctions:
        
        def __init__(self):
            self.ip = self.find_my_ip()
        
        
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
