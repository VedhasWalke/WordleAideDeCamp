import cv2
import pytesseract

img = cv2.imread('wordle.png')
edges = cv2.Canny(image=img, threshold1=100, threshold2=200)
cv2.imshow('Cany',edges)
cv2.waitKey(0)
text = pytesseract.image_to_string(edges)
print(text)