from PyQt6 import QtCore
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QCheckBox
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QInputDialog, QColorDialog, QComboBox
from store import store


class Form(QWidget):
    def __init__(self, parent, cassette):
        super().__init__()
        self.parent = parent
        self.cassette = cassette
        self.initUI()
        self.update_placeholders()

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
        self.title.setPlaceholderText('Название муз. группы')
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

        self.size_label = QLabel('Размер\nмуз. группы', self.form)
        self.size_label.move(146, 25)

        self.size = QComboBox(self.form)
        self.size.addItems(['24px', '26px', '28px', '30px', '32px'])
        self.size.setCurrentText(store.state['title-size'])
        self.size.move(146, 70)
        self.size.currentTextChanged.connect(self.form_size)

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
        self.form_reset.move(25, 432)
        self.form_reset.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.form_reset.clicked.connect(self.form_reset_action)

    def update_placeholders(self):
        self.title.setText(store.state['title'])
        self.album.setText(store.state['album'])
        self.ser_number.setText(store.state['ser_number'])
        self.lable.setText(store.state['lable'])

    def form_size(self, text):
        store.update_state({
            **store.state,
            'title-size': text
        })

    def form_reset_action(self):
        store.reset_state()
        self.update_placeholders()
        self.radio_italic.setChecked(False)
        self.radio_caps.setChecked(False)
        self.radio_bold.setChecked(False)
        self.size.setCurrentText(store.state['title-size'])
        self.cassette.update_content()
        self.cassette.update_styles()

    def form_save(self):
        name, ok_pressed = QInputDialog.getText(self.parent, 'Сохранить как', 'Введите имя файла: ')
        if ok_pressed:
            pass

    def form_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            store.state['color'] = color.name()

    def form_submit(self):
        if self.radio_italic.isChecked():
            store.state['style'] = 'italic'
        if self.radio_caps.isChecked():
            store.state['transform'] = 'uppercase'
        if self.radio_bold.isChecked():
            store.state['weight'] = '700'
        store.update_state({
            **store.state,
            'title': self.title.text(),
            'album': self.album.text(),
            'ser_number': self.ser_number.text(),
            'lable': self.lable.text(),
        })
        self.cassette.update_content()
        self.cassette.update_styles()
