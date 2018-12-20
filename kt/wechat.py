import requests
import itchat
from threading import Timer


def get_news():
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation


# 发送消息
def send_news():
    global mylover
    try:
        itchat.auto_login()  # 会弹出网页二维码，扫描即可，登入你的微信账号，True保持登入状态
        my_girfriend = itchat.search_friends(name='李兰兰')  # name改成你微信的备注
        mylover = my_girfriend[0]["UserName"]
        message1 = str(get_news()[0])  # 获取金山字典的内容
        content = str(get_news()[1][17:])
        message2 = str(content)
        message3 = "来自你最爱的人\n测试代码001"
        itchat.send(message1, toUserName=mylover)
        itchat.send(message2, toUserName=mylover)
        itchat.send(message3, toUserName=mylover)
        Timer(1, send_news).start()  # 每隔86400秒发送一次，也就是每天发一次
    except:
        message4 = "最爱你的人出现啦~~\n测试代码002"
        itchat.send(message4, toUserName=mylover)


if __name__ == "__main__":
    send_news()
