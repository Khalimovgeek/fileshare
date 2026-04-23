from http.server import HTTPServer
import os

from crud import SimpleUpload
from helper import HelperFunctions


if __name__ == "__main__":
    ip = HelperFunctions.find_my_ip()
    
    print(f"Open on phone: http://{ip}:8000")

    HTTPServer(("0.0.0.0", 8000), SimpleUpload).serve_forever()