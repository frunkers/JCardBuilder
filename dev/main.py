import sys

from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from cassette import Cassette
from form import Form
from list_cassettes import ListCassettes


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 950, 800)
        self.setWindowTitle('Конструктор J-Card')
        self.setWindowIcon(QIcon('dev/accets/favicon.png'))
        self.pixmap_bg = QPixmap('dev/accets/bg.png')
        self.image_bg = QLabel(self)
        self.image_bg.resize(self.width(), self.height())
        self.image_bg.setPixmap(self.pixmap_bg)
        self.image_bg.setScaledContents(True)
        self.image_bg.setObjectName('image')
        self.cassette = Cassette(self)
        self.form = Form(self, self.cassette)
        self.list_cassettes = ListCassettes(self, self.form)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
