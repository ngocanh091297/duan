import cv2
import numpy as np
import time 
import pyautogui
import pytesseract
import easyocr
reader = easyocr.Reader(['en'])
from singleton_ocr import OCRSingleton

# # Lấy đối tượng OCR đã khởi tạo
ocr = OCRSingleton.get_instance()
def timtext():
    image =  cv2.imread('image/t6.png')
    anh_xam = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rescaled_image = cv2.resize(anh_xam, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    result = ocr.ocr(rescaled_image, cls=False)
    detected_words = ""
    # Hiển thị kết quả
    for line in result:
       if line is not None:
            for word_info in line:
                if word_info is not None:
                    card_string = word_info[1][0]
                   
                    # Thêm từng lá bài vào mảng
                    detected_words =detected_words+card_string
            # xoay bài 1
    
    print(detected_words)
timtext()