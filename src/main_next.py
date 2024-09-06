HASS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI3ZTllODM4YTI2OWI0YjNlOWE5NzQ2Nzc2MDc3N2Y2MSIsImlhdCI6MTcyNDkxMTY0OSwiZXhwIjoyMDQwMjcxNjQ5fQ.6h_YU875EEImmW8EeBrTG4b0ASGDU1W5yXyTeJilsZ8"
TEST_TEMP = "sensor.temperature_humidity_sensor_9e8b_temperature"
TEST_HUMI = "sensor.temperature_humidity_sensor_9e8b_humidity"

ID_OUT_TEMP = TEST_TEMP
ID_OUT_HUMI = TEST_HUMI
ID_BEDROOM_TEMP = TEST_TEMP
ID_BEDROOM_HUMI = TEST_HUMI
ID_COMPUTER_TEMP = TEST_TEMP
ID_COMPUTER_HUMI = TEST_HUMI
# ID_OUT_TEMP = "sensor.atc_52df_temperature"
# ID_OUT_HUMI = "sensor.atc_52df_humidity"
# ID_BEDROOM_TEMP = "sensor.atc_52df_temperature"
# ID_BEDROOM_HUMI = "sensor.atc_52df_humidity"
# ID_COMPUTER_TEMP = "sensor.atc_52df_temperature"
# ID_COMPUTER_HUMI = "sensor.atc_52df_humidity"

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

Color_SENSER_TEMP = QColor(100, 230, 100, 200)
Color_SENSER_HUMI = QColor(65, 250, 250, 200)
Color_SENSER_CHART_FRAME = QColor(255, 230, 230, 150)

Color_up_str = QColor(255, 100, 150, 150)
Color_up_num = QColor(255, 230, 230, 150)

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


def chart_calculate(list1: list, list2=[]):
    """
    供绘制折线图使用,最多传入两个list,返回合适显示的y轴最小值与最大值
    """
    y_min = 0
    y_max = 0
    list_all = list1 + list2

    return (max(list_all) * 1.2,)


