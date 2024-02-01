import sys
import threading
#【可选代码】允许Thonny远程运行
import os
os.environ["DISPLAY"] = ":0.0"

from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import page
from draw_clock import draw_clock
from draw_label import label
from  mqtt_listen import *
from bilibili import bilibili
Color_str = QColor(100, 100, 100, 200)
Color_num = QColor(150, 250, 80, 200)
Color_tmp_outside = QColor(255, 255, 0, 150)
Color_tmp_outside_dim = Color_str
Color_tmp_inside = Color_num
Color_up_str = QColor(255, 100, 150, 150)
Color_up_num = QColor(255, 230, 230, 150)

app = QtWidgets.QApplication(sys.argv)
ui = page.Ui_MainWindow()

class my_window(QtWidgets.QMainWindow):
    def paintEvent(self, event):
        # print("paintEvent")
        draw_clock(self, QPainter(self), ui.label_clock)
        
        label(self, QPainter(self), ui.label_TNUM1).draw_str(SENSOR[1].get_temp(), Color_tmp_outside)
        label(self, QPainter(self), ui.label_TNUM2).draw_str(SENSOR[2].get_temp(), Color_tmp_inside)
        label(self, QPainter(self), ui.label_TNUM3).draw_str(SENSOR[0].get_temp(), Color_num)
        label(self, QPainter(self), ui.label_STR1).draw_str( "室外", Color_str)
        label(self, QPainter(self), ui.label_STR2).draw_str( "室内", Color_str)
        label(self, QPainter(self), ui.label_STR3).draw_str( "卧室", Color_str)
        # label(self, QPainter(self), ui.label_chart).add_chart_line( SENSOR[2].min15_today(), Color_tmp_inside)
        label(self, QPainter(self), ui.label_chart).add_chart_line( SENSOR[1].min15_today(), Color_tmp_outside)
        label(self, QPainter(self), ui.label_chart).add_chart_line( SENSOR[1].min15_yesterday(), Color_tmp_outside_dim)

        label(self, QPainter(self), ui.label_STR4).draw_str("粉丝 :", Color_up_str)
        label(self, QPainter(self), ui.label_STR5).draw_str("点赞 :", Color_up_str)
        label(self, QPainter(self), ui.label_STR6).draw_str("播放 :", Color_up_str)
        label(self, QPainter(self), ui.label_up_fans).draw_str(str(bilibili.fans), Color_up_num)
        label(self, QPainter(self), ui.label_up_like).draw_str(str(bilibili.like), Color_up_num)
        label(self, QPainter(self), ui.label_up_view).draw_str(str(bilibili.view), Color_up_num)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.close()

window = my_window()
ui.setupUi(window)


# 背景设置黑色
pal = QPalette(window.palette())
pal.setColor( QPalette.ColorRole.Background , QColor(Qt.GlobalColor.black))
window.setPalette(pal)

# 定时触发重绘
window.timer = QTimer()  # 定时器
window.timer.timeout.connect(window.update)
window.timer.start(1000)  # 每1s 更新一次


bilitimer = QTimer()  # 定时器
bilitimer.timeout.connect(bilibili.update)
bilitimer.start(15000)  # 每15s 更新一次

# window.show()
window.showFullScreen()
sys.exit(app.exec_())
