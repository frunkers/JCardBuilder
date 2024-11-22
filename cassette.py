from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QLabel
from PyQt6.QtGui import QPixmap


class Cassette(QWidget):
    def __init__(self, state):
        super().__init__()
        self.state = state
        step = 4
        self.h = 101 * step
        self.w_back = 15 * step
        self.w_spine = 13 * step
        self.w_main = 65 * step
        self.initUI()

    def initUI(self):
        self.pixmap_bg = QPixmap('bg.png')
        self.image_bg = QLabel(self)
        self.image_bg.resize(self.width(), self.height())
        self.image_bg.setPixmap(self.pixmap_bg)
        self.image_bg.setScaledContents(True)
        self.image_bg.setObjectName('image')

        self.cassete = QLabel(self)
        self.cassete.move(50, 50)
        self.cassete.resize(self.w_back + self.w_spine + self.w_main, self.h)

        self.cassete_back = QLabel(self)
        self.cassete_back.resize(self.w_back, self.h)
        self.cassete_back.move(50, 50)
        self.cassete_back.setObjectName('cassete_back')
        self.cassete_back.setStyleSheet(
            '#cassete_back {'
            'background-color: #f1f5f9;'
            'border-top: 1px solid #022c22;'
            'border-bottom: 1px solid #022c22;'
            'border-left: 1px solid #022c22;'
            '}'
        )

        self.cassete_spine = QLabel(self.cassete)
        self.cassete_spine.move(self.w_back, 0)
        self.cassete_spine.resize(self.w_spine, self.h)
        self.cassete_spine.setObjectName('cassete_spine')
        self.cassete_spine.setStyleSheet(
            '#cassete_spine {'
            'background-color: #e2e8f0;'
            'border-top: 1px solid #022c22;'
            'border-bottom: 1px solid #022c22;'
            'border-left: 1px solid #022c22;'
            '}'
        )

        self.cassete_main = QLabel(self.cassete)
        self.cassete_main.move(self.w_back + self.w_spine, 0)
        self.cassete_main.resize(self.w_main, self.h)
        self.cassete_main.setObjectName('cassete_main')
        self.cassete_main.setStyleSheet(
            '#cassete_main {'
            'background-color: #f1f5f9;'
            'border: 1px solid #022c22;'
            '}'
        )

        self.pixmap = QPixmap('default.jpg')
        self.image = QLabel(self.cassete_main)
        self.image.resize(self.w_main, self.w_main)
        self.image.setPixmap(self.pixmap)
        self.image.setScaledContents(True)
        self.image.setObjectName('image')
        self.image.setStyleSheet(
            '#image {'
            'border: 1px solid #022c22;'
            'border-bottom: none;'
            '}'
        )

        self.cassete_title = QLabel(self.cassete_main)
        self.cassete_title.setObjectName('cassete_title')
        self.cassete_title.setStyleSheet(
            '#cassete_title {'
            'font-size: 28px;'
            'font-family: monospace;'
            '}'
        )

        self.spine_text = QLabel(self.cassete_spine)
        self.spine_text.setObjectName('spine_text')
        self.spine_text.setStyleSheet(
            '#spine_text {'
            'font-size: 14px;'
            '}'
        )

        self.spine_text2 = QLabel(self.cassete_spine)
        self.spine_text2.setObjectName('spine_text2')
        self.spine_text2.setStyleSheet(
            '#spine_text2 {'
            'font-size: 8px;'
            '}'
        )

        self.back_text = QLabel(self.cassete_back)
        self.back_text.setObjectName('back_text')
        self.back_text.setStyleSheet(
            '#back_text {'
            'font-size: 12px;'
            'border: 1px solid #9ca3af;'
            'padding: 4px;'
            '}'
        )

        effect_cassete = QGraphicsDropShadowEffect()
        effect_cassete.setOffset(0, 0)
        effect_cassete.setBlurRadius(40)
        self.cassete.setGraphicsEffect(effect_cassete)

    def update_content(self):
        self.cassete_title.setText(self.state['title'])
        self.cassete_title.move(20, 272)
        self.spine_text.setText(''.join(list(map(lambda x: x + '\n', self.state['album'])))[:-1])
        self.spine_text.move(round((self.w_spine - self.spine_text.sizeHint().width()) / 2), 14)
        self.spine_text2.setText(self.state['ser_number'])
        self.spine_text2.move(round((self.w_spine - self.spine_text2.sizeHint().width()) / 2), self.h - 30)
        self.back_text.setText(''.join(list(map(lambda x: x + '\n', self.state['lable'])))[:-1])
        self.back_text.move(
            round((self.w_back - self.back_text.sizeHint().width()) / 2),
            round((self.h - self.back_text.sizeHint().height()) / 2)
        )
