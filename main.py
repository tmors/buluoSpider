# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from common import BuluoEntry


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 360)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 531, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.accountManageBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.accountManageBtn.setObjectName("accountManageBtn")
        self.horizontalLayout.addWidget(self.accountManageBtn)
        self.buluoManageBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buluoManageBtn.setObjectName("buluoManageBtn")
        self.horizontalLayout.addWidget(self.buluoManageBtn)
        self.targetUserBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.targetUserBtn.setObjectName("targetUserBtn")
        self.horizontalLayout.addWidget(self.targetUserBtn)
        self.contentSettingBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.contentSettingBtn.setObjectName("contentSettingBtn")
        self.horizontalLayout.addWidget(self.contentSettingBtn)
        self.softwareSettingBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.softwareSettingBtn.setObjectName("softwareSettingBtn")
        self.horizontalLayout.addWidget(self.softwareSettingBtn)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(50, 100, 54, 16))
        self.label.setObjectName("label")
        self.addBuluoByNameInput = QtWidgets.QLineEdit(self.centralWidget)
        self.addBuluoByNameInput.setGeometry(QtCore.QRect(110, 100, 61, 20))
        self.addBuluoByNameInput.setObjectName("addBuluoByNameInput")
        self.addBuluoByNameBtn = QtWidgets.QPushButton(self.centralWidget)
        self.addBuluoByNameBtn.setGeometry(QtCore.QRect(190, 100, 61, 23))
        self.addBuluoByNameBtn.setObjectName("addBuluoByNameBtn")
        self.buluoTableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.buluoTableWidget.setGeometry(QtCore.QRect(20, 150, 311, 161))
        self.buluoTableWidget.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.buluoTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.buluoTableWidget.setObjectName("buluoTableWidget")
        self.buluoTableWidget.setColumnCount(3)
        self.buluoTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        self.buluoTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.buluoTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.buluoTableWidget.setHorizontalHeaderItem(2, item)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(360, 170, 54, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(360, 210, 54, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 170, 81, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 210, 81, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.startSearch = QtWidgets.QPushButton(self.centralWidget)
        self.startSearch.setGeometry(QtCore.QRect(380, 260, 75, 23))
        self.startSearch.setObjectName("startSearch")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 532, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.addBuluoByNameBtn.click.connect(self.addBuluoByNameBtnClicked)

    def addBuluoByNameBtnClicked(self):
        buluoName = self.addBuluoByNameInput.text()
        buluoId = buluoName
        curBuluo = BuluoEntry(buluoId, buluoName)
        self.buluoList.append(curBuluo)

        curPosItem = QTableWidgetItem(self.buluoList.__len__())
        self.buluoTableWidget.setItem(self.buluoList.__len__(), 0, curPosItem)
        buluoIdItem = QTableWidgetItem(buluoId)
        self.buluoTableWidget.setItem(self.buluoList.__len__(), 1, buluoIdItem)
        buluoNameItem = QTableWidgetItem(buluoName)
        self.buluoTableWidget.setItem(self.buluoList.__len__(), 2, buluoNameItem)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.accountManageBtn.setText(_translate("MainWindow", "账号管理"))
        self.buluoManageBtn.setText(_translate("MainWindow", "部落管理"))
        self.targetUserBtn.setText(_translate("MainWindow", "目标用户"))
        self.contentSettingBtn.setText(_translate("MainWindow", "内容设置"))
        self.softwareSettingBtn.setText(_translate("MainWindow", "软件设置"))
        self.label.setText(_translate("MainWindow", "新增部落"))
        self.addBuluoByNameBtn.setText(_translate("MainWindow", "加入"))
        item = self.buluoTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.buluoTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "部落名称"))
        item = self.buluoTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "部落bid"))
        self.label_2.setText(_translate("MainWindow", "起始页码"))
        self.label_3.setText(_translate("MainWindow", "结束页码"))
        self.startSearch.setText(_translate("MainWindow", "开始搜索"))
