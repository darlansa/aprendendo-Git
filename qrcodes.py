import png
from pyqrcode import QRCode
import pyqrcode

s = input('Digite a senha do wifi : ')

url = pyqrcode.create(s)
url.png("QRCODE.png",scale=6)