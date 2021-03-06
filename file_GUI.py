# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'File_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 453)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 100, 131, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 190, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 120, 301, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 180, 301, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 240, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 120, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 180, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 340, 72, 15))
        self.label_3.setObjectName("label_3")
        self.product_quantity = QtWidgets.QLineEdit(self.centralwidget)
        self.product_quantity.setGeometry(QtCore.QRect(220, 330, 201, 31))
        self.product_quantity.setObjectName("product_quantity")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 26))
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
        self.label.setText(_translate("MainWindow", "文件"))
        self.label_2.setText(_translate("MainWindow", "文件"))
        self.pushButton.setText(_translate("MainWindow", "提交"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.pushButton_3.setText(_translate("MainWindow", "浏览"))
        self.pushButton_4.setText(_translate("MainWindow", "浏览"))
        self.label_3.setText(_translate("MainWindow", "产品种类"))
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.open)
        self.pushButton_4.clicked.connect(self.open)
        self.pushButton.clicked.connect(self.submit)

    """
        获取文件路径
    """
    def open(self):
        _translate = QtCore.QCoreApplication.translate
        directory1 = QFileDialog.getOpenFileName(None, '选取文件', './')
        print(directory1)
        path = directory1[0]
        sender = MainWindow.sender()
        if (sender.objectName() == 'pushButton_3'):
            self.lineEdit.setText(path)
        elif (sender.objectName() == 'pushButton_4'):
            self.lineEdit_2.setText(path)

    """
        通过路径读取文件,放回读取的文件
    """
    def read_file(self, path):
        if path is not None:
            with open(file=path, mode='r+', encoding='utf-8') as file:
                file = file.read()
        return file
    """
        读取出两个文件
        product_quantity:产品数量输出框
    """
    def submit(self):
        path_first = self.lineEdit.text()
        path_second = self.lineEdit_2.text()
        if path_first is not None:
            file_first = self.read_file(path_first)#取出第一个文件
            print(file_first)
        if path_second is not None:
            file_second = self.read_file(path_second)#取出第二个文件
            print(file_second)
        self.product_quantity.setText("产品数量")#输出产品数量
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import pics_ui_rc # 导入添加的资源（根据实际情况填写文件名）
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
