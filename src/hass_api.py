import requests
import json
import time
from datetime import datetime, timedelta
from urllib.parse import urlencode
from numpy import *


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

    def get_state(self, entity_id: str) -> str:
        """
        返回实体的数值
        @entity_id : 实体标识符
        """
        text = self._get_json("states/" + entity_id)
        if "state" not in text.keys():
            return "-"
        return text["state"]

    def get_hsitory(self, entity_id: str, start_time="", end_time=""):
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
        history = self._get_json(
            "history/period" + start_time + "?" + para + "&minimal_response"
        )
        return history

    def get_hsitory_in_1min(self, entity_id: str, time: str) -> list:
        """
        返回某一分钟内的均值，仅对数值型的实体有效
        @entity_id: 实体标识符
        @time: 格式同2024-08-29T14:00
        """
        time_start = f"{time}:00+08:00"
        time_end = f"{time}:00+07:59"
        history = self.get_hsitory(
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

    def _get_hsitory_one_day_all_minuter(self, entity_id: str, day: str) -> list:
        """
        返回指定日期内，每分钟的平均值,仅支持数值类型的实体
        @entity_id: 实体标识符
        @day: 格式为 2024-08-29
        """

        def convert_to_east_eight(utc_dt_str):
            without_microseconds = utc_dt_str.split(".")[0]
            without_tz = without_microseconds.replace("+00:00", "")
            last_changed_utc = datetime.fromisoformat(without_tz)
            return last_changed_utc + timedelta(hours=8)

        time_start = f"{day}T00:00+08:00"
        time_end = f"{day}T23:59+07:59"
        history = self.get_hsitory(entity_id, time_start, time_end)

        data = [[] for _ in range(24 * 60)]
        for item in history[0]:
            state = item["state"]
            timestamp = item["last_changed"]
            timestamp_east_eight = convert_to_east_eight(timestamp)  # 转换为东8区时间
            minute_of_day = timestamp_east_eight.hour * 60 + timestamp_east_eight.minute
            try:
                data[minute_of_day].append(float(state))
            except:
                pass
        data_average = []
        for i in data:
            if i.__len__() > 0:
                data_average.append(average(i))
            else:
                data_average.append(0)

        return data_average

    def get_hsitory_yesterday(self, entity_id: str) -> list:
        """
        返回一个列表，对应昨天一天每分钟的平均值,仅支持数值类型的实体
        @entity_id: 实体标识符
        """
        now = datetime.now()
        yesterday_midnight = now - timedelta(days=1)
        formatted_time = yesterday_midnight.strftime("%Y-%m-%d")
        return self._get_hsitory_one_day_all_minuter(entity_id, formatted_time)
    def get_hsitory_today(self, entity_id: str) -> list:
        """
        返回一个列表，对应今天一天每分钟的平均值,仅支持数值类型的实体
        @entity_id: 实体标识符
        """
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d")
        return self._get_hsitory_one_day_all_minuter(entity_id, formatted_time)

    def __init__(self, token: str, ip="127.0.0.1", port="8123") -> None:
        self._api_prefix = "http://" + ip + ":" + port + "/api/"
        self._authorization = token


class HASS_DATA:
    _HASS_OPT: HASS_API

    def __init__(self, token: str, ip="127.0.0.1", port="8123") -> None:
        self._HASS_OPT = HASS_API(token, ip, port)


# test = HASS_API(HASS_TOKEN)
# now = datetime.now()
# yesterday_midnight = now - timedelta(days=1)
# formatted_time = yesterday_midnight.strftime("%Y-%m-%d")
# res = test.get_entity_hsitory_yesterday_all_minuter("sensor.atc_52df_temperature")
# print(res.__len__())
# print(res[0])
# print(res[1000])
