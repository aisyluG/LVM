from window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap, QKeyEvent
from PyQt5.QtCore import QRect, Qt, QModelIndex
from drawWidget import DrawWidget
from dangerous_state import DangerousState
import sys
import figures

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.canvas = DrawWidget(self.ui.frame)
        self.ui.canvas.setGeometry(QRect(2, 2, self.ui.frame.width() - 165, self.ui.frame.height() - 6))
        palet = QPalette()
        palet.setColor(QPalette.Window, QColor('#ffffff'))
        palet.setColor(QPalette.Button, QColor('#ffffff'))
        self.ui.canvas.setPalette(palet)
        self.ui.canvas.setAutoFillBackground(True)

        ds = DangerousState()
        self.dangStates = [ds]
        self.ui.canvas.setState(ds)
        self.ui.listWidget.addItem('dangerous state 1')
        self.ui.listWidget.setCurrentRow(0)

        # кнопки
        self.ui.andBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.orBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.cursorBt.setStyleSheet('background-color: blue;')
        self.ui.stateBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.iniStateBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.dangStateBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.connectBt.setStyleSheet(('background-color: #f0f0f0;'))
        self.ui.cleanBt.setStyleSheet(('background-color: #f0f0f0;'))
        self.ui.delBt.setStyleSheet(('background-color: #f0f0f0;'))
        self.ui.addDSbt.setStyleSheet(('background-color: #f0f0f0;'))
        self.ui.saveBt.setStyleSheet(('background-color: #f0f0f0;'))
        self.ui.openBt.setStyleSheet(('background-color: #f0f0f0;'))

        # обработчики событий
        self.ui.andBt.clicked.connect(self.change_paintMode)
        self.ui.orBt.clicked.connect(self.change_paintMode)
        self.ui.stateBt.clicked.connect(self.change_paintMode)
        self.ui.cursorBt.clicked.connect(self.change_paintMode)
        self.ui.dangStateBt.clicked.connect(self.change_paintMode)
        self.ui.iniStateBt.clicked.connect(self.change_paintMode)
        self.ui.connectBt.clicked.connect(self.change_paintMode)
        self.ui.canvas.selectedChanged.connect(self.probabEnter)
        self.ui.computeDEPbt.clicked.connect(self.computing)
        self.ui.cleanBt.clicked.connect(self.cleancanvas)
        self.ui.addDSbt.clicked.connect(self.addNewDstate)
        self.ui.listWidget.currentItemChanged.connect(self.stateChanged)
        self.ui.canvas.dang_stateRenamed.connect(self.renameState)
        self.ui.delBt.clicked.connect(self.delCurrent)
        self.ui.openBt.clicked.connect(self.open)
        self.ui.saveBt.clicked.connect(self.save)

        self.selectedState = None


    def renameState(self, text):
        index = self.ui.listWidget.currentIndex()
        self.ui.listWidget.item(index.row()).setText(text)

    def delCurrent(self):
        self.ui.canvas.delCurrent()

    def stateChanged(self):
        index = self.ui.listWidget.currentIndex()
        self.ui.canvas.setState(self.dangStates[index.row()])
        self.ui.canvas.update()

    def addNewDstate(self):
        c = self.ui.listWidget.count()
        self.ui.listWidget.addItem(f'dangerous state {c + 1}')
        # try:
        #     self.ui.listWidget.setCurrentRow(c)
        # except Exception:
        #     print(Exception.mro())
        item = DangerousState()
        self.dangStates.append(item)
        self.ui.canvas.setState(item)
        self.ui.canvas.update()
        self.ui.listWidget.setCurrentRow(c)

    def change_paintMode(self):
        name = self.sender().objectName()
        self.ui.andBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.orBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.cursorBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.stateBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.dangStateBt.setStyleSheet('background-color: #f0f0f0;')
        self.ui.iniStateBt.setStyleSheet('background-color: #f0f0f0;')
        icon = QIcon()
        icon.addPixmap(QPixmap("D:/ucheba/4 курс/теория_принятия_решений/LVM/connect.bmp"), QIcon.Normal, QIcon.Off)
        self.ui.connectBt.setIcon(icon)
        self.ui.connectBt.setStyleSheet(('background-color: #f0f0f0;'))
        if name == 'andBt':
            self.ui.canvas.setMode('and')
            self.ui.andBt.setStyleSheet('background-color: blue;')
        elif name == 'orBt':
            self.ui.canvas.setMode('or')
            self.ui.orBt.setStyleSheet('background-color: blue;')
        elif name == 'stateBt':
            self.ui.canvas.setMode('state')
            self.ui.stateBt.setStyleSheet('background-color: blue;')
        elif name == 'dangStateBt':
            self.ui.canvas.setMode('dang')
            self.ui.dangStateBt.setStyleSheet('background-color: blue;')
        elif name == 'iniStateBt':
            self.ui.canvas.setMode('ini')
            self.ui.iniStateBt.setStyleSheet('background-color: blue;')
        elif name == 'cursorBt':
            self.ui.canvas.setMode('cursor')
            self.ui.cursorBt.setStyleSheet('background-color: blue;')
        elif name == 'connectBt':
            self.ui.canvas.setMode('connect')
            icon = QIcon()
            icon.addPixmap(QPixmap("D:/ucheba/4 курс/теория_принятия_решений/LVM/connect_active.bmp"), QIcon.Normal, QIcon.Off)
            self.ui.connectBt.setIcon(icon)
            self.ui.connectBt.setStyleSheet('background-color: blue;')

    def probabEnter(self, figure):
        self.selectedState = figure
        if figure is not None and figure.isClass(figures.IniStateFigure):
            self.ui.probLabel.setText(figure.get_name())

    def keyReleaseEvent(self, a0: QKeyEvent):
        if a0.key() == Qt.Key_Return:
            c = self.ui.dsCostBt.value()
            self.ui.canvas.dang_state.dang_state.setCost(c)
            if self.selectedState is not None and self.selectedState.isClass(figures.IniStateFigure):
                p = self.ui.doubleSpinBox.value()
                self.selectedState.setProbability(p)
                self.ui.probLabel.setText('Вероятность')
                self.selectedState = None
                self.ui.canvas.update()

    def computing(self):
        text = self.ui.canvas.computeConditionFunc()
        self.ui.textEdit.setHtml(text)

    def cleancanvas(self):
        self.selectedState = None
        self.ui.canvas.clean()

    def open(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Загрузка данных об опасном состоянии',
                                                            '/danger_state.txt',
                                                            'Текстовый документ (*.txt)')
        if _ == 'Текстовый документ (*.txt)':
            self.ui.canvas.load(filename)

    def save(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Сохранение данных об опасном состоянии',
                                                            '/danger_state.txt',
                                                            'Текстовый документ (*.txt)')
        if _ == 'Текстовый документ (*.txt)':
            self.ui.canvas.save(filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
