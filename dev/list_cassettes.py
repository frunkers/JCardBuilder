from PyQt6.QtWidgets import QWidget, QComboBox
from store import store


class ListCassettes(QWidget):
    def __init__(self, parent, form):
        super().__init__()
        self.parent = parent
        self.form = form
        self.initUI()

    def initUI(self):
        self.list = QComboBox(self.parent)
        self.list.addItems(store.state.keys())
        self.list.setCurrentText(store.active_cassette)
        self.list.move(50, 404 + 50 + 25)
        self.list.currentTextChanged.connect(self.list_change)

    def list_change(self, text):
        store.active_cassette = text
        self.form.form_reset_action()
