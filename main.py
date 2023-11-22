from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.painte = False

    def paintEvent(self, event):
        if self.painte:
            paint = QPainter()
            paint.begin(self)
            for k in range(5):
                # optionally fill each circle yellow
                paint.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                rad = random.randint(0, 100)
                paint.drawEllipse(random.randint(0, 300), random.randint(0, 200), rad, rad)
            paint.end()
        self.painte = False

    def run(self):
        self.painte = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())