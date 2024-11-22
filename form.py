from PyQt6 import QtCore
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QGraphicsDropShadowEffect, QInputDialog, \
    QColorDialog


class Form(QWidget):
    def __init__(self, parent, state):
        super().__init__()
        self.parent = parent
        self.state = state
        self.initUI()

    def initUI(self):
        self.form = QLabel(self.parent)
        self.form.move(500, 50)
        self.form.setObjectName('form')
        self.form.resize(400, 500)
        self.form.setStyleSheet(
            '#form {'
            'background: #d4d4d8;'
            'border-radius: 6px;'
            'border: 1px solid #022c22;'
            '}'

            '#radio-el {'
            'color: #022c22;'
            '}'

            '#names_field {'
            'padding-left: 8px;'
            'background: #ecfdf5;'
            'border: 1px solid #022c22;'
            'color: #022c22;'
            '}'

            '#form_btn {'
            'background: #d6d3d1;'
            'color: #022c22;'
            'border: 1px solid #022c22;'
            'padding: 2px 4px;'
            'border-radius: 3px;'
            '}'
            '#form_btn:hover {'
            'background: #a8a29e;'
            '}'
        )

        effect_form = QGraphicsDropShadowEffect()
        effect_form.setOffset(0, 0)
        effect_form.setBlurRadius(40)
        self.form.setGraphicsEffect(effect_form)

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
        self.title.move(25, 135)
        self.title.resize(200, 30)
        self.title.setObjectName('names_field')

        self.album = QLineEdit(self.form)
        self.album.setPlaceholderText('Название альбома/трека')
        self.album.move(25, 180)
        self.album.resize(200, 30)
        self.album.setObjectName('names_field')

        self.ser_number = QLineEdit(self.form)
        self.ser_number.setPlaceholderText('Номер кассеты из тиража')
        self.ser_number.move(25, 225)
        self.ser_number.resize(200, 30)
        self.ser_number.setObjectName('names_field')

        self.lable = QLineEdit(self.form)
        self.lable.setPlaceholderText('Название лейбла')
        self.lable.move(25, 270)
        self.lable.resize(200, 30)
        self.lable.setObjectName('names_field')

        self.submit = QPushButton('Собрать дизайн', self.form)
        self.submit.setObjectName('submit')
        self.submit.move(25, 332)
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
        self.submit.clicked.connect(self.form_submit)

        self.color = QPushButton('Выбрать\nцвет', self.form)
        self.color.setObjectName('color')
        self.color.move(400 - 25 - self.color.sizeHint().width(), 135)
        self.color.setStyleSheet(
            '#color {'
            'background: #5eead4;'
            'color: #022c22;'
            'border: 2px solid #0f766e;'
            'padding: 10px;'
            'border-radius: 4px;'
            '}'
            '#color:hover {'
            'background: #2dd4bf;'
            '}'
        )
        self.color.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.color.clicked.connect(self.form_color)

        self.save = QPushButton('Сохранить настройки в файл', self.form)
        self.save.setObjectName('form_btn')
        self.save.move(25, 400)
        self.save.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save.clicked.connect(self.form_save)

        self.form_reset = QPushButton('Очистить форму', self.form)
        self.form_reset.setObjectName('form_btn')
        self.form_reset.setStyleSheet = self.save.style()
        self.form_reset.move(25, 432)
        self.form_reset.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.form_reset.clicked.connect(self.form_reset_action)

    def update_placeholders(self):
        self.title.setText(self.state['title'])
        self.album.setText(self.state['album'])
        self.ser_number.setText(self.state['ser_number'])
        self.lable.setText(self.state['lable'])

    def form_reset_action(self):
        self.state = {
            'title': 'PILLBOX',
            'album': 'KOMM NIGHT REIN',
            'ser_number': '#TMPL003',
            'lable': 'TEMPLE DRIVE'
        }
        self.update_content()
        self.update_placeholders()
        self.radio_italic.setChecked(False)
        self.radio_caps.setChecked(False)
        self.radio_bold.setChecked(False)
        self.setStyleSheet(
            '#cassete_title, #spine_text, #spine_text2, #back_text {'
            'color: #022c22;'
            'font-style: normal;'
            'text-transform: none;'
            'font-weight: normal;'
            '}'
        )
        self.color_content = '#022c22'

    def form_save(self):
        name, ok_pressed = QInputDialog.getText(self, 'Сохранить как', 'Введите имя файла: ')
        if ok_pressed:
            pass

    def form_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_content = color.name()

    def form_submit(self):
        a1 = 'normal'
        a2 = 'none'
        a3 = '400'
        if self.radio_italic.isChecked():
            a1 = 'italic'
        if self.radio_caps.isChecked():
            a2 = 'uppercase'
        if self.radio_bold.isChecked():
            a3 = '700'
        self.setStyleSheet(
            '#cassete_title, #spine_text, #spine_text2, #back_text {' +
            'font-style: ' + a1 + ';' +
            'text-transform: ' + a2 + ';' +
            'font-weight: ' + a3 + ';' +
            'color: ' + self.color_content + ';' +
            '}'
        )
        self.state = {
            'title': self.title.text(),
            'album': self.album.text(),
            'ser_number': self.ser_number.text(),
            'lable': self.lable.text()
        }

        self.update_content()
