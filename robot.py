#__author:ayjin
#__Date:2020-12-23
#__Orginazation:JLUZH
#__Topic:
# 导入相关库
import requests
import time
import string
import random
import urllib
import hashlib


def Tencent_AI_Chat_Robot(msg):
    APPID = "2161028679"  # 这里填刚刚记录的APPID
    APPKEY = "hNLjDw4GkyOYEbcI"  # 这里填刚刚记录的APPKEY
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"  # API地址

    # 构造请求参数
    params = {

        "app_id": APPID,
        # 时间戳（从1970.01.01 08:00到现在经历了多少秒）
        "time_stamp": str(int(time.time())),
        # 随机字符串，这里从26个英文字母+10个数字中随机抽16个（可重复，小写）组成
        "nonce_str": "".join(random.choice(string.ascii_letters + string.digits) for x in range(16)),
        # 会话标识（默认“10000”，应用内唯一）
        "session": "10000".encode("utf-8"),
        # 我方发言
        "question": msg.encode("utf-8")
    }

    # 签名信息，生成规则见文档接口鉴权部分
    sign_before = ""

    # 生成签名
    # 将<key, value>请求参数对按key进行字典升序排序，得到有序的参数对列表N
    for key in sorted(params):
        # 将列表N中的参数对按URL键值对的格式拼接成字符串，得到字符串T（如：key1=value1&key2=value2）
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写
        sign_before += "{}={}&".format(key, urllib.parse.quote(params[key], safe=""))

    # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾
    sign_before += "app_key={}".format(APPKEY)

    # 对字符串sign_before进行MD5运算，并转换成16进制大写格式，得到接口请求签名
    sign = hashlib.md5(sign_before.encode("UTF-8")).hexdigest().upper()
    # print(sign)
    # 将签名追加到请求参数
    params["sign"] = sign

    # print(params)
    # 调用API（url是API地址，data是请求参数），并返回数据（JSON格式）
    html = requests.post(url, data=params).json()
    # print(html)
    # 提取API返回信息中的回答语句
    return html["data"]["answer"]




if __name__ == '__main__':
    rs = Tencent_AI_Chat_Robot('你好')
    print(rs)
