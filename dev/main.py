import sys

from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap, QIcon, QCursor
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from cassette import Cassette
from form import Form
from list_cassettes import ListCassettes
from form_info import FormInfo


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
        self.btn_info = QPushButton('О программе', self)
        self.btn_info.clicked.connect(self.btn_info_action)
        self.btn_info.setObjectName('btn_info')
        self.btn_info.setStyleSheet(
            '#btn_info {'
            'background: #d6d3d1;'
            'color: #022c22;'
            'border: 1px solid #022c22;'
            'padding: 0 4px;'
            'border-radius: 3px;'
            '}'
            '#btn_info:hover {'
            'background: #a8a29e;'
            '}'
        )
        self.btn_info.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_info.move(self.width() - 50 - self.btn_info.width() + 1, 600)
        self.form_info = FormInfo()

    def btn_info_action(self):
        self.form_info.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
