from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import math
from datetime import datetime



Color_hour_line = QColor(100, 100, 100, 200)
Color_hour_pointer = QColor(255, 120, 0, 200)
Color_minute_line = QColor(200, 200, 200, 150)
Color_minute_pointer = QColor(0, 255, 0, 200)
Color_sec_pointer = QColor(200, 200, 0, 150)
Color_center = QColor(50, 50, 100, 255)

# 时针形状
NEEDLE_HOUR_heigh = 20
NEEDLE_HOUR_width = 4
NEEDLE_HOUR_heigh_anoth = 6
pointr_hour=[
    QPoint(int(NEEDLE_HOUR_width/2), NEEDLE_HOUR_heigh_anoth),
    QPoint(int(-NEEDLE_HOUR_width/2), NEEDLE_HOUR_heigh_anoth),
    QPoint(int(-NEEDLE_HOUR_width/2), -NEEDLE_HOUR_heigh),
    QPoint(0, -NEEDLE_HOUR_heigh-6),
    QPoint(int(NEEDLE_HOUR_width/2), -NEEDLE_HOUR_heigh),
]

# 时针形状
NEEDLE_minute_heigh = 60
NEEDLE_minute_width = 4
NEEDLE_minute_heigh_anoth = 3
pointr_minute=[
    QPoint(int(NEEDLE_minute_width/2), NEEDLE_minute_heigh_anoth),
    QPoint(int(-NEEDLE_minute_width/2), NEEDLE_minute_heigh_anoth),
    QPoint(int(-NEEDLE_minute_width/2), -NEEDLE_minute_heigh),
    QPoint(0, -NEEDLE_minute_heigh-6),
    QPoint(int(NEEDLE_minute_width/2), -NEEDLE_minute_heigh),
]

# 秒针形状
NEEDLE_sec_heigh = 97
NEEDLE_sec_width = 2
NEEDLE_sec_heigh_anoth = 6
pointr_sec=[
    QPoint(int(NEEDLE_sec_width/2), NEEDLE_sec_heigh_anoth),
    QPoint(int(-NEEDLE_sec_width/2), NEEDLE_sec_heigh_anoth),
    QPoint(int(-NEEDLE_sec_width/2), -NEEDLE_sec_heigh),
    QPoint(int(NEEDLE_sec_width/2), -NEEDLE_sec_heigh),
]



class draw_clock(QPainter):
    window:QtWidgets.QMainWindow
    left_x:int
    left_y:int
    width:int
    height:int

    def draw(self, painter:QPainter):
        side = min( self.width, self.height)
        painter.translate( self.left_x + side/2, self.left_y + side/2)
        painter.scale(side / 200.0, side / 200.0)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 表盘-数字
        painter.setPen( Color_hour_line )
        painter.setBrush( Color_hour_line )  
        tmp_font = QFont(painter.font())
        tmp_font.setPointSize(int(side/90))
        painter.setFont(tmp_font)
        size = painter.font().pointSize()
        for i in range(1, 13):
            if i == datetime.now().hour%12:
                painter.setPen( Color_hour_pointer )
                painter.setBrush( Color_hour_pointer )
            else :
                painter.setPen( Color_hour_line )
                painter.setBrush( Color_hour_line )
                
            rect = QRectF()
            mx =  80 * math.sin(math.radians(i*30)) - size 
            my =  80 * math.cos(math.radians(i*30)) + size / 2
            mx = int( mx )
            my = int( -my )
            rect.setX( mx)

            rect.setY(my)
            rect.setHeight(size)
            rect.setWidth(size*2)
            # painter.drawLine(0, 0, mx, my)
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, str(i))


    
        # 时针
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush( Color_hour_pointer )
        painter.save()
        painter.rotate(30.0 * (  datetime.now().hour  + datetime.now().minute / 60 ))
        painter.drawConvexPolygon(pointr_hour)
        painter.restore()

        # 分针
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush( Color_minute_pointer )
        painter.save()
        painter.rotate(6 * datetime.now().minute)
        painter.drawConvexPolygon(pointr_minute)
        painter.restore()

        # 秒针
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush( Color_sec_pointer )
        
        painter.save()
        painter.rotate(6 * datetime.now().second)
        painter.drawConvexPolygon(pointr_sec)
        painter.restore()

        # 中心圆
        painter.setPen(Color_center)
        painter.setBrush(Color_center)
        CENTER_r = 2
        painter.drawEllipse(-CENTER_r, -CENTER_r, CENTER_r*2, CENTER_r*2)


        # 表盘-小时线
        painter.save()
        painter.setPen(Color_hour_line)
        painter.rotate(-90)
        for i in range(0, 360, 30):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30)
        painter.restore()

        # 表盘-当前小时线
        painter.save()
        painter.setPen( Color_hour_pointer )
        painter.rotate(datetime.now().hour % 12 * 30 - 90 )
        painter.drawLine(88, 0, 96, 0)
        painter.restore()

        # 表盘-分钟线
        painter.save()
        painter.setPen(Color_minute_line)
        # painter.rotate(-90)
        for i in range(0, 360, 6):
            if i%30 !=0 :
                painter.drawLine(95, 0, 96, 0)
            painter.rotate(6) 
        painter.restore()

        # 表盘-当前分钟线
        painter.save()
        painter.setPen( Color_minute_pointer )
        painter.rotate(datetime.now().minute % 60 * 6 - 90 )
        painter.drawLine(90, 0, 96, 0)
        painter.restore()



    def __init__(self, window:QtWidgets.QMainWindow,  painter:QPainter, label:QtWidgets.QLabel):
        # painter.begin(window)
        self.window = window
        self.width = label.width()
        self.height = label.height()
        self.left_x = label.pos().x()
        self.left_y = label.pos().y()
        self.draw(painter)
        label.hide()
        # painter.end()
   
