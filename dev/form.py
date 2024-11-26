from PyQt6 import QtCore
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QFileDialog
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
        self.title.setPlaceholderText('Название муз. группы (max=9)')
        self.title.move(25, 135)
        self.title.resize(200, 30)
        self.title.setObjectName('names_field')
        self.title.setMaxLength(9)

        self.album = QLineEdit(self.form)
        self.album.setPlaceholderText('Название альбома (max=18)')
        self.album.move(25, 180)
        self.album.resize(200, 30)
        self.album.setObjectName('names_field')
        self.album.setMaxLength(18)

        self.ser_number = QLineEdit(self.form)
        self.ser_number.setPlaceholderText('Номер кассеты (max=6)')
        self.ser_number.move(25, 225)
        self.ser_number.resize(200, 30)
        self.ser_number.setObjectName('names_field')
        self.ser_number.setMaxLength(6)

        self.lable = QLineEdit(self.form)
        self.lable.setPlaceholderText('Название лейбла (max=20)')
        self.lable.move(25, 270)
        self.lable.resize(200, 30)
        self.lable.setObjectName('names_field')
        self.lable.setMaxLength(20)

        self.size_label = QLabel('Размер\nмуз. группы', self.form)
        self.size_label.move(146, 25)

        self.size = QComboBox(self.form)
        self.size.addItems(['22px', '24px', '26px', '28px', '30px', '32px', '34px', '36px', '38px', '40px'])
        self.size.setCurrentText(store.state[store.active_cassette]['title-size'])
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

        self.image = QPushButton('Выбрать\nизображение', self.form)
        self.image.setObjectName('image')
        self.image.setGeometry(
            400 - 25 - 104, 205,
            100, 100
        )
        self.image.setStyleSheet(
            '#image {'
            'background: #d6d3d1;'
            'color: #022c22;'
            'border: 1px solid #292524;'
            'padding: 10px;'
            'border-radius: 3px;'
            '}'
            '#image:hover {'
            'background: #a8a29e;'
            '}'
        )
        self.image.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.image.clicked.connect(self.form_image)

        self.save = QPushButton('Сохранить настройки кассеты', self.form)
        self.save.setObjectName('form_btn')
        self.save.move(25, 400)
        self.save.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save.clicked.connect(self.form_save)

        self.form_reset = QPushButton('Очистить форму', self.form)
        self.form_reset.setObjectName('form_btn')
        self.form_reset.move(25, 432)
        self.form_reset.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.form_reset.clicked.connect(self.form_reset_action)

    def form_image(self):
        fileName, filter = QFileDialog().getOpenFileName(self.form, 'Имя файла:', '', '*jpg, *jpeg, *png')
        if fileName:
            store.state[store.active_cassette]['image-url'] = fileName

    def update_placeholders(self):
        self.title.setText(store.state[store.active_cassette]['title'])
        self.album.setText(store.state[store.active_cassette]['album'])
        self.ser_number.setText(store.state[store.active_cassette]['ser_number'])
        self.lable.setText(store.state[store.active_cassette]['lable'])

    def form_size(self, text):
        store.state[store.active_cassette]['title-size'] = text

    def form_reset_action(self):
        store.reset_state()
        if store.state[store.active_cassette]['style'] == 'italic':
            self.radio_italic.setChecked(True)
        else:
            self.radio_italic.setChecked(False)
        if store.state[store.active_cassette]['transform'] == 'uppercase':
            self.radio_caps.setChecked(True)
        else:
            self.radio_caps.setChecked(False)
        if store.state[store.active_cassette]['weight'] == 'bold':
            self.radio_bold.setChecked(True)
        else:
            self.radio_bold.setChecked(False)
        self.size.setCurrentText(store.state[store.active_cassette]['title-size'])
        self.update_placeholders()
        self.cassette.update_content()
        self.cassette.update_styles()

    def form_save(self):
        name, ok_pressed = QInputDialog.getText(
            self.parent,
            'Сохранить как',
            'Введите краткое название.\nНапример: моя кассета.\n'
            'Нельзя использовать: default, default2'
        )
        if name == 'default' or name == 'default2':
            self.form_save()
        else:
            if ok_pressed:
                store.push_cassette(name)

    def form_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            store.state[store.active_cassette]['color'] = color.name()

    def form_radios(self):
        if self.radio_italic.isChecked():
            store.state[store.active_cassette]['style'] = 'italic'
        else:
            store.state[store.active_cassette]['style'] = 'normal'
        if self.radio_caps.isChecked():
            store.state[store.active_cassette]['transform'] = 'uppercase'
        else:
            store.state[store.active_cassette]['transform'] = 'none'
        if self.radio_bold.isChecked():
            store.state[store.active_cassette]['weight'] = '700'
        else:
            store.state[store.active_cassette]['weight'] = '400'

    def form_submit(self):
        self.form_radios()
        store.state[store.active_cassette]['title'] = self.title.text()
        store.state[store.active_cassette]['album'] = self.album.text()
        store.state[store.active_cassette]['ser_number'] = self.ser_number.text()
        store.state[store.active_cassette]['lable'] = self.lable.text()
        self.cassette.update_content()
        self.cassette.update_styles()
