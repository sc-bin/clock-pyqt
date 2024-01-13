# B站UP主UID
UID = 234504537


# 把cookie存放到cookie.txt内
f=open('cookie.txt','r')
cookies={}
for line in f.read().split(';'):   #按照字符：进行划分读取
    #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split('=',1)
    cookies[name]=value  #为字典cookies添加内容



import requests                 # 用于得到网页链接
import json                     # 用于解析JSON格式的库 


class API():
    _UID:int
    fans:int
    like:int
    view:int
    def update(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}

        try:
            response = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' +str(self._UID), headers=headers)
            J_data = json.loads(response.text)
            self.fans = J_data['data']['follower']
        except:
            print("粉丝数获取失败")

        try:
            response = requests.get('https://api.bilibili.com/x/space/upstat?mid=' +str(self._UID),headers=headers, cookies=cookies)
            J_data = json.loads(response.text)
            self.view =  J_data['data']['archive']['view']
            self.like = J_data['data']['likes']
        except:
            print("播放量获取失败")


        # 成功得到网页
    def __init__(self, your_uid:int) -> None:
        self._UID = your_uid
        self.update()

def get_fans(UID:int):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    if UID == None:
        print("未输入姓名，请重新运行")
        return
    try:
        response = requests.get('https://api.bilibili.com/x/space/upstat?mid=' +str(UID),headers=headers, cookies=cookies)
        # response = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' +str(UID), headers=headers, cookies=MY_COOKIE)
    # 网络连接失败
    except:
        print("网络连接失败")
    # 成功得到网页
    else:
        J_data = json.loads(response.text)
        print(response.text)
        # print(J_data)
        # print(J_data['data'])
        # print(J_data['data']['follower'])
bili=API(UID)
print("粉丝", bili.fans )
print("点赞", bili.like )
print("播放", bili.view )