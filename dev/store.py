import csv


class Store:
    def __init__(self):
        self.state = {}
        self.reset_state()
        self.active_cassette = list(self.state.keys())[0]

    def from_db(self):
        state = {}
        with open('dev/db/db.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                state[row['name']] = row
        return state

    def reset_state(self):
        self.state = self.from_db()

    def push_cassette(self, name):
        state = self.from_db()
        box = self.state[self.active_cassette].copy()
        state_arr = []
        for i in state.items():
            state_arr.append(i[1])
        box['id'] = len(state)
        box['name'] = name
        state_arr.append(box)

        with open('dev/db/db.csv', 'w', newline='', encoding="utf8") as f:
            writer = csv.DictWriter(f, fieldnames=list(state_arr[0].keys()), delimiter=',')
            writer.writeheader()
            for d in state_arr:
                writer.writerow(d)


store = Store()
