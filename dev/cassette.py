from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QLabel
from PyQt6.QtGui import QPixmap
from store import store


class Cassette(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        step = 4
        self.h = 101 * step
        self.w_back = 15 * step
        self.w_spine = 13 * step
        self.w_main = 65 * step
        self.initUI()
        self.update_content()
        self.update_styles()

    def initUI(self):
        self.cassette = QLabel(self.parent)
        self.cassette.move(50, 50)
        self.cassette.resize(self.w_back + self.w_spine + self.w_main, self.h)

        self.cassette_back = QLabel(self.parent)
        self.cassette_back.resize(self.w_back, self.h)
        self.cassette_back.move(50, 50)
        self.cassette_back.setObjectName('cassette_back')
        self.cassette_back.setStyleSheet(
            '#cassette_back {'
            'background-color: #f1f5f9;'
            'border-top: 1px solid #022c22;'
            'border-bottom: 1px solid #022c22;'
            'border-left: 1px solid #022c22;'
            '}'
        )

        self.cassette_spine = QLabel(self.cassette)
        self.cassette_spine.move(self.w_back, 0)
        self.cassette_spine.resize(self.w_spine, self.h)
        self.cassette_spine.setObjectName('cassette_spine')
        self.cassette_spine.setStyleSheet(
            '#cassette_spine {'
            'background-color: #e2e8f0;'
            'border-top: 1px solid #022c22;'
            'border-bottom: 1px solid #022c22;'
            'border-left: 1px solid #022c22;'
            '}'
        )

        self.cassette_main = QLabel(self.cassette)
        self.cassette_main.move(self.w_back + self.w_spine, 0)
        self.cassette_main.resize(self.w_main, self.h)
        self.cassette_main.setObjectName('cassette_main')
        self.cassette_main.setStyleSheet(
            '#cassette_main {'
            'background-color: #f1f5f9;'
            'border: 1px solid #022c22;'
            '}'
        )

        self.pixmap = QPixmap(store.state[store.active_cassette]['image-url'])
        self.image = QLabel(self.cassette_main)
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

        self.cassette_title = QLabel(self.cassette_main)
        self.cassette_title.setObjectName('cassette_title')
        self.cassette_title.setStyleSheet(
            '#cassette_title {'
            'font-family: monospace;'
            '}'
        )

        self.spine_text = QLabel(self.cassette_spine)
        self.spine_text.setObjectName('spine_text')
        self.spine_text.setStyleSheet(
            '#spine_text {'
            'font-size: 14px;'
            '}'
        )

        self.spine_text2 = QLabel(self.cassette_spine)
        self.spine_text2.setObjectName('spine_text2')
        self.spine_text2.setStyleSheet(
            '#spine_text2 {'
            'font-size: 8px;'
            '}'
        )

        self.back_text = QLabel(self.cassette_back)
        self.back_text.setObjectName('back_text')
        self.back_text.setStyleSheet(
            '#back_text {'
            'font-size: 12px;'
            'border: 1px solid #9ca3af;'
            'padding: 4px;'
            '}'
        )

        effect_cassette = QGraphicsDropShadowEffect()
        effect_cassette.setOffset(0, 0)
        effect_cassette.setBlurRadius(40)
        self.cassette.setGraphicsEffect(effect_cassette)

    def update_content(self):
        self.cassette_title.setText(store.state[store.active_cassette]['title'])
        self.spine_text.setText('\n'.join(list(store.state[store.active_cassette]['album'])))
        self.spine_text2.setText(store.state[store.active_cassette]['ser_number'])
        self.back_text.setText('\n'.join(list(store.state[store.active_cassette]['lable'])))
        self.pixmap.load(store.state[store.active_cassette]['image-url'])
        self.image.setPixmap(self.pixmap)

    def update_styles(self):
        self.parent.setStyleSheet(
            '#cassette_title, #spine_text, #spine_text2, #back_text {' +
            'color:' + store.state[store.active_cassette]['color'] + ';' +
            'font-style: ' + store.state[store.active_cassette]['style'] + ';' +
            'text-transform: ' + store.state[store.active_cassette]['transform'] + ';' +
            'font-weight: ' + store.state[store.active_cassette]['weight'] + ';' +
            '}' +
            '#cassette_title {' +
            'font-size: ' + store.state[store.active_cassette]['title-size'] + ';' +
            '}'
        )
        self.cassette_title.setGeometry(
            20, 272,
            self.cassette_title.sizeHint().width(),
            self.cassette_title.sizeHint().height()
        )
        self.spine_text.setGeometry(
            round((self.w_spine - self.spine_text.sizeHint().width()) / 2), 14,
            self.spine_text.sizeHint().width(),
            self.spine_text.sizeHint().height()
        )
        self.spine_text2.setGeometry(
            round((self.w_spine - self.spine_text2.sizeHint().width()) / 2), self.h - 30,
            self.spine_text2.sizeHint().width(),
            self.spine_text2.sizeHint().height()
        )
        self.back_text.setGeometry(
            round((self.w_back - self.back_text.sizeHint().width()) / 2),
            round((self.h - self.back_text.sizeHint().height()) / 2),
            self.back_text.sizeHint().width(),
            self.back_text.sizeHint().height()
        )
