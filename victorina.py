# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'victorina.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 746)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Obj_pict = QtWidgets.QLabel(self.centralwidget)
        self.Obj_pict.setGeometry(QtCore.QRect(30, 0, 551, 261))
        self.Obj_pict.setText("")
        self.Obj_pict.setPixmap(QtGui.QPixmap("../../OneDrive/Рабочий стол/викторина-стоковая-иллюстрация.jpg"))
        self.Obj_pict.setObjectName("Obj_pict")
        self.obj_pict2 = QtWidgets.QLabel(self.centralwidget)
        self.obj_pict2.setGeometry(QtCore.QRect(580, 20, 451, 391))
        self.obj_pict2.setText("")
        self.obj_pict2.setPixmap(QtGui.QPixmap("../../OneDrive/Рабочий стол/картинка викторина.jpg"))
        self.obj_pict2.setObjectName("obj_pict2")
        self.obj_Menu = QtWidgets.QTabWidget(self.centralwidget)
        self.obj_Menu.setGeometry(QtCore.QRect(40, 270, 691, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.obj_Menu.setFont(font)
        self.obj_Menu.setObjectName("obj_Menu")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(-40, 0, 721, 51))
        self.textEdit.setObjectName("textEdit")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(0, 60, 86, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(0, 90, 86, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 120, 86, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 150, 721, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_4.setGeometry(QtCore.QRect(0, 210, 86, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_5.setGeometry(QtCore.QRect(0, 250, 86, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_6.setGeometry(QtCore.QRect(0, 300, 86, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.obj_Menu.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.obj_Menu.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.obj_Menu.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.obj_Menu.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.obj_Menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_2.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_3.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_4.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_5.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_6.setText(_translate("MainWindow", "RadioButton"))
        self.obj_Menu.setTabText(self.obj_Menu.indexOf(self.tab), _translate("MainWindow", "Музыка"))
        self.obj_Menu.setTabText(self.obj_Menu.indexOf(self.tab_4), _translate("MainWindow", "Литература"))
        self.obj_Menu.setTabText(self.obj_Menu.indexOf(self.tab_3), _translate("MainWindow", "Питон"))
        self.obj_Menu.setTabText(self.obj_Menu.indexOf(self.tab_2), _translate("MainWindow", "Кино"))
        self.textEdit.setText(_translate("MainWindow", "Первый вопрос"))

    def add_function(self):
        self.radioButton.clicked.connect(lambda: self.write_number(self.obj0.text()))
        self.obj1.clicked.connect(lambda: self.write_number(self.obj1.text()))
        self.obj2.clicked.connect(lambda: self.write_number(self.obj2.text()))
        self.obj3.clicked.connect(lambda: self.write_number(self.obj3.text()))
        self.obj4.clicked.connect(lambda: self.write_number(self.obj4.text()))
        self.obj5.clicked.connect(lambda: self.write_number(self.obj5.text()))
        self.obj6.clicked.connect(lambda: self.write_number(self.obj6.text()))
        self.obj7.clicked.connect(lambda: self.write_number(self.obj7.text()))
        self.obj8.clicked.connect(lambda: self.write_number(self.obj8.text()))
        self.obj9.clicked.connect(lambda: self.write_number(self.obj9.text()))
        self.pushButton.clicked.connect(lambda: self.write_number(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: self.write_number(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.write_number(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.write_number(self.pushButton_4.text()))
        self.obj_equal.clicked.connect(self.results)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())