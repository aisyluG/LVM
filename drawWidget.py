from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtGui import QMouseEvent, QPaintEvent, QPainter, QColor, QPen, QBrush, QKeyEvent
from PyQt5.QtCore import Qt, QLine, QRect, pyqtSignal
from figures import Figure, AndOrFigure, EventFigure, IniEventFigure

class DrawWidget(QWidget):
    selectedChanged = pyqtSignal(Figure)
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.flag = 'cursor'
        self.figures = []
        self.checked_figure = None
        self.connection_line = None

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        x = event.x()
        y = event.y()
        mouseIn = [f.mouseInFigure(x, y) for f in self.figures]
        if x > 20 and x < self.width() - 40 and y > 15 and y < self.height() - 30:
            if True not in mouseIn:
                if self.flag == 'and' or self.flag == 'or':
                    figure = AndOrFigure(x, y, self.flag)
                    self.figures.insert(0, figure)
                elif self.flag == 'event':
                    figure = EventFigure(QColor('#ffa500'), x, y, self.flag)
                    self.figures.append(figure)
                elif self.flag == 'ini':
                    figure = IniEventFigure(Qt.yellow, x, y, self.flag)
                    self.figures.append(figure)
                elif self.flag == 'dang':
                    figure = EventFigure(Qt.red, x, y, self.flag)
                    self.figures.append(figure)
                # снимаем выделение
                if self.checked_figure is not None:
                    self.checked_figure.check()
                    self.checked_figure = None
            else: #if self.flag == 'cursor':
                index = mouseIn.index(True)
                self.figures[index].check()
                if self.checked_figure is not None:
                    self.checked_figure.check()
                self.checked_figure = self.figures[index]
                self.selectedChanged.emit(self.checked_figure)

        self.update()

    def mouseMoveEvent(self, mouseEvent):
        if self.flag == 'connect' and self.checked_figure is not None:
            x, y = self.checked_figure.getXY()
            self.connection_line = QLine(x, y, mouseEvent.x(), mouseEvent.y())
            self.update()

    def mouseReleaseEvent(self, mouseEvent):
        if self.flag == 'connect' and self.checked_figure is not None:
            mouseIn = [f.mouseInFigure(mouseEvent.x(), mouseEvent.y()) for f in self.figures]
            index = mouseIn.index(True)
            if index != -1 and self.checked_figure != self.figures[index]:
                self.checked_figure.addConnection(self.figures[index])
                self.figures[index].addConnection(self.checked_figure)
            self.connection_line = None
            self.update()

    def mouseDoubleClickEvent(self, mouseEvent):
        if self.checked_figure is not None and self.checked_figure.__class__ == EventFigure:
            x, y = self.checked_figure.getXY()
            self.input_ = QLineEdit(self)
            self.input_.setGeometry(QRect(x, y+5, 50, 22))
            self.input_.setObjectName("lineEdit")
            self.input_.show()
            text = self.input_.text()

            # self.update()
    def keyReleaseEvent(self, event: QKeyEvent):
        # Enter
        if event.key() == Qt.Key_Insert:
            text = self.input_.text()
            self.checked_figure.set_name(text)
            self.input_.hide()
            self.update()

    def paintEvent(self, event:QPaintEvent):
        super().paintEvent(event)
        painter = QPainter()
        painter.begin(self)
        for f in self.figures:
            if f.isChecked() == True:
                pen = QPen(Qt.black, 3, Qt.SolidLine)
                painter.setPen(pen)
                f.paint(painter)
                pen = QPen(Qt.black, 1, Qt.SolidLine)
                painter.setPen(pen)
            else:
                f.paint(painter)
        if self.connection_line is not None:
            painter.drawLine(self.connection_line)
        painter.end()

    def setMode(self, mode: str):
        self.flag = mode
