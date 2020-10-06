from window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap, QKeyEvent
from PyQt5.QtCore import QRect, Qt
from drawWidget import DrawWidget
import sys
import figures

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.canvas = DrawWidget(self.ui.frame)
        self.ui.canvas.setGeometry(QRect(2, 2, self.ui.frame.width() - 160, self.ui.frame.height() - 6))
        palet = QPalette()
        palet.setColor(QPalette.Window, QColor('#ffffff'))
        palet.setColor(QPalette.Button, QColor('#ffffff'))
        self.ui.canvas.setPalette(palet)
        self.ui.canvas.setAutoFillBackground(True)
        # кнопки
        self.ui.andBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.orBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.cursorBt.setStyleSheet('background-color: blue;')
        self.ui.eventBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.iniEventBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.dangEventBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.connectBt.setStyleSheet(('background-color: #f0f0f0;'))


        # обработчики событий
        self.ui.andBt.clicked.connect(self.change_paintMode)
        self.ui.orBt.clicked.connect(self.change_paintMode)
        self.ui.eventBt.clicked.connect(self.change_paintMode)
        self.ui.cursorBt.clicked.connect(self.change_paintMode)
        self.ui.dangEventBt.clicked.connect(self.change_paintMode)
        self.ui.iniEventBt.clicked.connect(self.change_paintMode)
        self.ui.connectBt.clicked.connect(self.change_paintMode)
        self.ui.canvas.selectedChanged.connect(self.probabEnter)

        self.selectedEvent = None

    def change_paintMode(self):
        name = self.sender().objectName()
        self.ui.andBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.orBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.cursorBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.eventBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.dangEventBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.iniEventBt.setStyleSheet('background-color: #f0f0f0;')
        icon = QIcon()
        icon.addPixmap(QPixmap("connect.bmp"), QIcon.Normal, QIcon.Off)
        self.ui.connectBt.setIcon(icon)
        self.ui.connectBt.setStyleSheet(('background-color: #f0f0f0;'))
        if name == 'andBt':
            self.ui.canvas.setMode('and')
            self.ui.andBt.setStyleSheet('background-color: blue;')
        elif name == 'orBt':
            self.ui.canvas.setMode('or')
            self.ui.orBt.setStyleSheet('background-color: blue;')
        elif name == 'eventBt':
            self.ui.canvas.setMode('event')
            self.ui.eventBt.setStyleSheet('background-color: blue;')
        elif name == 'dangEventBt':
            self.ui.canvas.setMode('dang')
            self.ui.dangEventBt.setStyleSheet('background-color: blue;')
        elif name == 'iniEventBt':
            self.ui.canvas.setMode('ini')
            self.ui.iniEventBt.setStyleSheet('background-color: blue;')
        elif name == 'cursorBt':
            self.ui.canvas.setMode('cursor')
            self.ui.cursorBt.setStyleSheet('background-color: blue;')
        elif name == 'connectBt':
            self.ui.canvas.setMode('connect')
            icon = QIcon()
            icon.addPixmap(QPixmap("connect_active.bmp"), QIcon.Normal, QIcon.Off)
            self.ui.connectBt.setIcon(icon)
            self.ui.connectBt.setStyleSheet('background-color: blue;')

    def probabEnter(self, figure):
        if figure.__class__ == figures.IniEventFigure:
            self.ui.probLabel.setText(figure.get_name())
            self.selectedEvent = figure

    def keyReleaseEvent(self, a0: QKeyEvent):
        if self.selectedEvent is not None and a0.key() == Qt.Key_Return:
            p = self.ui.doubleSpinBox.text()
            self.selectedEvent.setProbability(p)
            self.ui.probLabel.setText('Вероятность')
            self.selectedEvent = None
            self.ui.canvas.update()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
