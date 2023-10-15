import sys
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import page
from draw_clock import draw_clock

    
class my_window(QtWidgets.QMainWindow):
    def paintEvent(self, event):
        # print("paintEvent")
        draw_clock(self, QPainter(self), event)

        

app = QtWidgets.QApplication(sys.argv)
window = my_window()
ui = page.Ui_MainWindow()
ui.setupUi(window)

# 设置按钮关闭窗口
def close_window():
    window.close()
ui.pushButton.clicked.connect(close_window)

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
