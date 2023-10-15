from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import math
from datetime import datetime
from  mqtt_listen import *

Color_str = QColor(50, 150, 100, 100)
Color_num = QColor(100, 200, 50, 100)


class draw_temp(QPainter):
    window:QtWidgets.QMainWindow
    left_x:int
    left_y:int
    width:int
    height:int
    sensor:DEVICE
    str:str

    def draw(self, painter:QPainter):
        painter.translate( self.left_x + self.width/2, self.left_y + self.height/2)
        painter.scale(self.width / 200.0, self.height / 100.0)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 右上角文字标签
        painter.setPen( Color_str )
        tmp_font = QFont(painter.font())
        # tmp_font.setPointSize(20)
        # print(self.height)
        tmp_font.setPointSize(20)
        painter.setFont(tmp_font)
        size = painter.font().pointSize()
        # print(size)
        rect = QRectF()
        rect.setX( 0 )
        rect.setY( -30 )
        rect.setHeight(50)
        rect.setWidth(100)
        # painter.drawLine(0, 0, mx, my)
        painter.drawText(rect, Qt.AlignmentFlag.AlignLeft, self.str)

        # 右下角数字
        painter.setPen( Color_num )
        tmp_font = QFont(painter.font())
        # tmp_font.setPointSize(20)
        # print(self.height)
        tmp_font.setPointSize(30)
        painter.setFont(tmp_font)
        size = painter.font().pointSize()
        # print(size)
        rect = QRectF()
        rect.setX( 0 )
        rect.setY( 0 )
        rect.setHeight(50)
        rect.setWidth(100)
        # painter.drawLine(0, 0, mx, my)
        painter.drawText(rect, Qt.AlignmentFlag.AlignLeft, self.sensor.get_temp())


    def __init__(self, window:QtWidgets.QMainWindow,  painter:QPainter, label:QtWidgets.QLabel, num:int, str:str):
        self.window = window
        self.width = label.width()
        self.height = label.height()
        self.left_x = label.pos().x()
        self.left_y = label.pos().y()
        self.sensor = SENSOR[num]
        self.str = str
        self.draw(painter)
