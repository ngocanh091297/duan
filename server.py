import tkinter as tk
import pyautogui
from PIL import Image
import keyboard
import cv2
import numpy as np
# Hàm test sẽ được chạy khi nhấn nút
import time 

# from api import callapi_nhl 
from timbainhl import timlabai_club
from testtimmau  import xacdinhchatbai_nhl 
# import logging
# logging.getLogger('ppocr').setLevel(logging.ERROR)
# logging.getLogger('paddle').setLevel(logging.ERROR)
template_cb = cv2.imread('image/toiluot.png')
template_cb = cv2.cvtColor(template_cb, cv2.COLOR_BGR2GRAY)
template_fold =cv2.imread('image/fold.png')
template_fold = cv2.cvtColor(template_fold, cv2.COLOR_BGR2GRAY)
template_allin =cv2.imread('image/all.png')
template_allin = cv2.cvtColor(template_allin, cv2.COLOR_BGR2GRAY)
template_vitri_sb =cv2.imread('image/sb.png')
template_vitri_sb = cv2.cvtColor(template_vitri_sb, cv2.COLOR_BGR2GRAY)
template_vitri_bb =cv2.imread('image/bb.png')
template_vitri_bb = cv2.cvtColor(template_vitri_bb, cv2.COLOR_BGR2GRAY)
template_vitri_btn =cv2.imread('image/btn.png')
template_vitri_btn = cv2.cvtColor(template_vitri_btn, cv2.COLOR_BGR2GRAY)

template_game = cv2.imread('image/game.png')
template_game = cv2.cvtColor(template_game, cv2.COLOR_BGR2GRAY)
threshold = 0.8  # Ngưỡng khớp, giá trị từ 0 đến 1
loi = True
all_in_cac_vong_sau=False
chuyen_ban_thanh_cong=False
hanhdong_status=True
def chupanhmanhinh():
      screenshot = pyautogui.screenshot(region=(0, 0, 550, 950))
# Bước 2: Chuyển đổi ảnh chụp màn hình từ định dạng PIL sang định dạng mà OpenCV có thể xử lý
      screenshot = np.array(screenshot)
      screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
      return screenshot



    #  print("songuoicon_lai ",songuoicon_lai)
def exit_program():
    print("ESC được nhấn! Thoát chương trình.")
    global loi
    loi =False  # Dừng chương trình ngay lập tức
keyboard.add_hotkey('p', exit_program)
# keyboard.add_hotkey('f', fold_bai)
# keyboard.add_hotkey('c', call)
def chupanhkhuvuc_player(x1,y1,x2,y2):
     screenshot = pyautogui.screenshot(region=(x1,y1,x2,y2)) 
     screenshot = np.array(screenshot)
     screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
     result2 = cv2.matchTemplate(screenshot, template_game, cv2.TM_CCOEFF_NORMED)
     locations2 = np.where(result2 >= 0.6)
     if len(locations2[0]) > 0: 
        
          check_all = cv2.matchTemplate(screenshot, template_allin, cv2.TM_CCOEFF_NORMED)
          locations3 = np.where(check_all >= 0.7)
          if len(locations3[0]) > 0:
               return 3
        #    
                
          return  1
     
     else:     
        #  0 là ko tham gia
        #  1 là có tham gia nhưng chưa action
        #  2 là đã chọn fold
        #  3 là đã chọn all
         check_fold = cv2.matchTemplate(screenshot, template_fold, cv2.TM_CCOEFF_NORMED)
         locations1 = np.where(check_fold >= 0.7)
         
         if len(locations1[0]) > 0:
             #  check_status =0 là chưa hành động . check_status = 1 là đã fold  check_status =2 là đã all in
                 return 2
         return 0 
def test2():
    check1 = chupanhkhuvuc_player(384,462,544,609)
    print(check1)
    check2 = chupanhkhuvuc_player(384,462,544,609)
    print(check2)
    check3 = chupanhkhuvuc_player(384,462,544,609)
    print(check3)
    labai =timlabai_club()
    print(labai)
    chatbai = xacdinhchatbai_nhl()
    print(chatbai)
def test():
   
    stack="20 bb"
    
    du_lieu_stack = cv2.imread('anhstack.png')
    du_lieu_stack = cv2.cvtColor(du_lieu_stack, cv2.COLOR_BGR2GRAY)
    du_lieu_board = cv2.imread('baiboarrd.png')
    du_lieu_board = cv2.cvtColor(du_lieu_board, cv2.COLOR_BGR2GRAY)
  
   
    list_la_bai =[]
    list_bai_board=[]
    chatlabai_board=[]
    chatlabai=[]
    print("bat dau.")
    kiemtra_la_bai=True
    du_lieu_anh_bai=cv2.imread('t5.png') 
    du_lieu_anh_bai = cv2.cvtColor(du_lieu_anh_bai, cv2.COLOR_BGR2GRAY)
    global loi ,all_in_cac_vong_sau
    loi=True
    
    while loi:
        start_time = time.time()
      
        screenshot = chupanhmanhinh()   
        result2 = cv2.matchTemplate(screenshot, template_cb, cv2.TM_CCOEFF_NORMED)
        locations2 = np.where(result2 >= threshold)
        
        if len(locations2[0]) > 0:  
        #    đến lượt mình đánh
         
            end_time = time.time()
            elapsed_time = end_time - start_time
# 188 40 230 62
            print(f"hanh dong2 : {elapsed_time:.4f} giây")  

            time.sleep(4)
            continue
      
        time.sleep(2.5)      
    print("out cu")   

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
start_button = tk.Button(root, text="Start", command=test2)
start_button.pack(pady=20)
label = tk.Label(root, text="")
label.pack(pady=10)
label.config(text="test thung")
# Chạy giao diện chính
root.mainloop()
