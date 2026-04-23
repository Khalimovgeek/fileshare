from http.server import HTTPServer
import os

from crud import SimpleUpload
from helper import HelperFunctions

# create uploads directory if not exists
UPLOAD_DIRS = "uploads"
os.makedirs(UPLOAD_DIRS,exist_ok=True)

if __name__ == "__main__":
    ip = HelperFunctions.find_my_ip()
    
    print(f"Open on phone: http://{ip}:8000")
    helpers = HelperFunctions("sharenet")
    print("Registering service...")
    print(f"Service URL: {helpers.url}")

    HTTPServer(("0.0.0.0", 8000), SimpleUpload).serve_forever()