from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets


class label(QPainter):
    """
    传入一个qt label,然后以他的坐标尺寸绘制指定物品
    """

    window: QtWidgets.QMainWindow
    left_x: int
    left_y: int
    width: int
    height: int
    str: str
    _painter: QPainter
    rect: QRectF

    def draw_str(
        self, string, color: QColor, pointsize=30, offset_x=-100, offset_y=-50
    ):
        """
        绘制字符串
        """
        rect = QRectF()
        rect.setX(offset_x)
        rect.setY(offset_y)
        rect.setHeight(100)
        rect.setWidth(200)

        painter = self._painter
        painter.save()
        painter.translate(self.left_x + self.width / 2, self.left_y + self.height / 2)
        # 将xy坐标原点移到正中间
        painter.scale(self.width / 200.0, self.height / 100.0)
        # 修改xy坐标点与实际像素距离的对应关系，xy变为宽200 高100

        painter.setPen(color)
        tmp_font = QFont(painter.font())
        tmp_font.setPointSize(pointsize)
        painter.setFont(tmp_font)
        painter.drawText(rect, Qt.AlignmentFlag.AlignLeft, string)
        painter.restore()

    def draw_frame(self, color: QColor):
        """
        绘制一个外框
        """
        painter = self._painter
        painter.save()
        painter.translate(self.left_x + self.width / 2, self.left_y + self.height / 2)
        # 将xy坐标原点移到正中间
        painter.scale(self.width / 200.0, self.height / 100.0)
        # 修改xy坐标点与实际像素距离的对应关系，xy变为宽200 高100

        painter.setPen(color)
        painter.drawRect(-100, -50, 200, 100)
        painter.restore()

    def add_chart_line(
        self, data: list, color: QColor, y_min=0, y_max=50, show_dial=False
    ):
        """
        利用传入的数据，绘制折线图
        @data: 数据列表
        @color: 线条颜色
        @y_min: y轴原点值
        @y_max: y轴最大值
        """
        painter = self._painter
        painter.save()
        painter.setPen(color)
        painter.translate(self.left_x, self.left_y + self.height)
        painter.scale(self.width / len(data), 1)
        y_scale = self.height / (y_max - y_min)
        path = QPainterPath()
        path.moveTo(0, 0)
        for i in range(len(data)):
            if data[i] == 0:
                path.lineTo(i, 0)
            else:
                path.lineTo(i, -((data[i] - y_min)) * y_scale)
        painter.drawPath(path)

        # 绘制y轴刻度
        if show_dial:
            point_size = int(self.height / 6)
            tmp_font = QFont(painter.font())
            tmp_font.setPointSize(point_size)
            painter.setFont(tmp_font)
            rect = QRectF()
            rect.setHeight(self.height)
            rect.setWidth(self.width)
            rect.setX(int(point_size / 2))
            rect.setY(0 - point_size * 2)
            painter.drawText(rect, Qt.AlignmentFlag.AlignLeft, str(y_min))
            rect.setX(int(point_size / 2))
            rect.setY(0 - self.height)
            painter.drawText(rect, Qt.AlignmentFlag.AlignLeft, str(y_max))

        painter.restore()

    def __init__(
        self, window: QtWidgets.QMainWindow, painter: QPainter, label: QtWidgets.QLabel
    ):
        self.window = window
        self.width = label.width()
        self.height = label.height()
        self.left_x = label.pos().x()
        self.left_y = label.pos().y()
        label.hide()

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        self._painter = painter
