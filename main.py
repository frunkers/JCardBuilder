import sys

from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QRadioButton, QVBoxLayout, \
    QWidget, QCheckBox


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 1000, 800)
        self.setWindowTitle('Конструктор J-Card')
        step = 4
        h = 101 * step
        w_back = 15 * step
        w_spine = 13 * step
        w_main = 65 * step
        self.cassete = QLabel(self)
        self.cassete.move(50, 50)
        self.cassete.resize(w_back + w_spine + w_main, h)

        self.cassete_back = QLabel(self)
        self.cassete_back.resize(w_back, h)
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
        self.cassete_spine.move(w_back, 0)
        self.cassete_spine.resize(w_spine, h)
        self.cassete_spine.setObjectName('cassete_spine')
        self.cassete_spine.setStyleSheet(
            '#cassete_spine {'
            'background-color: #f1f5f9;'
            'border-top: 1px solid #022c22;'
            'border-bottom: 1px solid #022c22;'
            'border-left: 1px solid #022c22;}'
        )

        self.cassete_main = QLabel(self.cassete)
        self.cassete_main.move(w_back + w_spine, 0)
        self.cassete_main.resize(w_main, h)
        self.cassete_main.setObjectName('cassete_main')
        self.cassete_main.setStyleSheet(
            '#cassete_main {'
            'background-color: #f1f5f9;'
            'border: 1px solid #022c22;}'
        )

        self.pixmap = QPixmap('default.jpg')
        self.image = QLabel(self.cassete_main)
        self.image.move(0, 0)
        self.image.resize(w_main, w_main)
        self.image.setPixmap(self.pixmap)
        self.image.setScaledContents(True)
        self.image.setObjectName('image')
        self.image.setStyleSheet(
            '#image {'
            'border: 1px solid #022c22;'
            'border-bottom: none;}'
        )

        self.cassete_title = QLabel('PILLBOX', self.cassete_main)
        self.cassete_title.setObjectName('cassete_title')
        self.cassete_title.setStyleSheet(
            '#cassete_title {'
            'font-size: 28px;'
            'font-weight: 700;'
            'font-family: monospace;'
            '}'
        )
        self.cassete_title.move(20, 272)

        t = 'KOMM NIGHT REIN'
        t = ''.join(list(map(lambda x: x + '\n', t)))[:-1]
        self.spine_text = QLabel(t, self.cassete_spine)
        self.spine_text.setObjectName('spine_text')
        self.spine_text.setStyleSheet(
            '#spine_text {'
            'font-size: 14px;'
            '}'
        )
        self.spine_text.move(round((w_spine - self.spine_text.sizeHint().width()) / 2), 10)

        t2 = '#TMPL003'
        self.spine_text2 = QLabel(t2, self.cassete_spine)
        self.spine_text2.setObjectName('spine_text2')
        self.spine_text2.setStyleSheet(
            '#spine_text2 {'
            'font-size: 8px;'
            'font-weight: 700;'
            '}'
        )
        self.spine_text2.move(round((w_spine - self.spine_text2.sizeHint().width()) / 2), h - 30)

        t3 = 'TEMPLE DRIVE'
        t3 = ''.join(list(map(lambda x: x + '\n', t3)))[:-1]
        self.spine_text3 = QLabel(t3, self.cassete_back)
        self.spine_text3.setObjectName('spine_text3')
        self.spine_text3.setStyleSheet(
            '#spine_text3 {'
            'font-size: 12px;'
            'border: 1px solid #777;'
            'padding: 4px;'
            '}'
        )
        self.spine_text3.move(
            round((w_back - self.spine_text3.sizeHint().width()) / 2),
            round((h - self.spine_text3.sizeHint().height()) / 2)
        )

        self.form = QLabel(self)
        self.form.move(500, 50)
        self.form.setObjectName('form')
        self.form.resize(400, 400)
        self.setStyleSheet(
            '#form {'
            'background: #d4d4d8;'
            'border-radius: 6px;'
            '}'
        )
        self.form.setStyleSheet(
            '#radio-el {'
            'color: #022c22;'
            '}'
            '#names_field {'
            'padding-left: 8px;'
            'background: #ecfdf5;'
            'border: 1px solid #022c22;'
            'color: #022c22;'
            '}'
        )

        self.radio_italic = QCheckBox('Наклонный', self.form)
        self.radio_italic.move(25, 25)
        self.radio_italic.setObjectName('radio-el')
        self.radio_caps = QCheckBox('CAPS', self.form)
        self.radio_caps.move(25, 55)
        self.radio_caps.setObjectName('radio-el')
        self.radio_bold = QCheckBox('Весь жирный', self.form)
        self.radio_bold.move(25, 85)
        self.radio_bold.setObjectName('radio-el')

        self.title = QLineEdit(self.form)
        self.title.setPlaceholderText('Название композитора')
        self.title.setText('PILLBOX')
        self.title.move(25, 135)
        self.title.resize(200, 30)
        self.title.setObjectName('names_field')

        self.album = QLineEdit(self.form)
        self.album.setPlaceholderText('Название альбома/трека')
        self.album.setText('KOMM NIGHT REIN')
        self.album.move(25, 180)
        self.album.resize(200, 30)
        self.album.setObjectName('names_field')

        self.ser_number = QLineEdit(self.form)
        self.ser_number.setPlaceholderText('Номер кассаты из тиража')
        self.ser_number.setText('#TMPL003')
        self.ser_number.move(25, 225)
        self.ser_number.resize(200, 30)
        self.ser_number.setObjectName('names_field')

        self.lable = QLineEdit(self.form)
        self.lable.setPlaceholderText('Название лейбла')
        self.lable.setText('TEMPLE DRIVE')
        self.lable.move(25, 225)
        self.lable.resize(200, 30)
        self.lable.setObjectName('names_field')

        self.submit = QPushButton('Собрать дизайн', self.form)
        self.submit.setObjectName('submit')
        self.submit.move(25, h - 64)
        self.submit.resize(200, 35)
        self.submit.setStyleSheet(
            '#submit {'
            'background: #10b981;'
            'color: #ecfdf5;'
            'font-weight: 700;'
            'font-size: 16px;'
            'border: 1px solid #022c22;'
            'padding-bottom: 4px;'
            'border-radius: 6px;'
            '}'
            '#submit:hover {'
            'background: #059669;'
            '}'
        )
        self.submit.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
