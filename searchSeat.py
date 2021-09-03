'''
Author: SpadeXiao
Date: 2021-09-02 21:14:02
LastEditTime: 2021-09-03 10:05:00
'''
import requests
import json

cookie = input("请输入你的cookie：\n")
url = "https://wechat.v2.traceint.com/index.php/graphql/"

search_params = {
    "query": "query libLayout($libId: Int, $libType: Int) {\n userAuth {\n reserve {\n libs(libType: $libType, libId: $libId) {\n lib_id\n is_open\n lib_floor\n lib_name\n lib_type\n lib_layout {\n seats_total\n seats_booking\n seats_used\n max_x\n max_y\n seats {\n x\n y\n key\n type\n name\n seat_status\n status\n }\n }\n }\n }\n }\n}",
    "variables": {
        "libId": 324    #A区为323
    },
    "operationName": "libLayout"
}

headers = {
    "Host": "wechat.v2.traceint.com",
    "Content-Type": "application/json",
    "Origin": "https://web.traceint.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": cookie,
    "Connection": "keep-alive",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.12(0x18000c27) NetType/WIFI Language/zh_CN",
    "Referer": "https://web.traceint.com/web/index.html",
    "Accept-Language": "zh-cn"
}

search_data = json.dumps(search_params)

available_seat, flag = [], 1
while(len(available_seat) == 0 and flag > 0):
    print("第%d次开始"%flag,end = '\r')
    res = requests.get(url,headers=headers,data=search_data)
    # print(res.text)
    if "html" in res.text:
        print('网络拥堵。次数为%d'%flag)
    else:
        res = res.json()
        seat_list = res['data']['userAuth']['reserve']['libs'][0]['lib_layout']['seats']
        for seat in seat_list:
            if seat.get('seat_status') == 1:
                available_seat.append(seat.get('key'))
                flag = -1
    flag += 1

print("可供选择的座位有：",available_seat)

for seat in available_seat:
    reserve_params = {
        "query": "mutation reserveSeat($libId: Int!, $seatKey: String!, $captchaCode: String, $captcha: String!) { userAuth { reserve { reserveSeat( libId: $libId seatKey: $seatKey captchaCode: $captchaCode captcha: $captcha ) } }}",
        "variables": {
            "captchaCode": "",
            "seatKey": seat,
            "captcha": "",
            "libId": 324    #A区为323
        },
        "operationName": "reserveSeat"
    }
    reserve_data = json.dumps(reserve_params)
    res = requests.post(url,headers=headers,data=reserve_data).json()
    if res.get('errors'):
        print('抢座失败！将再次尝试！错误内容:',res.get('errors')[0].get('msg'))
    else:
        print('抢座成功！请及时查看！')
        break
    # print(flag)

