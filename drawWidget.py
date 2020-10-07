from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtGui import QMouseEvent, QPaintEvent, QPainter, QColor, QPen, QBrush, QKeyEvent
from PyQt5.QtCore import Qt, QLine, QRect, pyqtSignal
from figures import Figure, AndOrFigure, StateFigure, IniStateFigure, DangStateFigure


class DrawWidget(QWidget):
    selectedChanged = pyqtSignal(Figure)
    dang_stateRenamed = pyqtSignal(str)
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.flag = 'cursor'
        # self.figures = []
        # self.dang_state = None
        # self.init_states = []
        self.dang_state = None
        self.checked_figure = None
        self.connection_line = None

    def setState(self, state):
        self.dang_state = state
        self.checked_figure = None
        self.connection_line = None

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        x = event.x()
        y = event.y()
        mouseIn = [f.mouseInFigure(x, y) for f in self.dang_state.figures]
        if x > 20 and x < self.width() - 40 and y > 15 and y < self.height() - 30:
            if True not in mouseIn:
                if self.flag == 'and' or self.flag == 'or':
                    figure = AndOrFigure(x, y, self.flag)
                    # self.figures.insert(0, figure)
                    self.dang_state.figures.insert(0, figure)
                elif self.flag == 'state':
                    figure = StateFigure(QColor('#ffa500'), x, y, self.flag)
                    # self.figures.append(figure)
                    self.dang_state.figures.append(figure)
                elif self.flag == 'ini':
                    figure = IniStateFigure(Qt.yellow, x, y, self.flag + str(len(self.dang_state.init_states)))
                    # self.figures.append(figure)
                    # self.init_states.append(figure)
                    self.dang_state.figures.append(figure)
                    self.dang_state.init_states.append(figure)
                elif self.flag == 'dang':
                    if self.dang_state.dang_state is None:
                        figure = DangStateFigure(Qt.red, x, y, self.flag)
                        self.dang_state.figures.append(figure)
                        self.dang_state.dang_state = figure
                # снимаем выделение
                if self.checked_figure is not None:
                    self.checked_figure.check()
                    self.checked_figure = None
                    self.selectedChanged.emit(AndOrFigure(1, 1, 'q'))
            else: #if self.flag == 'cursor':
                index = mouseIn.index(True)
                self.dang_state.figures[index].check()
                if self.checked_figure is not None:
                    self.checked_figure.check()
                self.checked_figure = self.dang_state.figures[index]
                self.selectedChanged.emit(self.checked_figure)
        self.update()

    def mouseMoveEvent(self, mouseEvent):
        if self.flag == 'connect' and self.checked_figure is not None:
            x, y = self.checked_figure.getXY()
            self.connection_line = QLine(x, y, mouseEvent.x(), mouseEvent.y())
            self.update()

    def mouseReleaseEvent(self, mouseEvent):
        if self.flag == 'connect' and self.checked_figure is not None:
            mouseIn = [f.mouseInFigure(mouseEvent.x(), mouseEvent.y()) for f in self.dang_state.figures]
            try:
                index = mouseIn.index(True)
                if self.checked_figure != self.dang_state.figures[index]:
                    self.checked_figure.addConnection(self.dang_state.figures[index])
                    self.dang_state.figures[index].addConnection(self.checked_figure)
            except:
                pass
            self.connection_line = None
            self.update()

    def mouseDoubleClickEvent(self, mouseState):
        if self.checked_figure is not None and self.checked_figure.isClass(StateFigure) == True:
            x, y = self.checked_figure.getXY()
            self.input_ = QLineEdit(self)
            self.input_.setGeometry(QRect(x, y+5, 50, 22))
            self.input_.setObjectName("lineEdit")
            self.input_.show()
            text = self.input_.text()

            # self.update()

    def keyReleaseEvent(self, event: QKeyEvent):
        # Enter
        if event.key() == Qt.Key_Return:
            text = self.input_.text()
            if text != '':
                self.checked_figure.set_name(text)
                if self.checked_figure.isClass(DangStateFigure) == True:
                    self.dang_stateRenamed.emit(text)
            self.input_.hide()
            self.update()

    def paintEvent(self, event:QPaintEvent):
        super().paintEvent(event)
        painter = QPainter()
        painter.begin(self)
        self.dang_state.paint(painter)
        if self.connection_line is not None:
            painter.drawLine(self.connection_line)
        painter.end()

    def setMode(self, mode: str):
        self.flag = mode

    def clean(self):
        self.dang_state.clean()
        self.checked_figure = None
        self.connection_line = None
        self.update()

    def computeConditionFunc(self):
        # figure = self.dang_state.connections[0]
        # conditions = calc(figure, [self.dang_state])
        # print(conditions)
        # paths = foundPaths(figure, [self.dang_state])
        paths = self.dang_state.computeConditionFunc()
        func = self.pathsToFunc(paths) + f'<br> P = {self.dang_state.dang_state.probability}'
        risk = f'<br> Риск от реализации текущего опасного состояния равен {self.dang_state.calc_risk()}'
        self.update()
        return func + risk

    def pathsToFunc(self, paths):
        func = 'f = '
        for path in paths:
            p = '('
            for state in path:
                p += f'{state.get_name()} <b>and</b> '
            p = p.rstrip('<b>and</b> ')
            p += ') <b>or</b>'
            func += p
        func = func.rstrip('<b>or</b>')
        func += '<br>P(f=1) = 1 - ('
        for path in paths:
            p = '(1 - '
            for state in path:
                p += f'<b>{state.get_name()}</b>*'
            p = p.rstrip('*')
            p += ')'
            func += p
        func += ')'
        print(func)
        print(len(paths))
        return (func)

    def delCurrent(self):
        if self.checked_figure.isClass(DangStateFigure) == False:
            self.dang_state.figures.remove(self.checked_figure)
            for s in self.checked_figure.connections:
                s.delConnection(self.checked_figure)
            self.checked_figure = None
            self.update()

    def load(self, filename):
        self.clean()
        self.dang_state.figures = []
        self.dang_state.dang_state = None
        figures = []
        with open(filename, 'r', encoding='utf-8') as file:
            line = ''
            flag = file.readline()
            while flag != '':
                print('line', line)
                figure = None
                line = flag.rstrip('\n').split(',')
                connections = file.readline().rstrip('\n').split(':')[1].split(',')
                if line[0].split()[1] == 'or' or line[0].split()[1] == 'and':
                    figure = AndOrFigure(int(line[1]), int(line[2]), line[3])
                elif line[0].split()[1] == 'StateFigure':
                   figure = StateFigure(QColor('#ffa500'), int(line[1]), int(line[2]), line[3])
                elif line[0].split()[1] == 'IniStateFigure':
                    figure = IniStateFigure(Qt.yellow, int(line[1]), int(line[2]), line[3])
                    p = float(file.readline().rstrip('\n').split(':')[1])
                    figure.setProbability(p)
                elif line[0].split()[1] == 'DangStateFigure':
                    figure = DangStateFigure(Qt.red, int(line[1]), int(line[2]), line[3])
                    p = float(file.readline().rstrip('\n').split(':')[1])
                    figure.setProbability(p)
                    c = float(file.readline().rstrip('\n').split(':')[1])
                    figure.setCost(c)
                    self.dang_state.dang_state = figure
                figures.append((figure, connections))
                self.dang_state.figures.append(figure)
                flag = file.readline()
            for f, c in figures:
                print('f', f)
                for i in c:
                    f.addConnection(self.dang_state.figures[int(i) - 1])
        self.update()




    def save(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for i, state in enumerate(self.dang_state.figures):
                file.write(f'{i+1} {state.__str__()},{state.x},{state.y},{state.get_name()}\n')
                file.write('Connections:' + ','.join([str(self.dang_state.figures.index(x) + 1) for x in state.connections])
                           + '\n')
                if state.isClass(IniStateFigure):
                    file.write(f'Probability:{state.probability}\n')
                elif state.isClass(DangStateFigure):
                    file.write(f'Probability:{state.probability}\n')
                    file.write(f'Cost:{state.cost}\n')





