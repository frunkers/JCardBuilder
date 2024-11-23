class Store:
    def __init__(self):
        self.state = {}
        self.reset_state()

    def reset_state(self):
        self.state = {
            'title': 'PILLBOX',
            'album': 'KOMM NIGHT REIN',
            'ser_number': '#TMPL003',
            'lable': 'TEMPLE DRIVE',
            'color': '#022c22',
            'weight': '400',
            'style': 'normal',
            'transform': 'none',
            'title-size': '28px',
        }

    def update_state(self, new_state):
        self.state = new_state


store = Store()
