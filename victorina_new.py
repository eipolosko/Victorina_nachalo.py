# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'victorina_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
import random
conn = sqlite3.connect('table111')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS table111(id INTEGER PRIMARY KEY AUTOINCREMENT, Qwestion Text, answer_1 Text,answer_2 Text,answer_3 Text) ''')

# a=random.randint(0,9)
# b=random.randint(0,9)
l = [('Что такое питон?', 'язык программирования ', 'лекарство', 'животное'),
     ('Что такое list?', 'список ', 'множество', 'словарь'),
     ('Что такое range?', 'функция ', 'итератор', 'генератор')]
cursor.executemany('''INSERT INTO table111(Qwestion,answer_1,answer_2,answer_3) VALUES (?,?,?,?)''', l)
# conn.commit()
cursor.execute('''SELECT id FROM table111''')
k = cursor.fetchall()
r = random.choice(k)
print(*r)  # * используется для распаковки элемента из кортежа

cursor.execute('''SELECT Qwestion FROM table111 WHERE id=?''', (r))
oo = cursor.fetchall()
print(oo)
for i in oo:
    for j in i:
        print(j)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 688)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Obj_pict = QtWidgets.QLabel(self.centralwidget)
        self.Obj_pict.setGeometry(QtCore.QRect(10, 0, 551, 251))
        self.Obj_pict.setText("")
        self.Obj_pict.setPixmap(QtGui.QPixmap("../../OneDrive/Рабочий стол/викторина-стоковая-иллюстрация.jpg"))
        self.Obj_pict.setObjectName("Obj_pict")
        self.obj_pict2 = QtWidgets.QLabel(self.centralwidget)
        self.obj_pict2.setGeometry(QtCore.QRect(580, 20, 451, 391))
        self.obj_pict2.setText("")
        self.obj_pict2.setPixmap(QtGui.QPixmap("../../OneDrive/Рабочий стол/картинка викторина.jpg"))
        self.obj_pict2.setObjectName("obj_pict2")
        self.obj_Menu = QtWidgets.QTabWidget(self.centralwidget)
        self.obj_Menu.setGeometry(QtCore.QRect(0, 240, 691, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.obj_Menu.setFont(font)
        self.obj_Menu.setObjectName("obj_Menu")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(0, 60, 231, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(0, 90, 281, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 120, 301, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_1 = QtWidgets.QLabel(self.tab)
        self.label_1.setGeometry(QtCore.QRect(10, 0, 671, 51))
        self.label_1.setObjectName("label_1")
        self.labelRes1 = QtWidgets.QLabel(self.tab)
        self.labelRes1.setGeometry(QtCore.QRect(120, 170, 201, 21))
        self.labelRes1.setObjectName("labelRes1")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(391, 160, 261, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.obj_Menu.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.obj_Menu.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.obj_Menu.addTab(self.tab_4, "")
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
        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "Что такое map?"))
        self.radioButton.setText(_translate("MainWindow", "карта"))
        self.radioButton_2.setText(_translate("MainWindow", "функция"))
        self.radioButton_3.setText(_translate("MainWindow", "переменная"))
        self.labelRes1.setText(_translate("MainWindow", "11111"))
        self.obj_Menu.setTabText(self.obj_Menu.indexOf(self.tab), _translate("MainWindow", "Музыка"))
        self.obj_Menu.setTabText(self.obj_Menu.indexOf(self.tab_4), _translate("MainWindow", "Литература"))
        self.obj_Menu.setTabText(self.obj_Menu.indexOf(self.tab_3), _translate("MainWindow", "Питон"))
        self.obj_Menu.setTabText(self.obj_Menu.indexOf(self.tab_2), _translate("MainWindow", "Кино"))
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(391, 160, 261, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")

    def qwes2(self):
        _translate = QtCore.QCoreApplication.translate
        ar1 = self.qwes_rand()
        self.label_1.setText(_translate("MainWindow", ar1[0]))
        self.radioButton.setText(_translate("MainWindow", ar1[1]))
        self.radioButton_2.setText(_translate("MainWindow", ar1[2]))
        self.radioButton_3.setText(_translate("MainWindow", ar1[3]))

    def add_function(self):
        self.radioButton.clicked.connect(self.res_no)
        self.radioButton_2.clicked.connect(self.res_yes)
        self.radioButton_3.clicked.connect(self.res_no)
        self.commandLinkButton.clicked.connect(self.next_qwestions)

    def res_no(self):
        self.labelRes1.setText("ответ неверный")

    def res_yes(self):
        self.labelRes1.setText("ответ верный")

    def qwes_rand(self):
        ar=[]
        cursor.execute('''SELECT id FROM table111''')
        k = cursor.fetchall()
        r = random.choice(k)
        cursor.execute('''SELECT Qwestion,answer_1,answer_2,answer_3 FROM table111 WHERE id=?''', (r))
        oo = cursor.fetchall()
        for i in oo:
            for j in i:
                    ar.append(j)
        return ar

    def next_qwestions(self):
        self.hide_radio_buttons()
        self.show_radio_buttons()
        self.qwes2()

    def hide_radio_buttons(self):
        for btn in [self.radioButton, self.radioButton_2, self.radioButton_3]:
            btn.setAutoExclusive(False)
            btn.setChecked(False)
            btn.repaint()
            btn.setAutoExclusive(True)
            btn.hide()


    def show_radio_buttons(self):
        for btn in [self.radioButton, self.radioButton_2, self.radioButton_3]:
            btn.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
