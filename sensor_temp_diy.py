import paho.mqtt.client as mqtt
import time
import sqlite3
import re
from datetime import datetime, timedelta
import os

HOST = "192.168.1.111" #服务器ip地址
PORT = 1800   #服务器端口
USER = 'master'     #登陆用户名
PASSWORD = 'master'    #用户名对应的密码
topic = 'mes/#'



class DEVICE:
    '''
    个人使用esp32自制的温度传感器
    '''
    flag=""
    table_1s=""
    table_15min=""
    __now_temp = "0"
    client:mqtt.Client
    def on_connect(self,client, userdata, flags, rc):
        rc_status = [ "连接成功", "协议版本错误", "无效的客户端标识", "服务器无法使用", "用户密码错误", "无授权" ]
        print("connect：" , rc_status[rc])

    def on_message(self,client, userdata, msg):
        text= str(msg.payload,'utf-8')
        self.fetch(text)
        # print("主题：", msg.topic)
        # print("消息：\r\n",  text,'\n' )

    def __init__(self, str) -> None:
        self.flag = str
        self.table_1s=str + "_s"
        self.table_15min=str + "_15min"

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect          #注册返回连接状态的回调函数
        self.client.username_pw_set(USER, PASSWORD)   #如果服务器要求需要账户密码
        self.client.will_set("test/die", "我死了", 0)  #设置遗嘱消息
        try:
            self.client.connect(HOST, PORT, keepalive=600) # 连接服务器
        except:
            print("error: 不能连接到mqtt服务器")
            print("\tHOST:%s\n\tPORT:%s" % ( HOST,PORT))
            return
        #client.disconnect() #断开连接，不会触发遗嘱消息
        
        self.client.on_message = self.on_message      #定义回调函数
        self.client.subscribe(topic, qos=0)   #订阅主题test/#
        self.client.loop_start()                 #非阻塞，启动接收线程
        # client.loop_forever()              #阻塞式，会卡死在这等待接收
        

    def __db_exe(self, str, is_today:bool=True):

        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

        today = datetime.now().strftime('%Y-%m-%d')
        day = None
        if is_today:
            day = today
        else:
            day = yesterday

        filename = "db/" + day + ".db"
        folder = os.path.exists("./db")
        if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs("./db")            #makedirs 创建文件时如果路径不存在会创建这个路径
        conn = sqlite3.connect(filename, check_same_thread=False)


        cursor = conn.cursor()
        # print(str)
        cursor.execute(str)
        conn.commit() # 提交事务
        value = cursor.fetchall()
        conn.close()
        return value

    def __db_creat_table(self, name):
        try:
            self.__db_exe('''
                CREATE TABLE {0} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    time INTEGER,
                    temp INTEGER
                )
            '''.format(name))
        except:
            pass
        
    def min15_today(self) -> list:
        data = [0 for i in range(95)]
        try:
            value = self.__db_exe("SELECT * FROM {0} ORDER BY id DESC LIMIT 96".format(self.table_15min))
            for i in value:
                # data.append(i)
                data[i[1]] = i[2] / 100
        except:
            pass
        return data
    def min15_yesterday(self) -> list:
        data = [0 for i in range(95)]
        try:
            value = self.__db_exe("SELECT * FROM {0} ORDER BY id DESC LIMIT 96".format(self.table_15min), False)
            for i in value:
                # data.append(i)
                data[i[1]] = i[2] / 100
        except:
            pass
        return data
        


    def get_temp(self) -> str:
        return self.__now_temp[0:-2] + "." + self.__now_temp[-2:]

    def fetch(self, msg):
        pattern = "Temp \[{0}\] = \[(\d+)\]".format(self.flag)
        match = re.search(pattern, msg)
        if match :
            temp=match.group(1)
            self.__now_temp = temp
            # print(self.flag, "=", temp)
            self.__db_creat_table(self.table_1s)
            self.__db_exe("INSERT INTO {0} (time, temp) VALUES ({1}, {2})".format(self.table_1s, time.time(), temp ))

        # 计算上一个已经完整度过的15分钟区间的开始和结束时间
        
        now = datetime.now()
        end_time = now - timedelta(minutes=now.minute % 15, seconds=now.second, microseconds=now.microsecond)
        start_time = end_time - timedelta(minutes=15)
        end_time = end_time.timestamp()
        start_time = start_time.timestamp()
        # print(end_time)
        # print(start_time)
        current_interval = now.hour * 4 + now.minute // 15
        last_interval = current_interval - 1
        # print("当前区间是", current_interval)
          
        self.__db_creat_table(self.table_15min)
        try:
            avg =  self.__db_exe("SELECT AVG(temp) FROM {0} WHERE time BETWEEN {1} AND {2}".format(self.table_1s, start_time, end_time))
            avg = int(avg[0][0])
            # print(f'Average temperature in the last completed 15-minute interval: {avg}')
            
            # 检查temp_15min表中是否有一行的time列等于last_interval
            # 如果没有这样的行，则插入一行新数据
            tmp = self.__db_exe('SELECT * FROM {0} WHERE time = {1}'.format(self.table_15min, last_interval))
            if len(tmp) == 0:
                # print("插入15min新行")
                self.__db_exe('INSERT INTO {0} (time, temp) VALUES ({1}, {2})'.format(self.table_15min, last_interval, avg))
        except:
            pass
           




SENSOR=[ 
    DEVICE("T1"), 
    DEVICE("T2"), 
    DEVICE("T3")
]

