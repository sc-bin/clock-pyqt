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
        painter.setPen(color)
        tmp_font = QFont(painter.font())
        tmp_font.setPointSize(pointsize)
        painter.setFont(tmp_font)
        painter.drawText(rect, Qt.AlignmentFlag.AlignLeft, string)

    def draw_frame(self, color: QColor):
        """
        绘制一个外框
        """
        painter = self._painter
        painter.setPen(color)
        painter.drawRect(-100, -50, 200, 100)

    def add_chart_line(self, data: list, color: QColor):
        """
        利用传入的数据，绘制折线图
        """
        painter = self._painter

        painter.setPen(color)
        path = QPainterPath()
        path.moveTo(-100, 50)
        for i in range(len(data)):
            path.lineTo(-100 + i * 2, (-data[i] * 2) + 50)
        painter.drawPath(path)

    def __init__(
        self, window: QtWidgets.QMainWindow, painter: QPainter, label: QtWidgets.QLabel
    ):
        self.window = window
        self.width = label.width()
        self.height = label.height()
        self.left_x = label.pos().x()
        self.left_y = label.pos().y()
        label.hide()

        # 将xy坐标原点移到正中间
        painter.translate(self.left_x + self.width / 2, self.left_y + self.height / 2)
        # 修改xy坐标点与实际像素距离的对应关系，xy变为宽200 高100
        painter.scale(self.width / 200.0, self.height / 100.0)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        self._painter = painter
