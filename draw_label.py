from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import math
from datetime import datetime
from  mqtt_listen import *



class label(QPainter):
    '''
    传入一个qt label,然后以他的坐标尺寸绘制指定物品
    '''
    window:QtWidgets.QMainWindow
    left_x:int
    left_y:int
    width:int
    height:int
    sensor:DEVICE
    str:str
    _painter:QPainter
    rect:QRectF

    def draw_str(self, string:str, color:QColor):
        '''
        绘制字符串
        '''
        painter = self._painter
        painter.setPen( color )
        tmp_font = QFont(painter.font())
        tmp_font.setPointSize(50)
        painter.setFont(tmp_font)
        size = painter.font().pointSize()
        painter.drawText(self.rect, Qt.AlignmentFlag.AlignLeft, string)

    def draw_frame(self, color:QColor):
        '''
        绘制一个外框
        '''
        painter = self._painter
        painter.setPen(color)
        painter.drawRect(-100, -50, 200, 100)


    def add_chart_line(self, data:list, color:QColor):
        '''
        利用传入的数据，绘制折线图
        '''
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