# Import thư viện

import cv2
import matplotlib.pyplot as plt
import pyautogui
import time 
import os
import numpy as np
import re

from singleton_ocr import OCRSingleton

# Lấy đối tượng OCR đã khởi tạo
ocr = OCRSingleton.get_instance()


def process_card_string(card_string):
    # Loại bỏ dấu chấm nếu có
    card_string = re.sub(r'[^AKQJakqj0-9]', '', card_string)


    # Tạo danh sách kết quả
    cards = []

    # Xử lý từng ký tự hoặc nhóm ký tự
    i = 0
    while i < len(card_string):
        if card_string[i] == '1' and i + 1 < len(card_string) and card_string[i+1] == '0':
            # Nếu phát hiện '10', thì thêm '10' vào mảng và bỏ qua ký tự tiếp theo
            cards.append('10')
            i += 2
        else:
            # Thêm các ký tự riêng lẻ (A, 2-9, J, Q, K)
            cards.append(card_string[i])
            i += 1

    return cards

def timlabai_club():
# 188 40 230 62
    du_lieu_anh_bai_2 = pyautogui.screenshot(region=(188, 40, 42, 23))
    du_lieu_anh_bai_2 = np.array(du_lieu_anh_bai_2)

    anh_xam = cv2.cvtColor(du_lieu_anh_bai_2, cv2.COLOR_BGR2GRAY)

    rescaled_image = cv2.resize(anh_xam, None, fx=6, fy=6, interpolation=cv2.INTER_CUBIC)

    ret, right_thresh = cv2.threshold(rescaled_image, 150, 255, cv2.THRESH_BINARY)
  
    result = ocr.ocr(right_thresh, cls=False)
   
    detected_words = []
    # Hiển thị kết quả
    for line in result:
       if line is not None:
            for word_info in line:
                if word_info is not None:
                    card_string = word_info[1][0]
                    processed_cards = process_card_string(card_string)
                    # Thêm từng lá bài vào mảng
                    if processed_cards!="":
                       
                        detected_words.extend(processed_cards) 
                         
               
    return detected_words
