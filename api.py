import requests

# URL của API bạn muốn gọi
url = 'http://localhost:2021/client/poker_tinhtoan/preflop2'
url_type2 = 'http://localhost:2021/client/poker_tinhtoan/quet2'
url_nhl = 'http://206.189.93.164:2021/client/poker_tinhtoan_nhl_game/preflop2'

def callapi(bai,chat,chat_board,action ): #
   # Dữ liệu bạn muốn gửi đi (nếu cần)
    data = {
        'bai': bai,
        'chat':chat,
        "chat_board":chat_board,
        action:action
      
    }
    
    # Headers (nếu API yêu cầu)
    headers = {
        'Content-Type': 'application/json',
        # 'Authorization': 'Beare'  # Nếu cần token
    }

    # Gửi yêu cầu POST
    response = requests.post(url, json=data, headers=headers)
    print(response)
    # Kiểm tra status code
    if response.status_code == 200:
        data =response.json()  # Xử lý kết quả nếu cần4
        print(data)
        return  data['data']
    else:
        return "errrr"
# callapi()
def callapi_nhl(bai,chat,chat_board,action,pot_hien_tai ,action_text ,songcon ,stack):
    data = {
        'bai': bai,
        'chat':chat,
        "chat_board":chat_board,
        "action":action,
        "pot":pot_hien_tai,
        "action_text":action_text,
        "songcon":songcon,
        "stack":stack
      
    }
    
    # Headers (nếu API yêu cầu)
    headers = {
        'Content-Type': 'application/json',
        # 'Authorization': 'Beare'  # Nếu cần token
    }

    # Gửi yêu cầu POST
    response = requests.post(url_nhl, json=data, headers=headers)
  
    # Kiểm tra status code
    if response.status_code == 200:
        data =response.json()  # Xử lý kết quả nếu cần4
        print(data)
        return  data['action_res']
    else:
        return "errrr"
def callapi_type2(list_la_bai,list_bai_2 ,chatlabai_1,chatlabai_2,chatlabai_board):
  
    data = {
        'list_la_bai': list_la_bai,
        'list_bai_2':list_bai_2,
        "chatlabai_1":chatlabai_1,
        "chatlabai_2":chatlabai_2,
        "chatlabai_board":chatlabai_board
      
    }
    
    # Headers (nếu API yêu cầu)
    headers = {
        'Content-Type': 'application/json',
        # 'Authorization': 'Beare'  # Nếu cần token
    }

    # Gửi yêu cầu POST
    response = requests.post(url_type2, json=data, headers=headers)
  
    # Kiểm tra status code
    if response.status_code == 200:
        data =response.json()  # Xử lý kết quả nếu cần4
        print(data['action_res'],data['data'])
        return  data['action_res']
    else:
        return "errrr"