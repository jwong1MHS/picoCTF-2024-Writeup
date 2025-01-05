import cv2

img = cv2.imread('home/ctf-player/drop-in/flag.png')
detector = cv2.QRCodeDetector()
data, _, _ = detector.detectAndDecode(img)
print(data)

# Flag: picoCTF{p33k_@_b00_d4ca652e}
