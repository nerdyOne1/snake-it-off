# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snake-it-off.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_Repeat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Repeat.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_Repeat.setObjectName("pushButton_Repeat")
        self.horizontalLayout_3.addWidget(self.pushButton_Repeat)
        self.pushButton_Random = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Random.setObjectName("pushButton_Random")
        self.horizontalLayout_3.addWidget(self.pushButton_Random)
        self.pushButton_Practice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Practice.setObjectName("pushButton_Practice")
        self.horizontalLayout_3.addWidget(self.pushButton_Practice)
        self.pushButton_Play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Play.setObjectName("pushButton_Play")
        self.horizontalLayout_3.addWidget(self.pushButton_Play)
        self.pushButton_Pause = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Pause.setObjectName("pushButton_Pause")
        self.horizontalLayout_3.addWidget(self.pushButton_Pause)
        self.label_Playtime = QtWidgets.QLabel(self.centralwidget)
        self.label_Playtime.setObjectName("label_Playtime")
        self.horizontalLayout_3.addWidget(self.label_Playtime)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_Search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.horizontalLayout_3.addWidget(self.pushButton_Search)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.horizontalLayout.addWidget(self.treeWidget)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Repeat.setText(_translate("MainWindow", "Repeat"))
        self.pushButton_Random.setText(_translate("MainWindow", "Random"))
        self.pushButton_Practice.setText(_translate("MainWindow", "Practice "))
        self.pushButton_Play.setText(_translate("MainWindow", "Play"))
        self.pushButton_Pause.setText(_translate("MainWindow", "Pause"))
        self.label_Playtime.setText(_translate("MainWindow", "0:00/0:00"))
        self.pushButton_Search.setText(_translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

