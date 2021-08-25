import qrcode

# First we make a QRCode which contains a link:
link = qrcode.make("https://www.twitch.tv/blitzkriegboys")
link.save("twitchQR.jpg")

# Second we make a QRCode which contains a text:
text = qrcode.make("This is a QR Code which displays any text coded")
text.save("textQR.jpg")
