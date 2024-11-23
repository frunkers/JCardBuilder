import csv


class Store:
    def __init__(self):
        self.state = {}
        self.reset_state()
        self.active_cassette = list(self.state.keys())[0]

    def reset_state(self):
        with open('dev/db/db.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                self.state[row['name']] = row


store = Store()