class my_window(QtWidgets.QMainWindow):
    def paintEvent(self, event):

        # 绘制时钟
        draw_clock(self, QPainter(self), ui.label_clock)
        now = datetime.now()
        formatted_time = now.strftime("%H:%M")
        ui.label_clock_num.setText(formatted_time)

        label(self, QPainter(self), ui.label_FRAME_1).draw_frame(
            Color_SENSER_CHART_FRAME
        )
        label(self, QPainter(self), ui.label_FRAME_2).draw_frame(
            Color_SENSER_CHART_FRAME
        )
        label(self, QPainter(self), ui.label_FRAME_3).draw_frame(
            Color_SENSER_CHART_FRAME
        )

        # 显示室外温度
        str_temp = " 🌡" + HASS_API(HASS_TOKEN).get_state(ID_OUT_TEMP)
        ui.label_TNUM_1.setText(str_temp)

        data_yesterday = HASS_API(HASS_TOKEN).get_hsitory_yesterday(ID_OUT_TEMP)
        data_today = HASS_API(HASS_TOKEN).get_hsitory_today(ID_OUT_TEMP)
        y_min = 0
        y_max = 50
        # non_zero_values = [x for x in data_yesterday + data_today if x != 0]
        # y_min = int(min(non_zero_values))
        # y_max = int(max(non_zero_values) + 1)
        label(self, QPainter(self), ui.label_chart1).add_chart_line(
            data_yesterday,
            Color_SENSER_CHART_FRAME,
            y_min,
            y_max,
        )
        label(self, QPainter(self), ui.label_chart1).add_chart_line(
            data_today,
            Color_SENSER_TEMP,
            y_min,
            y_max,
            show_dial=True,
        )
        label(self, QPainter(self), ui.label_chart1).draw_frame(
            Color_SENSER_CHART_FRAME
        )

        # 显示室外湿度
        str_humi = "💧" + HASS_API(HASS_TOKEN).get_state(ID_OUT_HUMI)
        ui.label_HNUM_1.setText(str_humi)

        data_yesterday = HASS_API(HASS_TOKEN).get_hsitory_yesterday(ID_OUT_HUMI)
        data_today = HASS_API(HASS_TOKEN).get_hsitory_today(ID_OUT_HUMI)
        y_min = 0
        y_max = 100
        # non_zero_values = [x for x in data_yesterday + data_today if x != 0]
        # y_min = int(min(non_zero_values))
        # y_max = int(max(non_zero_values) + 1)
        label(self, QPainter(self), ui.label_chart2).add_chart_line(
            data_today,
            Color_SENSER_HUMI,
            y_min,
            y_max,
            show_dial=True,
        )
        label(self, QPainter(self), ui.label_chart2).add_chart_line(
            data_yesterday,
            Color_SENSER_CHART_FRAME,
            y_min,
            y_max,
        )
        label(self, QPainter(self), ui.label_chart2).draw_frame(
            Color_SENSER_CHART_FRAME
        )

        # 显示卧室温度
        str_temp = " 🌡" + HASS_API(HASS_TOKEN).get_state(ID_BEDROOM_TEMP)
        ui.label_TNUM_2.setText(str_temp)

        data_yesterday = HASS_API(HASS_TOKEN).get_hsitory_yesterday(ID_BEDROOM_TEMP)
        data_today = HASS_API(HASS_TOKEN).get_hsitory_today(ID_BEDROOM_TEMP)
        y_min = 0
        y_max = 50
        # non_zero_values = [x for x in data_yesterday + data_today if x != 0]
        # y_min = int(min(non_zero_values))
        # y_max = int(max(non_zero_values) + 1)
        label(self, QPainter(self), ui.label_chart3).add_chart_line(
            data_yesterday,
            Color_SENSER_CHART_FRAME,
            y_min,
            y_max,
        )
        label(self, QPainter(self), ui.label_chart3).add_chart_line(
            data_today,
            Color_SENSER_TEMP,
            y_min,
            y_max,
            show_dial=True,
        )
        label(self, QPainter(self), ui.label_chart3).draw_frame(
            Color_SENSER_CHART_FRAME
        )

        # 显示室外湿度
        str_humi = "🩸" + HASS_API(HASS_TOKEN).get_state(ID_BEDROOM_HUMI)
        ui.label_HNUM_2.setText(str_humi)

        data_yesterday = HASS_API(HASS_TOKEN).get_hsitory_yesterday(ID_BEDROOM_HUMI)
        data_today = HASS_API(HASS_TOKEN).get_hsitory_today(ID_BEDROOM_HUMI)
        y_min = 0
        y_max = 100
        # non_zero_values = [x for x in data_yesterday + data_today if x != 0]
        # y_min = int(min(non_zero_values))
        # y_max = int(max(non_zero_values) + 1)
        label(self, QPainter(self), ui.label_chart4).add_chart_line(
            data_today,
            Color_SENSER_HUMI,
            y_min,
            y_max,
            show_dial=True,
        )
        label(self, QPainter(self), ui.label_chart4).add_chart_line(
            data_yesterday,
            Color_SENSER_CHART_FRAME,
            y_min,
            y_max,
        )
        label(self, QPainter(self), ui.label_chart4).draw_frame(
            Color_SENSER_CHART_FRAME
        )

        # 显示客厅温度
        str_temp = " 🌡" + HASS_API(HASS_TOKEN).get_state(ID_COMPUTER_TEMP)
        ui.label_TNUM_3.setText(str_temp)

        # 显示客厅湿度
        str_humi = "🩸" + HASS_API(HASS_TOKEN).get_state(ID_COMPUTER_HUMI)
        ui.label_HNUM_3.setText(str_humi)

        # 显示粉丝数
        label(self, QPainter(self), ui.label_STR4).draw_str("粉丝 :", Color_up_str, 50)
        label(self, QPainter(self), ui.label_up_fans).draw_str(
            str(bilibili.fans), Color_up_num, 50
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
