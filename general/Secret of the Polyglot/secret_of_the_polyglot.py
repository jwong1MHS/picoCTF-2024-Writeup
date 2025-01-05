import cv2
import pdfplumber
import pytesseract  # Make sure to install tesseract-ocr

# # PDF
with pdfplumber.open("flag2of2-final.pdf") as pdf:
    first_page = pdf.pages[0]  # Access the first page
    second_flag = first_page.extract_text()

# PNG
image = cv2.imread("flag2of2-final.pdf")
resized_image = cv2.resize(image, (100, 100))
text = pytesseract.image_to_string(resized_image)
first_flag = ''.join(text.splitlines())

print(first_flag + second_flag)

# Flag: picoCTF{f1u3n7_1n_pn9_&_pdf_2a6a1ea8}
