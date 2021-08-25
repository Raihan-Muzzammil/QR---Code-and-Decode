import cv2

# OpenCV is a library with a vast number of built in function that are yet to be explored.
# Today I will be sticking with the theme of QRCodes and make a QRCode Decoder.

# We Assign a function to a new variable.
Decode = cv2.QRCodeDetector()

# We create a new variable to display the result of the QR Code.
# Here the underscores are used to avoid unwanted outputs.
Decoded, _, _ = Decode.detectAndDecode(cv2.imread("textQR.jpg"))

# We print the Code.
print("Decoded Text is : ", Decoded)
