import cv2
import numpy as np
import time 
import pyautogui
import pytesseract
# import easyocr
# reader = easyocr.Reader(['en'])
from singleton_ocr import OCRSingleton

# # Lấy đối tượng OCR đã khởi tạo
ocr = OCRSingleton.get_instance()
# Đọc ảnh
# image = cv2.imread('thumau1.png')

# Chia ảnh thành 5 vùng chứa từng lá bài
# height, width, _ = image.shape
# card_width = width // 5  # Giả sử luôn có 5 lá bài
# cards = [image[:, i*card_width:(i+1)*card_width] for i in range(5)]

# Chuyển ảnh sang không gian màu HSV
def detect_suit(card):
    hsv_image = cv2.cvtColor(card, cv2.COLOR_BGR2HSV)
    
    # Định nghĩa dải màu cho từng chất bài (trong HSV)
    # Màu xanh dương cho chất rô
    # lower_blue = np.array([105, 180, 100])  # Giới hạn thấp hơn
    # upper_blue = np.array([125, 255, 255])  # Giới hạn cao hơn
    lower_blue = np.array([100, 150, 80])  # Hue thấp hơn
    upper_blue = np.array([130, 255, 255])  # Hue cao hơn

    # Màu đỏ cho chất cơ
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    

    # Màu xanh lá cho chất tép
    lower_green = np.array([40, 100, 50])
    upper_green = np.array([80, 255, 255])

    # Màu đen cho chất bích (xấp xỉ bằng độ bão hòa và giá trị thấp)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])

    # Tạo mặt nạ cho từng chất bài
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    mask_red1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    mask_red = mask_red1 | mask_red2
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
    mask_black = cv2.inRange(hsv_image, lower_black, upper_black)

    # Kiểm tra mặt nạ nào có nhiều pixel nhất (để xác định chất)
    blue_count = cv2.countNonZero(mask_blue)
    red_count = cv2.countNonZero(mask_red)
    green_count = cv2.countNonZero(mask_green)
    black_count = cv2.countNonZero(mask_black)
    
    # Lưu kết quả vào dictionary để dễ so sánh
    counts = {
        "h": blue_count,
        "d": red_count,   # cơ  nhung thành rô
        "c": green_count,
        "s": black_count
    }

    # Kiểm tra giá trị cao nhất và lớn hơn 10
    max_suit = max(counts, key=counts.get)
    if counts[max_suit] > 0:
        # print(counts[max_suit])
        return max_suit
    else:
        # print(counts[max_suit])
        return "none"

# Phát hiện chất bài cho từng lá

# In ra thứ tự các chất



def xacdinhchatbai_nhl():
        # image = cv2.imread('mau2.png')
    # du_lieu_anh_bai =  pyautogui.screenshot(region=(338, 772,80, 25))     #   pyautogui.screenshot(region=(305, 761,180, 65))        
    # image = np.array(du_lieu_anh_bai)
    image = pyautogui.screenshot(region=(188, 40, 42, 23))
    image = np.array(image)
    height, width, _ = image.shape
    card_width = width // 2  # Giả sử luôn có 5 lá bài
    cards = [image[:, i*card_width:(i+1)*card_width] for i in range(2)]
    # for i, card in enumerate(cards):
    #     filename = f'anh{i+1}.png'  # Đặt tên file tương ứng với từng lá bài
    #     cv2.imwrite(filename, card)  # Lưu ảnh
    
    suits = [detect_suit(card) for card in cards]
    print(suits)
    return suits
