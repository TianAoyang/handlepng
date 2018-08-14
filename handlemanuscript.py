from skimage import io
from pyzbar.pyzbar import decode


class FindQRCode:
    def findqrcode(path, type = 0):
        img = io.imread(path)
        decodedata = decode(img)
        return decodedata
