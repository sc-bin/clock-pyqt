HASS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxNGY2ZTk0MGIzNzI0ODcyOWFhMzk3MjM3MWU0YmMwOCIsImlhdCI6MTcyNjc4NzMwNCwiZXhwIjoyMDQyMTQ3MzA0fQ.0w6czUHoeelfpiUM0YDmRRumwsEjoKCZys9a1A7CSSY"

ID_OUTSIDE_TEMP = "sensor.atc_42f8_temperature"
ID_OUTSIDE_HUMI = "sensor.atc_42f8_humidity"
ID_ROOM_TEMP =  "sensor.atc_52df_temperature"
ID_ROOM_HUMI = "sensor.atc_52df_humidity"
ID_BEDROOM_TEMP = "sensor.a4_c1_38_14_dd_f1_ddf1_temperature"
ID_BEDROOM_HUMI = "sensor.a4_c1_38_14_dd_f1_ddf1_humidity"

import sys
import threading

# 【可选代码】允许Thonny远程运行
import os

os.environ["DISPLAY"] = ":0.0"

from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *

# 【建议代码】允许终端通过ctrl+c中断窗口，方便调试
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)
timer = QTimer()
timer.start(100)  # You may change this if you wish.
timer.timeout.connect(lambda: None)  # Let the interpreter run each 100 ms

import page2 as page
from draw_clock import draw_clock
from draw_label import label
from hass_api import *
from spider_bilibili import bilibili

app = QtWidgets.QApplication(sys.argv)
ui = page.Ui_MainWindow()

# 设置鼠标指针为隐藏
QCursor.setPos(QtWidgets.QApplication.instance().desktop().screen().rect().center())
app.setOverrideCursor(Qt.BlankCursor)

font_id = QFontDatabase.addApplicationFont("SEGUIEMJ.TTF")
font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
print(f"字体名称为{font_family}")
font = QFont(font_family)
app.setFont(font)


class ChartLabel(QtWidgets.QLabel):
    entity: str
    color_main: QColor
    y_min: int
    y_max: int

    def __init__(
        self,
        parent: QtWidgets.QLabel,
        entity_id: str,
        color_main_line: QColor,
        y_min=0,
        y_max=50,
    ):
        """
        在label上绘制图表的类
            @parent: 继承父label,使用其尺寸及位置
            @entity_id: 实体id,准备在这个图标中显示的
            @color_main_line: 今日数据的线条颜色
            @y_min: y轴刻度起始
            @y_max: y轴刻度最大值
        """
        super(ChartLabel, self).__init__(parent)
        self.resize(parent.width(), parent.height())
        parent.setText("")
        self.entity = entity_id
        self.color_main = color_main_line
        self.y_min = y_min
        self.y_max = y_max

        # self.timer = QTimer()  # 定时器
        # self.timer.timeout.connect(self.update)
        # self.timer.start(300000)  # 每5min 更新一次

    def draw_chart_line(self, data: list, color=None):
        """
        利用传入的数据，绘制折线图
        @data: 数据列表
        @color: 线条颜色
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 设置抗锯齿
        painter.save()
        if color != None:
            painter.setPen(color)
        painter.translate(self.pos().x(), self.pos().y() + self.height())
        painter.scale(self.width() / len(data), 1)
        y_scale = self.height() / (self.y_max - self.y_min)
        path = QPainterPath()
        path.moveTo(0, 0)
        for i in range(len(data)):
            if data[i] == 0:
                path.lineTo(i, 0)
            else:
                path.lineTo(i, -((data[i] - self.y_min)) * y_scale)
        painter.drawPath(path)

        painter.restore()

    def paintEvent(self, event):
        # print("重绘")
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 设置抗锯齿

        data_yesterday = HASS_API(HASS_TOKEN).get_hsitory_yesterday(self.entity)
        data_today = HASS_API(HASS_TOKEN).get_hsitory_today(self.entity)
        self.draw_chart_line(data_yesterday)
        self.draw_chart_line(data_today, self.color_main)


class my_window(QtWidgets.QMainWindow):
    def paintEvent(self, event):

        # 绘制时钟
        draw_clock(self, QPainter(self), ui.label_clock)
        now = datetime.now()
        formatted_time = now.strftime("%H:%M")
        ui.label_clock_num.setText(formatted_time)

        # 显示室外温度
        str_temp = "🌡" + HASS_API(HASS_TOKEN).get_state(ID_OUTSIDE_TEMP)
        ui.label_TNUM_1.setText(str_temp)

        # 显示室外湿度
        str_humi = "💧" + HASS_API(HASS_TOKEN).get_state(ID_OUTSIDE_HUMI)
        ui.label_HNUM_1.setText(str_humi)

        # 显示卧室温度
        str_temp = "🌡" + HASS_API(HASS_TOKEN).get_state(ID_BEDROOM_TEMP)
        ui.label_TNUM_2.setText(str_temp)

        # 显示室外湿度
        str_humi = "🩸" + HASS_API(HASS_TOKEN).get_state(ID_BEDROOM_HUMI)
        ui.label_HNUM_2.setText(str_humi)

        # 显示客厅温度
        str_temp = "🌡" + HASS_API(HASS_TOKEN).get_state(ID_ROOM_TEMP)
        ui.label_TNUM_3.setText(str_temp)

        # 显示客厅湿度
        str_humi = "🩸" + HASS_API(HASS_TOKEN).get_state(ID_ROOM_HUMI)
        ui.label_HNUM_3.setText(str_humi)

        # 显示粉丝数
        ui.label_up_fans.setText(str(bilibili.fans))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.close()


window = my_window()
ui.setupUi(window)

COLOR_T1 = ui.label_TNUM_1.palette().color(QPalette.WindowText)
COLOR_T2 = ui.label_TNUM_2.palette().color(QPalette.WindowText)
COLOR_T3 = ui.label_TNUM_3.palette().color(QPalette.WindowText)
COLOR_H1 = ui.label_HNUM_1.palette().color(QPalette.WindowText)
COLOR_H2 = ui.label_HNUM_2.palette().color(QPalette.WindowText)
COLOR_H3 = ui.label_HNUM_3.palette().color(QPalette.WindowText)
ChartLabel(ui.label_chartT_1, ID_OUTSIDE_TEMP, COLOR_T1)
ChartLabel(ui.label_chartH_1, ID_OUTSIDE_HUMI, COLOR_H1, 0, 100)
ChartLabel(ui.label_chartT_2, ID_BEDROOM_TEMP, COLOR_T2)
ChartLabel(ui.label_chartH_2, ID_BEDROOM_HUMI, COLOR_H2, 0, 100)
ChartLabel(ui.label_chartT_3, ID_ROOM_TEMP, COLOR_T3)
ChartLabel(ui.label_chartH_3, ID_ROOM_HUMI, COLOR_H3, 0, 100)

# # 背景设置黑色
# pal = QPalette(window.palette())
# pal.setColor(QPalette.ColorRole.Background, QColor(Qt.GlobalColor.black))
# window.setPalette(pal)

# 定时触发重绘
window.timer = QTimer()  # 定时器
window.timer.timeout.connect(window.update)
window.timer.start(1000)  # 每1s 更新一次


bilitimer = QTimer()  # 定时器
bilitimer.timeout.connect(bilibili.update)
bilitimer.start(60 * 60 * 24 * 1000)  # 每隔24小时更新一次
# window.show()
window.showFullScreen()

sys.exit(app.exec_())
