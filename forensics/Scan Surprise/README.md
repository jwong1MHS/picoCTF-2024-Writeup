## Solution

Scan the QR code found at `home/ctf-player/drop-in/flag.png`.

**Flag: `picoCTF{p33k_@_b00_d4ca652e}`**

## Code

```python
import cv2

img = cv2.imread('home/ctf-player/drop-in/flag.png')
detector = cv2.QRCodeDetector()
data, _, _ = detector.detectAndDecode(img)
print(data)
```
