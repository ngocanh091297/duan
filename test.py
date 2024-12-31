# Import thư viện

import cv2
import matplotlib.pyplot as plt
import pyautogui
import time 
import os
import numpy as np
import re
import easyocr
reader = easyocr.Reader(['en'])
from singleton_ocr import OCRSingleton

# Lấy đối tượng OCR đã khởi tạo
ocr = OCRSingleton.get_instance()
def rotate_image(image, angle, scale=1.0):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)  # Tọa độ trung tâm của ảnh
    ma_tran_xoay = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, ma_tran_xoay, (w, h))

def process_card_string(card_string):
    # Loại bỏ dấu chấm nếu có
    card_string = re.sub(r'[^A-Za-z0-9]', '', card_string)

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
def timlabai(du_lieu_anh_bai,du_lieu_anh_bai_2,du_lieu_anh_bai_3):

    # du_lieu_anh_bai = pyautogui.screenshot(region=(400, 761,90, 33)) 

    # du_lieu_anh_bai = np.array(du_lieu_anh_bai)
    # du_lieu_anh_bai_3 = pyautogui.screenshot(region=(375, 761,20, 25))   
    # du_lieu_anh_bai_3 = np.array(du_lieu_anh_bai_3)
    # du_lieu_anh_bai_3 = cv2.cvtColor(du_lieu_anh_bai_3, cv2.COLOR_BGR2GRAY)
    # du_lieu_anh_bai_2 = pyautogui.screenshot(region=(310, 761, 67, 36))
    # du_lieu_anh_bai_2 = np.array(du_lieu_anh_bai_2)

    anh_xam = cv2.cvtColor(du_lieu_anh_bai_2, cv2.COLOR_BGR2GRAY)

    # Bước 4: Phóng to ảnh để cải thiện độ phân giải
    rescaled_image = cv2.resize(anh_xam, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

    # Bước 5: Cắt ảnh thành 2 phần (trái và phải)
    h, w = rescaled_image.shape  # h là chiều cao, w là chiều rộng
    left_half = rescaled_image[:, :w // 2]  # Nửa bên trái
    right_half = rescaled_image[:, w // 2:]  # Nửa bên phải

    angle = -14  # Góc xoay
    left_rotated = rotate_image(left_half, angle)
    right_rotated = rotate_image(right_half, -7)

    # Bước 7: Áp dụng threshold
    ret, left_thresh = cv2.threshold(left_rotated, 150, 255, cv2.THRESH_BINARY)
    ret, right_thresh = cv2.threshold(right_rotated, 150, 255, cv2.THRESH_BINARY)
    h_right, w_right = right_thresh.shape  # Lấy chiều cao và rộng của ảnh
    top_70_percent = int(h_right * 0.7)  # Tính 70% chiều cao
    right_thresh_cropped = right_thresh[:top_70_percent, :]  # Giữ lại 70% từ trên xuống


   
    result = ocr.ocr(left_thresh, cls=False)
   
    detected_words = []
    check=False
    # Hiển thị kết quả
    for line in result:
       if line is not None:
            for word_info in line:
                if word_info is not None:
                    card_string = word_info[1][0]
                    processed_cards = process_card_string(card_string)
                    # Thêm từng lá bài vào mảng
                    # print("la trai")
                    detected_words.extend(processed_cards)
                    check=True
    # if check ==False:
    #     result = reader.readtext(left_thresh) 
    #     for (bbox, text, prob) in result:
    #            text
    #            detected_words.extend(text)
    result = ocr.ocr(right_thresh_cropped, cls=False)
   
 
    # Hiển thị kết quả
    for line in result:
       if line is not None:
            for word_info in line:
                if word_info is not None:
                    card_string = word_info[1][0]
                    processed_cards = process_card_string(card_string)
                    # Thêm từng lá bài vào mảng
                    
                    detected_words.extend(processed_cards)   
    rescaled_image = cv2.resize(du_lieu_anh_bai_3, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    ret, thresh = cv2.threshold(rescaled_image, 150, 255, cv2.THRESH_BINARY)   
    # cv2.imwrite('daxoay3.png', thresh)
  
    result = ocr.ocr(thresh, cls=True)
   
    # Hiển thị kết quả
    for line in result:
       if line is not None:
            for word_info in line:
                if word_info is not None:
                    card_string = word_info[1][0]
                  
                    processed_cards = process_card_string(card_string)
                    # Thêm từng lá bài vào mảng
                 
                    detected_words.extend(processed_cards)   
            # xoay bài 1
    (h, w) = du_lieu_anh_bai.shape[:2]

    # Bước 3: Tính toán ma trận xoay
    center = (w // 2, h // 2)  # Tọa độ trung tâm của ảnh
    angle = 17  # Góc xoay
    scale = 1.0  # Tỷ lệ (1.0 là giữ nguyên kích thước)
    # Tạo ma trận xoay
    ma_tran_xoay = cv2.getRotationMatrix2D(center, angle, scale)

    # Bước 4: Áp dụng ma trận xoay
    anh_xoay = cv2.warpAffine(du_lieu_anh_bai, ma_tran_xoay, (w, h))
    anh_xoay_xam = cv2.cvtColor(anh_xoay, cv2.COLOR_BGR2GRAY)

    # Phóng to ảnh để cải thiện độ phân giải
    rescaled_image = cv2.resize(anh_xoay_xam, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    ret, thresh = cv2.threshold(rescaled_image, 150, 255, cv2.THRESH_BINARY)
    # cv2.imwrite('daxoay2.png', thresh)
    h, w = thresh.shape  # h là chiều cao, w là chiều rộng

    # Cắt ảnh thành hai phần theo chiều dọc (trái và phải)
   
    split_point = w * 35 // 100  # 40% chiều rộng

    # Cắt ảnh thành 4 phần bên trái và 6 phần bên phải
    left_half = thresh[:, :split_point]  # Nửa bên trái (4 phần)
    right_half = thresh[:, split_point:]  # Nửa bên phải (6 phần)

    # Lưu ảnh
    # cv2.imwrite('nuatrai2.png', left_half)
    # cv2.imwrite('nuaphai2.png', right_half)
    result = ocr.ocr(left_half, cls=True)
  
    # Hiển thị kết quả
    for line in result:
       if line is not None:
            for word_info in line:
                if word_info is not None:
                    card_string = word_info[1][0]
                    processed_cards = process_card_string(card_string)
                    # Thêm từng lá bài vào mảng
                   
                    detected_words.extend(processed_cards)    
    result = ocr.ocr(right_half, cls=True)
  
    # Hiển thị kết quả
    for line in result:
       if line is not None:
            for word_info in line:
                if word_info is not None:
                    card_string = word_info[1][0]
                    processed_cards = process_card_string(card_string)
                    # Thêm từng lá bài vào mảng
                   
                    detected_words.extend(processed_cards)    
    
    return detected_words
