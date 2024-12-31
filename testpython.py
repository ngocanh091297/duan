import tkinter as tk
import pyautogui
from PIL import Image
import keyboard
import cv2
import numpy as np
# Hàm test sẽ được chạy khi nhấn nút
import time 

threshold = 0.8  # Ngưỡng khớp, giá trị từ 0 đến 1
loi = True
all_in_cac_vong_sau=False
chuyen_ban_thanh_cong=False
hanhdong_status=True
def chupanhmanhinh():
      screenshot = pyautogui.screenshot()
# Bước 2: Chuyển đổi ảnh chụp màn hình từ định dạng PIL sang định dạng mà OpenCV có thể xử lý
      screenshot = np.array(screenshot)
      screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
      return screenshot

def exit_program():
    print("ESC được nhấn! Thoát chương trình.")
    global loi
    loi =False  # Dừng chương trình ngay lập tức
keyboard.add_hotkey('p', exit_program)
# keyboard.add_hotkey('f', fold_bai)
# keyboard.add_hotkey('c', call)
def auto():
      global hanhdong_status
      hanhdong_status=True
def tuchoi():
      global hanhdong_status
      hanhdong_status=False
keyboard.add_hotkey('a', auto)
keyboard.add_hotkey('t',tuchoi )


def test():
   
    stack="20 bb"
     

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Start Button Example")
root.geometry("300x700")
# 
# Tạo nhãn và trường nhập liệu
label2 = tk.Label(root, text="Nhập một số:")
label2.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)
# Tạo nút Start và gán nó với hàm test
start_button = tk.Button(root, text="Start", command=test)
start_button.pack(pady=20)
label = tk.Label(root, text="")
label.pack(pady=10)
label.config(text="test thung")
# Chạy giao diện chính
root.mainloop()
