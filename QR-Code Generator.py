# Import QRCode from pyqrcode Library 
import pyqrcode 
from pyqrcode import QRCode 
  
  
# Link Variable used to store the link of your website,document,portfolio
Link = "Enter Your desired Link or Website Hear"
  
# Generate QR code 
url = pyqrcode.create(Link) 
  
# Create and save the png file naming "Qr-Code.png" 
url.svg("Qr-Code.svg", scale = 8) 
