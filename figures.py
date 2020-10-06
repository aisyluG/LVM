from abc import ABC, abstractmethod
from accessify import protected
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QBrush, QColor

class Figure(ABC):
    def __init__(self, x:int, y:int, name:str):
        self._name = name
        self.x = x
        self.y = y
        self.enters = []
        self.outs = []
        self.checked = False
        self.connections = []

    @abstractmethod
    def paint(self, painter:QPainter):
        pass

    def getXY(self):
        return self.x, self.y

    def get_name(self):
        return self._name

    @abstractmethod
    def mouseInFigure(self, x, y):
        pass

    def check(self):
        if self.checked == True:
            self.checked = False
        else:
            self.checked = True

    def isChecked(self):
        return self.checked

    @abstractmethod
    def addConnection(self, figure):
        pass



class AndOrFigure(Figure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.r = 15
        self.brush = QBrush(Qt.lightGray, Qt.SolidPattern)

    def paint(self, painter):
        painter.setBrush(self.brush)
        try:
            for c in self.connections:
                x2, y2 = c.getXY()
                painter.drawLine(self.x, self.y, x2, y2)
            painter.drawEllipse(QPoint(self.x, self.y), self.r, self.r)
            painter.drawText(self.x - self.r, self.y - self.r, 2*self.r, 2*self.r, Qt.AlignCenter, self._name)
        except Exception:
            print(Exception.mro())

    def mouseInFigure(self, x, y):
        if (self.x - 2*self.r) <= x  and (self.x + 2*self.r) >= x and (self.y - 2*self.r) <= y and (self.y + 2*self.r) >= y:
            return True
        else:
            return False

    def addConnection(self, figure: Figure):
        if figure.__class__ == EventFigure:
            self.connections.append(figure)
            return True
        else:
            return False


class EventFigure(Figure):
    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = 40
        self.height = 30
        self.color = color
        self.brush = QBrush(self.color, Qt.SolidPattern)

    def paint(self, painter):
        # for c in self.connections:
        #     x2, y2 = c.getXY()
        #     painter.drawLine(self.x, self.y, x2, y2)
        painter.setBrush(self.brush)
        painter.drawRect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        painter.drawText(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height, Qt.AlignCenter, self._name)

    def mouseInFigure(self, x, y):
        if (self.x - self.width) <= x  and (self.x + self.width) >= x and (self.y - self.height) <= y and (self.y + self.height) >= y:
            return True
        else:
            return False

    def addConnection(self, figure: Figure):
        if figure.__class__ == AndOrFigure:
            self.connections.append(figure)
            return True
        else:
            return False

    def set_name(self, text:str):
        self._name = text

class IniEventFigure(EventFigure):
    def __init__(self, color, *args, **kwargs):
        super().__init__(color,*args, **kwargs)
        self.color = color
        self.probability = 0

    def setProbability(self, p):
        self.probability = p

    def paint(self, painter):
        super().paint(painter)
        painter.drawText(self.x+self.width/2, self.y + self.height/2, 25, 10, Qt.AlignCenter, str(self.probability))