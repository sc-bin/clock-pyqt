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

import page
from draw_clock import draw_clock
from draw_label import label
from sensor_hass_temp_xiaomi import *
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

        s_home_temp = xiaomi_temp.temperature("9e8b")
        if s_home_temp != None:
            if s_home_temp.is_update_in_30s():
                label(self, QPainter(self), ui.label_TNUM1).draw_str(
                    s_home_temp.get_last_value(), Color_tmp_outside
                )
            else:
                label(self, QPainter(self), ui.label_TNUM1).draw_str(
                    "--", Color_tmp_outside
                )
            label(self, QPainter(self), ui.label_chart).add_chart_line(
                s_home_temp.get_min15_today(), Color_tmp_outside
            )
        s_home_humi = xiaomi_temp.humidity("9e8b")
        if s_home_humi != None:
            if s_home_humi.is_update_in_30s():
                label(self, QPainter(self), ui.label_TNUM2).draw_str(
                    s_home_humi.get_last_value(), Color_tmp_inside
                )
            else:
                label(self, QPainter(self), ui.label_TNUM2).draw_str(
                    "--", Color_tmp_outside
                )

        # temp = xiaomi_temp.get_temperature("9e8b")
        # # temp = xiaomi_temp.get_temperature("9e8b")
        # label(self, QPainter(self), ui.label_TNUM1).draw_str(temp, Color_tmp_outside)

        # humi = xiaomi_temp.get_humidity("9e8b")
        # label(self, QPainter(self), ui.label_TNUM2).draw_str(humi, Color_tmp_inside)

        # label(self, QPainter(self), ui.label_TNUM1).draw_str(
        #     SENSOR[1].get_temp(), Color_tmp_outside
        # )
        # label(self, QPainter(self), ui.label_TNUM2).draw_str(
        #     SENSOR[2].get_temp(), Color_tmp_inside
        # )
        # label(self, QPainter(self), ui.label_TNUM3).draw_str(
        #     SENSOR[0].get_temp(), Color_num
        # )
        # label(self, QPainter(self), ui.label_STR1).draw_str("室外", Color_str)
        # label(self, QPainter(self), ui.label_STR2).draw_str("室内", Color_str)
        # label(self, QPainter(self), ui.label_STR3).draw_str("卧室", Color_str)
        # label(self, QPainter(self), ui.label_chart).add_chart_line(
        #     SENSOR[1].min15_today(), Color_tmp_outside
        # )
        # label(self, QPainter(self), ui.label_chart).add_chart_line(
        #     SENSOR[1].min15_yesterday(), Color_tmp_outside_dim
        # )

        label(self, QPainter(self), ui.label_STR4).draw_str("粉丝 :", Color_up_str)
        label(self, QPainter(self), ui.label_up_fans).draw_str(
            str(bilibili.fans), Color_up_num
        )

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
