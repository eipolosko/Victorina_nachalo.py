import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QPushButton

class window(QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        self.setWindowTitle('Simple')
        self.setGeometry(300, 300, 300, 220)

        self.new_text=QLabel(self)
        self.main_text = QLabel(self)
        self.main_text.setText("Это надпись")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()
        self.btn = QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText('Нажми на меня')
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText('Hello')
        self.new_text.move(100,50)
        self.new_text.adjustSize()



def application():
    app = QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    application()