import sys
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import page
from draw_clock import draw_clock
from draw_temp import draw_temp

app = QtWidgets.QApplication(sys.argv)
ui = page.Ui_MainWindow()
class my_window(QtWidgets.QMainWindow):
    def paintEvent(self, event):
        # print("paintEvent")
        draw_clock(self, QPainter(self), ui.label_clock)
        draw_temp(self, QPainter(self), ui.label_T3, 0, "卧室")
        draw_temp(self, QPainter(self), ui.label_T1, 1, "室外")
        draw_temp(self, QPainter(self), ui.label_T2, 2, "室内")
        # draw_temp(self, QPainter(self), ui.label_T1, 1)
        # draw_temp(self, QPainter(self), ui.label_T1, 2)
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
