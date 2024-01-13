from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import math
from datetime import datetime
from  mqtt_listen import *



#define COLOR_TEMP_DATA QColor(0, 200, 150, 150)
#define COLOR_TEMP_BACKGROUND QColor(180, 50, 180, 255)

class label(QPainter):
    window:QtWidgets.QMainWindow
    left_x:int
    left_y:int
    width:int
    height:int
    sensor:DEVICE
    str:str
    _painter:QPainter
    rect:QRectF
    def draw_number(self, num:int, color:QColor):
        painter = self._painter
        painter.setPen( color )
        tmp_font = QFont(painter.font())
        tmp_font.setPointSize(50)
        painter.setFont(tmp_font)
        size = painter.font().pointSize()
        # print(size)

        painter.drawText(self.rect, Qt.AlignmentFlag.AlignLeft, num)
        
    def draw_str(self, string:str, color:QColor):
        painter = self._painter
        painter.setPen( color )
        tmp_font = QFont(painter.font())
        tmp_font.setPointSize(50)
        painter.setFont(tmp_font)
        size = painter.font().pointSize()
        painter.drawText(self.rect, Qt.AlignmentFlag.AlignLeft, string)

    def draw_frame(self, color:QColor):
        painter = self._painter
        # 图标外框
        painter.setPen(color)
        painter.drawRect(-100, -50, 200, 100)


    def add_chart_line(self, data:list, color:QColor):
        painter = self._painter

        painter.setPen(color)
        # data = self.sensor.min15_yesterday()
        path = QPainterPath()
        path.moveTo(-100, 50)
        for i in range(len(data)):
            path.lineTo(-100 + i*2, (-data[i] * 2 ) + 50 )
        painter.drawPath(path)



    def __init__(self, window:QtWidgets.QMainWindow,  painter:QPainter, label:QtWidgets.QLabel):
        self.window = window
        self.width = label.width()
        self.height = label.height()
        self.left_x = label.pos().x()
        self.left_y = label.pos().y()
        label.hide()
        # # 图标外框
        # painter.setPen( Color_str )
        
        # painter.setPen(Color_str)
        # painter.drawRect(-100, -50, 95, 100)

        painter.translate( self.left_x + self.width/2, self.left_y + self.height/2)
        painter.scale(self.width / 200.0, self.height / 100.0)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        self._painter = painter
        self.rect= QRectF()
        self.rect.setX( -80 )
        self.rect.setY( -30 )
        self.rect.setHeight(200)
        self.rect.setWidth(200)