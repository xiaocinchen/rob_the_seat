'''
Author: SpadeXiao
Date: 2021-09-02 20:37:05
LastEditTime: 2021-09-02 21:36:29
'''
import requests
import json
url = "https://wechat.v2.traceint.com/index.php/graphql/"
headers = {
    "Host": "wechat.v2.traceint.com",
    "Content-Type": "application/json",
    "Origin": "https://web.traceint.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "SERVERID=e3fa93b0fb9e2e6d4f53273540d4e924|1630589209|1630585515; Hm_lpvt_7ecd21a13263a714793f376c18038a87=1630589201; Hm_lvt_7ecd21a13263a714793f376c18038a87=1630585517; v=5.5; wechatSESS_ID=8aec7f38abecf3f02b977187b447f07f759202d4894a729c; FROM_TYPE=weixin; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjI0NTMyNTUxLCJzY2hJZCI6OTMsImV4cGlyZUF0IjoxNjMwNTkyNjM4fQ.pWZh97VqD60zZEa6w8Bz0TuFJjd0-5tVvj7L6BLyGYugSd7rTyxA_p15M6-3JDT1uHZz07qR8uOgqGHtPK1cDDDrW_vGe8k8uRESflgOEyo0vX7v23g_nmREto-PC2gfmWWXLeNT5LCVQoLPz0b822ecD43V6gsG1QLQbO98GQPQMg13zxTAA8WmTAgK_E_Le-kVyNpO5rSwy0UV14Zd0tseBUz8wd0Veo9Uysd34BRRpUvmylAKr0702sGnLdzWcZL5ejlsnvHkO4E30g7g4l1bjhYqWROCndmNYEBpd_yfJ7GMvN-H_fmvCiEd7GFio3BDbynjIKKWa42IQRS68w",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.12(0x18000c27) NetType/WIFI Language/zh_CN",
    "Referer": "https://web.traceint.com/web/index.html",
    "Accept-Language": "zh-cn"
}

params = {
    "query": "mutation reserveSeat($libId: Int!, $seatKey: String!, $captchaCode: String, $captcha: String!) { userAuth { reserve { reserveSeat( libId: $libId seatKey: $seatKey captchaCode: $captchaCode captcha: $captcha ) } }}",
    "variables": {
        "captchaCode": "",
        "seatKey": "5,37",
        "captcha": "",
        "libId": 324
    },
    "operationName": "reserveSeat"
}
data = json.dumps(params)

res = requests.post(url,headers=headers,data=data)
print(res.text)