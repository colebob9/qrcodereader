"""
Batch QR code decoder
colebob9

NEEDS:
pip install pyzbar
pip install image
"""

from pyzbar.pyzbar import decode
from PIL import Image
import os

files = os.listdir(os.getcwd())


decoded_qr_data = ''

data_file = open("data.txt","w")

for file in sorted(files):
        if file.endswith(".png"):
            decoded_qr = decode(Image.open(file))
            #print(decoded_qr)

            decoded_qr_data = str(decoded_qr[0].data)
            print(file + " contains " + decoded_qr_data)
            data_file.write(decoded_qr_data)

data_file.close()