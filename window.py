# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1250, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(310, 0, 931, 685))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.andBt = QtWidgets.QToolButton(self.frame)
        self.andBt.setGeometry(QtCore.QRect(830, 50, 41, 31))
        self.andBt.setObjectName("andBt")
        self.orBt = QtWidgets.QToolButton(self.frame)
        self.orBt.setGeometry(QtCore.QRect(830, 10, 41, 31))
        self.orBt.setStyleSheet("")
        self.orBt.setObjectName("orBt")
        self.stateBt = QtWidgets.QToolButton(self.frame)
        self.stateBt.setGeometry(QtCore.QRect(830, 90, 41, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("state.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stateBt.setIcon(icon)
        self.stateBt.setIconSize(QtCore.QSize(30, 30))
        self.stateBt.setObjectName("stateBt")
        self.cursorBt = QtWidgets.QToolButton(self.frame)
        self.cursorBt.setGeometry(QtCore.QRect(830, 210, 41, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("cursor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cursorBt.setIcon(icon1)
        self.cursorBt.setIconSize(QtCore.QSize(41, 31))
        self.cursorBt.setObjectName("cursorBt")
        self.iniStateBt = QtWidgets.QToolButton(self.frame)
        self.iniStateBt.setGeometry(QtCore.QRect(830, 130, 41, 31))
        self.iniStateBt.setIconSize(QtCore.QSize(30, 30))
        self.iniStateBt.setObjectName("iniStateBt")
        self.dangStateBt = QtWidgets.QToolButton(self.frame)
        self.dangStateBt.setGeometry(QtCore.QRect(830, 170, 41, 31))
        self.dangStateBt.setIconSize(QtCore.QSize(30, 30))
        self.dangStateBt.setObjectName("dangStateBt")
        self.connectBt = QtWidgets.QToolButton(self.frame)
        self.connectBt.setGeometry(QtCore.QRect(830, 250, 41, 31))
        self.connectBt.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("connect.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connectBt.setIcon(icon2)
        self.connectBt.setIconSize(QtCore.QSize(30, 30))
        self.connectBt.setObjectName("connectBt")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setGeometry(QtCore.QRect(860, 450, 62, 22))
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.probLabel = QtWidgets.QLabel(self.frame)
        self.probLabel.setGeometry(QtCore.QRect(770, 450, 81, 21))
        self.probLabel.setObjectName("probLabel")
        self.computeDEPbt = QtWidgets.QPushButton(self.frame)
        self.computeDEPbt.setGeometry(QtCore.QRect(780, 550, 141, 41))
        self.computeDEPbt.setObjectName("computeDEPbt")
        self.cleanBt = QtWidgets.QToolButton(self.frame)
        self.cleanBt.setGeometry(QtCore.QRect(830, 290, 41, 31))
        self.cleanBt.setObjectName("cleanBt")
        self.delBt = QtWidgets.QToolButton(self.frame)
        self.delBt.setGeometry(QtCore.QRect(830, 330, 41, 31))
        self.delBt.setObjectName("delBt")
        self.dsCostBt = QtWidgets.QDoubleSpinBox(self.frame)
        self.dsCostBt.setGeometry(QtCore.QRect(860, 480, 62, 22))
        self.dsCostBt.setMaximum(1000.0)
        self.dsCostBt.setObjectName("dsCostBt")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(770, 480, 91, 20))
        self.label.setObjectName("label")
        self.saveBt = QtWidgets.QToolButton(self.frame)
        self.saveBt.setGeometry(QtCore.QRect(830, 370, 41, 31))
        self.saveBt.setObjectName("saveBt")
        self.openBt = QtWidgets.QToolButton(self.frame)
        self.openBt.setGeometry(QtCore.QRect(830, 410, 41, 31))
        self.openBt.setObjectName("openBt")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 384, 301, 301))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(3, 16, 291, 261))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 291, 361))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 251, 331))
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidget.setObjectName("listWidget")
        self.addDSbt = QtWidgets.QToolButton(self.groupBox_2)
        self.addDSbt.setGeometry(QtCore.QRect(260, 30, 27, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.addDSbt.setFont(font)
        self.addDSbt.setObjectName("addDSbt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ЛВМ"))
        self.andBt.setText(_translate("MainWindow", "AND"))
        self.orBt.setText(_translate("MainWindow", "OR"))
        self.stateBt.setToolTip(_translate("MainWindow", "Промежуточное событие"))
        self.stateBt.setText(_translate("MainWindow", "..."))
        self.cursorBt.setText(_translate("MainWindow", "..."))
        self.iniStateBt.setToolTip(_translate("MainWindow", "Инициирующее событие"))
        self.iniStateBt.setText(_translate("MainWindow", "ИС"))
        self.dangStateBt.setToolTip(_translate("MainWindow", "Опасное событие"))
        self.dangStateBt.setText(_translate("MainWindow", "ОС"))
        self.connectBt.setToolTip(_translate("MainWindow", "Соединение событий"))
        self.probLabel.setText(_translate("MainWindow", "Вероятность"))
        self.computeDEPbt.setToolTip(_translate("MainWindow", "Расчет вероятности реализации опасного состояния"))
        self.computeDEPbt.setText(_translate("MainWindow", "Рассчитать"))
        self.cleanBt.setText(_translate("MainWindow", "Clean"))
        self.delBt.setText(_translate("MainWindow", "Delete"))
        self.label.setText(_translate("MainWindow", "Стоимость ОС"))
        self.saveBt.setToolTip(_translate("MainWindow", "Сохранить опасное состояние в файл"))
        self.saveBt.setText(_translate("MainWindow", "Save"))
        self.openBt.setToolTip(_translate("MainWindow", "Загрузить опасное состояние из файла"))
        self.openBt.setText(_translate("MainWindow", "Open"))
        self.groupBox.setTitle(_translate("MainWindow", "Условие перехода в опасное состояние "))
        self.groupBox_2.setTitle(_translate("MainWindow", "Опасные состояния ресурса"))
        self.addDSbt.setToolTip(_translate("MainWindow", "Новое опасное состояние"))
        self.addDSbt.setText(_translate("MainWindow", "+"))
