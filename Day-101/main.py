#QR CODE GENARATOR
import qrcode
image = qrcode.make("https://github.com/NiamulAnkon/365-Days-of-python-code")
image.save("ankon_github.png")
