from drawWidget import DrawWidget
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPalette, QColor, QPen
from figures import AndOrFigure, IniStateFigure
class DangerousState():
    def __init__(self):
        self.figures = []
        self.dang_state = None
        self.init_states = []
        self.paths = []
        self.risk = 0


    def paint(self, painter):
        for f in self.figures:
            if f.isChecked() == True:
                pen = QPen(Qt.black, 3, Qt.SolidLine)
                painter.setPen(pen)
                f.paint(painter)
                pen = QPen(Qt.black, 1, Qt.SolidLine)
                painter.setPen(pen)
            else:
                f.paint(painter)

    def clean(self):
        self.figures = [self.dang_state]
        self.init_states = []

    def computeConditionFunc(self):
        figure = self.dang_state.connections[0]
        conditions = calc(figure, [self.dang_state])
        print(conditions)
        self.paths = foundPaths(figure, [self.dang_state])
        probability = self.calcDangerProbability(self.paths)
        self.dang_state.setProbability(probability)
        return self.paths

    def calc_risk(self):
        print(self.dang_state.cost)
        self.risk = self.dang_state.probability*self.dang_state.cost
        return self.risk

    def calcDangerProbability(self, paths):
        P = 1
        for path in paths:
            p = 1
            for state in path:
                p = p*state.probability
            P = P * (1 - p)
        return 1 - P

def calc(root:AndOrFigure, checked=None):
    paths = 0
    if checked is None:
        checked = []
    checked.append(root)
    for x in root.connections:
        if x not in checked:
            checked.append(x)
            # если вершина - лист
            if x.isClass(IniStateFigure) == True:
                if root.get_name() == 'or':
                    paths += 1
            else: # промежуточное состояние
                for f in x.connections:
                    if f != root:
                        if paths == 0:
                            paths = calc(f, checked)
                        elif root.get_name() == 'or':
                            paths += calc(f, checked)
                        else:
                            paths *= calc(f, checked)
    if paths == 0:
        return 1
    else:
        return paths

def foundPaths(root:AndOrFigure, checked=None):
    paths = []
    if checked is None:
        checked = []
    checked.append(root)
    for x in root.connections:
        if x not in checked:
            checked.append(x)
            # если вершина не лист
            if x.isClass(IniStateFigure) == False:
                for f in x.connections:
                    if f != root:
                        p = foundPaths(f, checked)
                        if root.get_name() == 'or':
                            paths = paths + p
                        else:
                            if paths == []:
                                paths = [[]]
                            list = []
                            for s in p:
                                list = list + [i + s for i in paths]
                            paths = list
            else:
                if root.get_name() == 'or':
                    paths.append([x])
                else:
                    if paths == []:
                        paths = [[]]
                    paths = [i + [x] for i in paths]
    return paths



