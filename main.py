# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from common import BuluoEntry


class Ui_Widget(object):
    buluoList = []

    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(548, 351)
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(370, 160, 54, 16))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 531, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.accountManageBtn_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.accountManageBtn_3.setObjectName("accountManageBtn_3")
        self.horizontalLayout_3.addWidget(self.accountManageBtn_3)
        self.buluoManageBtn_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buluoManageBtn_3.setObjectName("buluoManageBtn_3")
        self.horizontalLayout_3.addWidget(self.buluoManageBtn_3)
        self.targetUserBtn_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.targetUserBtn_3.setObjectName("targetUserBtn_3")
        self.horizontalLayout_3.addWidget(self.targetUserBtn_3)
        self.contentSettingBtn_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.contentSettingBtn_3.setObjectName("contentSettingBtn_3")
        self.horizontalLayout_3.addWidget(self.contentSettingBtn_3)
        self.softwareSettingBtn_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.softwareSettingBtn_3.setObjectName("softwareSettingBtn_3")
        self.horizontalLayout_3.addWidget(self.softwareSettingBtn_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(Widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 160, 81, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.buluoTableWidget = QtWidgets.QTableWidget(Widget)
        self.buluoTableWidget.setGeometry(QtCore.QRect(30, 140, 311, 161))
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
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(370, 200, 54, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(60, 90, 54, 16))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(Widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 200, 81, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.startSearch = QtWidgets.QPushButton(Widget)
        self.startSearch.setGeometry(QtCore.QRect(390, 250, 75, 23))
        self.startSearch.setObjectName("startSearch")
        self.addBuluoByNameBtn = QtWidgets.QPushButton(Widget)
        self.addBuluoByNameBtn.setGeometry(QtCore.QRect(200, 90, 61, 23))
        self.addBuluoByNameBtn.setObjectName("addBuluoByNameBtn")
        self.addBuluoByNameInput = QtWidgets.QLineEdit(Widget)
        self.addBuluoByNameInput.setGeometry(QtCore.QRect(120, 90, 61, 20))
        self.addBuluoByNameInput.setObjectName("addBuluoByNameInput")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)


    def addBuluoByNameBtnClicked(self):
        buluoName = self.addBuluoByNameInput.text()
        buluoId = buluoName
        curBuluo = BuluoEntry(buluoId, buluoName)
        self.buluoTableWidget.setRowCount(self.buluoList.__len__() + 1)
        self.buluoTableWidget.verticalHeader().setVisible(False);
        curPosItem = QTableWidgetItem(str(self.buluoList.__len__() + 1))
        self.buluoTableWidget.setItem(self.buluoList.__len__(), 0, curPosItem)
        buluoIdItem = QTableWidgetItem(buluoId)
        self.buluoTableWidget.setItem(self.buluoList.__len__(), 1, buluoIdItem)
        buluoNameItem = QTableWidgetItem(buluoName)
        self.buluoTableWidget.setItem(self.buluoList.__len__(), 2, buluoNameItem)

        self.buluoTableWidget.resizeRowsToContents();
        self.buluoList.append(curBuluo)
        self.buluoTableWidget.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label_2.setText(_translate("Widget", "起始页码"))
        self.accountManageBtn_3.setText(_translate("Widget", "账号管理"))
        self.buluoManageBtn_3.setText(_translate("Widget", "部落管理"))
        self.targetUserBtn_3.setText(_translate("Widget", "目标用户"))
        self.contentSettingBtn_3.setText(_translate("Widget", "内容设置"))
        self.softwareSettingBtn_3.setText(_translate("Widget", "软件设置"))
        item = self.buluoTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Widget", "序号"))
        item = self.buluoTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Widget", "部落名称"))
        item = self.buluoTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Widget", "部落bid"))
        self.label_3.setText(_translate("Widget", "结束页码"))
        self.label.setText(_translate("Widget", "新增部落"))
        self.startSearch.setText(_translate("Widget", "开始搜索"))
        self.addBuluoByNameBtn.setText(_translate("Widget", "加入"))
        self.addBuluoByNameBtn.clicked.connect(self.addBuluoByNameBtnClicked)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
    print()
