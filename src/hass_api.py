import requests
import json
import time
from datetime import datetime, timedelta
from urllib.parse import urlencode
from numpy import *

HASS_IP = "127.0.0.1"
HASS_PORT = "8123"
HASS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI3ZTllODM4YTI2OWI0YjNlOWE5NzQ2Nzc2MDc3N2Y2MSIsImlhdCI6MTcyNDkxMTY0OSwiZXhwIjoyMDQwMjcxNjQ5fQ.6h_YU875EEImmW8EeBrTG4b0ASGDU1W5yXyTeJilsZ8"


class HASS_API:
    """
    使用hass的api来读取数据
    """

    _api_prefix: str
    _authorization: str

    def _get(self, endpoint=""):
        headers = {
            "Authorization": "Bearer " + self._authorization,
            "content-type": "application/json",
        }
        response = requests.get(self._api_prefix + endpoint, headers=headers)
        return response.text

    def _get_json(self, endpoint=""):
        return json.loads(self._get(endpoint))

    def is_connect_ok(self) -> bool:
        """
        是否能成功连接
        """
        text = test._get()
        try:
            json.loads(text)
            return True
        except:
            print("ERROR 连接到hass失败 :\n\t", text, "\n")
            return False

    def get_entity_state(self, entity_id: str) -> str:
        """
        返回实体的数值
        @entity_id : 实体标识符
        """
        text = self._get_json("states/" + entity_id)
        if "state" not in text.keys():
            return "-"
        return text["state"]

    def get_entity_hsitory(self, entity_id: str, start_time="", end_time=""):
        """
        返回实体在指定时间段内的数值记录
        @start_time: 格式为 strftime("%Y-%m-%dT%H:%M:%S+08:00")
        @end_time: 格式为 strftime("%Y-%m-%dT%H:%M:%S+08:00")
        """
        history: list
        if start_time != "":
            start_time = "/" + start_time

        para = {"filter_entity_id": entity_id, "end_time": end_time}
        para = urlencode(para)
        history = test._get_json(
            "history/period" + start_time + "?" + para + "&minimal_response"
        )
        return history

    def get_entity_hsitory_mean_in_1min(self, entity_id: str, time: str) -> list:
        """
        返回某一分钟内的均值，仅对数值型的实体有效
        @entity_id: 实体标识符
        @time: 格式同2024-08-29T14:00
        """
        time_start = f"{time}:00+08:00"
        time_end = f"{time}:00+07:59"
        history = self.get_entity_hsitory(
            entity_id,
            start_time=time_start,
            end_time=time_end,
        )
        if history.__len__() == 0:
            return 0
        sum = []
        for message in history[0]:
            try:
                sum.append(float(message["state"]))
            except:
                pass
        return round(mean(sum), 2)

    def get_day_by_1min(self, entity_id: str, day: str) -> list:
        """
        返回指定日期内，每分钟的平均值,仅支持数值类型的实体
        @entity_id: 实体标识符
        @day: 格式为 2024-08-29
        """
        re_list = []
        for hour in range(24):
            for minuter in range(60):
                time_start = "%sT%d:%d" % (day, hour, minuter)
                re_list.append(self.get_entity_hsitory_mean_in_1min(entity_id, time_start))
        return re_list

    def get_yesterday_by_1min(self, entity_id: str) -> list:
        now = datetime.now()
        yesterday_midnight = now - timedelta(days=1)
        formatted_time = yesterday_midnight.strftime("%Y-%m-%d")
        return self.get_day_by_1min(entity_id, formatted_time)

    def __init__(self, token: str, ip="127.0.0.1", port="8123") -> None:
        self._api_prefix = "http://" + ip + ":" + port + "/api/"
        self._authorization = token


class HASS_DATA:
    _HASS_OPT: HASS_API

    def __init__(self, token: str, ip="127.0.0.1", port="8123") -> None:
        self._HASS_OPT = HASS_API(token, ip, port)


test = HASS_API(HASS_TOKEN)
now = datetime.now()
yesterday_midnight = now - timedelta(days=1)
formatted_time = yesterday_midnight.strftime("%Y-%m-%d")
# res = test.get_day_by_1min("sensor.atc_52df_temperature", formatted_time)
res = test.get_yesterday_by_1min("sensor.atc_52df_temperature")
print(res.__len__())

"""
测试计算昨日每分钟均值，

采用for循环发出1440条请求
real    0m36.264s
user    0m17.279s
sys     0m1.530s


"""