import pyqrcode
from pyqrcode import QRCode
s="https://www.linkedin.com/in/jagadeesh-rallabandi/"
url=pyqrcode.create(s)
url.svg("mylinkedin.svg",scale=8)