import paho.mqtt.client as mqtt
import time
import sqlite3
import re
from datetime import datetime, timedelta
import os

HOST = "127.0.0.1"  # 服务器ip地址
PORT = 1883  # 服务器端口
USER = "pi"  # 登陆用户名
PASSWORD = "pi"  # 用户名对应的密码
topic = "homeassistant/#"


class DB_DATE:
    """
    创建sqlite表格，用于存储与查找一种属性数据
    """

    id: str
    page_name_raw: str
    page_name_15min: str

    def __init__(self, page_name_prefix: str) -> None:
        self.id = page_name_prefix
        self.page_name_raw = page_name_prefix
        self.page_name_15min = page_name_prefix + "_15min"

    def _db_exe(self, cmd, is_today: bool = True):
        """
        自动创建以日期为名的sql文件,并在其中执行传入的命令
        """
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        today = datetime.now().strftime("%Y-%m-%d")
        day = None
        if is_today:
            day = today
        else:
            day = yesterday

        filename = "db/" + day + ".db"
        folder = os.path.exists("./db")
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs("./db")  # makedirs 创建文件时如果路径不存在会创建这个路径
        conn = sqlite3.connect(filename, check_same_thread=False)

        cursor = conn.cursor()
        cursor.execute(cmd)
        conn.commit()  # 提交事务
        value = cursor.fetchall()
        conn.close()
        return value

    def _db_create_page(self, page_name) -> None:
        """
        尝试在今日sql文件中创建对应页
        """
        cmd = """
                CREATE TABLE {0} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    flag INTEGER,
                    value INTEGER
                )
            """.format(
            page_name
        )
        try:
            return self._db_exe(cmd)
        except:
            return None

    def _db_page_add_date(self, page_name, flag, value):
        return self._db_exe(
            "INSERT INTO {0} (flag, value) VALUES ({1}, {2})".format(
                page_name, flag, value
            )
        )

    def add(self, value) -> None:
        timestamp = time.time()
        print("写入%s : \t%s \t%s" % (self.page_name_raw, timestamp, value))
        self._db_create_page(self.page_name_raw)
        self._db_page_add_date(self.page_name_raw, timestamp, value)


def get_str_mid(str_raw: str, str1: str, str2: str):
    """
    搜索字符串,从第一个字符串的末尾到字符串2之前。搜索不到则返回None
    """
    result_start = str_raw.find(str1)
    if result_start == -1:
        return None
    result_start += len(str1)
    end = str_raw.find(str2, result_start)
    if end == -1:
        return None
    return str_raw[result_start:end]


class DEVICE_HASS_XIAOMI_TEMP_1:
    """
    通过hass的mqtt转发功能,获取所有小米温湿度计1的信息
    """

    sensors = {"0": DB_DATE("0")}

    client: mqtt.Client

    def on_connect(self, client, userdata, flags, rc):
        rc_status = [
            "连接成功",
            "协议版本错误",
            "无效的客户端标识",
            "服务器无法使用",
            "用户密码错误",
            "无授权",
        ]
        print("connect：", rc_status[rc])

    def on_message(self, client, userdata, msg):
        text = str(msg.payload, "utf-8")
        self.fetch_attr("humidity", msg.topic, text)
        self.fetch_attr("temperature", msg.topic, text)
        # print("主题：", msg.topic)
        # print("消息：\r\n",  text,'\n' )

    def gen_page_name(self, id: str, attr: str) -> str:
        return "s_" + id + "_" + attr

    def fetch_attr(self, attr: str, topic: str, text: str):
        id = get_str_mid(
            topic, "homeassistant/sensor/temperature_humidity_sensor_", "_" + attr
        )
        if id == None:
            return
        sensor_key = self.gen_page_name(id, attr)
        if sensor_key not in self.sensors.keys():
            self.sensors[sensor_key] = DB_DATE(sensor_key)

        if (
            topic
            == "homeassistant/sensor/temperature_humidity_sensor_"
            + id
            + "_"
            + attr
            + "/state"
        ):
            self.sensors[sensor_key].add(text)

    def __init__(self) -> None:
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect  # 注册返回连接状态的回调函数
        self.client.username_pw_set(USER, PASSWORD)  # 如果服务器要求需要账户密码
        self.client.will_set("test/die", "我死了", 0)  # 设置遗嘱消息
        try:
            self.client.connect(HOST, PORT, keepalive=600)  # 连接服务器
        except:
            print("error: 不能连接到mqtt服务器")
            print("\tHOST:%s\n\tPORT:%s" % (HOST, PORT))
            return
        # client.disconnect() #断开连接，不会触发遗嘱消息

        self.client.on_message = self.on_message  # 定义回调函数
        self.client.subscribe(topic, qos=0)  # 订阅主题test/#
        self.client.loop_start()  # 非阻塞，启动接收线程
        # client.loop_forever()              #阻塞式，会卡死在这等待接收


xiaomi_temp = DEVICE_HASS_XIAOMI_TEMP_1()