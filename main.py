import sys
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import page
from draw_clock import draw_clock
from draw_label import label
from  mqtt_listen import *

Color_str = QColor(100, 100, 100, 200)
Color_num = QColor(150, 250, 80, 200)
Color_tmp_outside = QColor(255, 255, 0, 150)
Color_tmp_outside_dim = Color_str
Color_tmp_inside = Color_num

app = QtWidgets.QApplication(sys.argv)
ui = page.Ui_MainWindow()

class my_window(QtWidgets.QMainWindow):
    def paintEvent(self, event):
        # print("paintEvent")
        draw_clock(self, QPainter(self), ui.label_clock)
        label(self, QPainter(self), ui.label_TNUM3).draw_number(SENSOR[0].get_temp(), Color_num)
        label(self, QPainter(self), ui.label_TNUM1).draw_number(SENSOR[1].get_temp(), Color_tmp_outside)
        label(self, QPainter(self), ui.label_TNUM2).draw_number(SENSOR[2].get_temp(), Color_tmp_inside)
        label(self, QPainter(self), ui.label_STR3).draw_str( "卧室", Color_str)
        label(self, QPainter(self), ui.label_STR1).draw_str( "室外", Color_str)
        label(self, QPainter(self), ui.label_STR2).draw_str( "室内", Color_str)
        label(self, QPainter(self), ui.label_chart).add_chart_line( SENSOR[2].min15_today(), Color_tmp_inside)
        label(self, QPainter(self), ui.label_chart).add_chart_line( SENSOR[1].min15_today(), Color_tmp_outside)
        label(self, QPainter(self), ui.label_chart).add_chart_line( SENSOR[1].min15_yesterday(), Color_tmp_outside_dim)


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


# window.show()
window.showFullScreen()
sys.exit(app.exec_())
