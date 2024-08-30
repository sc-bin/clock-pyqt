HASS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI3ZTllODM4YTI2OWI0YjNlOWE5NzQ2Nzc2MDc3N2Y2MSIsImlhdCI6MTcyNDkxMTY0OSwiZXhwIjoyMDQwMjcxNjQ5fQ.6h_YU875EEImmW8EeBrTG4b0ASGDU1W5yXyTeJilsZ8"


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

Color_str = QColor(100, 100, 100, 200)
Color_num = QColor(150, 250, 80, 200)
Color_tmp_outside = QColor(255, 255, 0, 150)
Color_tmp_outside_dim = Color_str
Color_tmp_inside = Color_num
Color_up_str = QColor(255, 100, 150, 150)
Color_up_num = QColor(255, 230, 230, 150)

app = QtWidgets.QApplication(sys.argv)
ui = page.Ui_MainWindow()

# 设置鼠标指针为隐藏
QCursor.setPos(QtWidgets.QApplication.instance().desktop().screen().rect().center())
app.setOverrideCursor(Qt.BlankCursor)


class my_window(QtWidgets.QMainWindow):
    def paintEvent(self, event):
        # print("paintEvent")
        draw_clock(self, QPainter(self), ui.label_clock)
        now = datetime.now()
        formatted_time = now.strftime("%H:%M")
        label(self, QPainter(self), ui.label_clock_num).draw_str(
            formatted_time, QColor(255, 120, 0, 200), 50, offset_x=-90
        )
        # label(self, QPainter(self), ui.label_clock_num).draw_frame(Color_up_str)

        # 显示室外温度
        str_temp = " 🌡"+ HASS_API(HASS_TOKEN).get_state("sensor.atc_52df_temperature") 
        label(self, QPainter(self), ui.label_TNUM1).draw_str(
            str_temp, Color_tmp_outside, 40, offset_y=-25
        )
        label(self, QPainter(self), ui.label_chart1).add_chart_line(
            HASS_API(HASS_TOKEN).get_hsitory_yesterday("sensor.atc_52df_temperature"),
            Color_tmp_outside_dim,
            0,
            50,
        )
        label(self, QPainter(self), ui.label_chart1).add_chart_line(
            HASS_API(HASS_TOKEN).get_hsitory_today("sensor.atc_52df_temperature"),
            Color_tmp_outside,
            0,
            50,
        )
        label(self, QPainter(self), ui.label_chart1).draw_frame(Color_up_str)

        # 显示室外湿度
        str_humi = "🩸"+ HASS_API(HASS_TOKEN).get_state("sensor.atc_52df_humidity") 
        label(self, QPainter(self), ui.label_HNUM1).draw_str(
            str_humi, Color_tmp_outside, 40, offset_y=-25
        )
        label(self, QPainter(self), ui.label_chart2).add_chart_line(
            HASS_API(HASS_TOKEN).get_hsitory_today("sensor.atc_52df_humidity"),
            Color_tmp_outside,
            0,
            100,
        )
        label(self, QPainter(self), ui.label_chart2).add_chart_line(
            HASS_API(HASS_TOKEN).get_hsitory_yesterday("sensor.atc_52df_humidity"),
            Color_tmp_outside_dim,
            0,
            100,
        )
        label(self, QPainter(self), ui.label_chart2).draw_frame(Color_up_str)

        label(self, QPainter(self), ui.label_STR1).draw_str(
            "室外", Color_str, 50, offset_x=-60
        )
        label(self, QPainter(self), ui.label_STR2).draw_str(
            "室内", Color_str, 50, offset_x=-60
        )
        label(self, QPainter(self), ui.label_STR3).draw_str(
            "卧室", Color_str, 50, offset_x=-60
        )

        label(self, QPainter(self), ui.label_STR4).draw_str("粉丝 :", Color_up_str, 50)
        label(self, QPainter(self), ui.label_up_fans).draw_str(
            str(bilibili.fans), Color_up_num, 50
        )

        # label(self, QPainter(self), ui.label_STR4).draw_frame(Color_tmp_outside)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.close()


window = my_window()
ui.setupUi(window)


# 背景设置黑色
pal = QPalette(window.palette())
pal.setColor(QPalette.ColorRole.Background, QColor(Qt.GlobalColor.black))
window.setPalette(pal)

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
