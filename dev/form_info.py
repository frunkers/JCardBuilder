from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPixmap, QIcon


class FormInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 600, 300)
        self.setWindowTitle('О программе')
        self.setWindowIcon(QIcon('dev/accets/favicon-about.png'))
        self.pixmap_bg_about = QPixmap('dev/accets/bg-about.jpg')
        self.image_bg_about = QLabel(self)
        self.image_bg_about.resize(self.width(), self.height())
        self.image_bg_about.setPixmap(self.pixmap_bg_about)
        self.image_bg_about.setScaledContents(True)
        self.image_bg_about.setObjectName('image-about')
        self.info = QLabel(
            '"Конструктор J Card" - программа для создания кассетных вкладышей.\n'
            'Жикарды можно сохранить, открыть после закрытия программы.', self
        )
        self.info.setObjectName('info')
        self.info.setStyleSheet(
            '#info {'
            'color: white;'
            'font-size: 16px;'
            '}'
        )
        self.info.move(44, 30)
        self.pixmap_jcard = QPixmap('dev/accets/jcard.jpg')
        self.image_jcard = QLabel(self)
        self.image_jcard.setPixmap(self.pixmap_jcard)
        self.image_jcard.resize(round(160 * 1355 / 633), 160)
        self.image_jcard.setScaledContents(True)
        self.image_jcard.setObjectName('image-jcard')
        self.image_jcard.move(44, 100)
