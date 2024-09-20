# B站UP主UID
UID = 234504537

import requests  # 用于得到网页链接
import json  # 用于解析JSON格式的库


class API:
    _UID: int
    fans = 0
    like = 0
    view = 0

    def update(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
        }

        try:
            response = requests.get(
                "https://api.bilibili.com/x/relation/stat?vmid=" + str(self._UID),
                headers=headers,
            )
            J_data = json.loads(response.text)
            self.fans = J_data["data"]["follower"]
        except:
            print("粉丝数获取失败")

        response = requests.get(
            "https://api.bilibili.com/x/space/upstat?mid=" + str(self._UID),
            headers=headers,
        )
        J_data = json.loads(response.text)
        print(J_data)

        ## 获取播放量和点赞需要提供cookie，还没找到好方法，暂时屏蔽
        # try:
        #     response = requests.get('https://api.bilibili.com/x/space/upstat?mid=' +str(self._UID),headers=headers)
        #     J_data = json.loads(response.text)
        #     self.view =  J_data['data']['archive']['view']
        #     self.like = J_data['data']['likes']
        # except:
        #     print("播放量获取失败")

    def __init__(self, your_uid: int) -> None:
        self._UID = your_uid
        # self.update()


bilibili = API(UID)
print("粉丝", bilibili.fans)
# print("点赞", bilibili.like )
# print("播放", bilibili.view )
