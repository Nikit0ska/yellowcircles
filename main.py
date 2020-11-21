import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.flag = False
        self.pushButton.clicked.connect(self.onClicked)


    def onClicked(self):
        self.flag = True
        self.update()


    def paintEvent(self, e):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawEllipse(qp)
            qp.end()


    def drawEllipse(self, qp):
        x = random.randint(0, 567)
        y = random.randint(0, 464)
        radius = random.randint(0, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MW = MyWidget()
    MW.show()
    sys.exit(app.exec())



