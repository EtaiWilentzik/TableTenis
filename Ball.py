from Constants import Constants


class Ball:
    def __init__(self, first_serve):
        self.positions = []
        if first_serve == Constants.LEFT:
            self.last_state = Constants.SERVE_LEFT
        else:
            self.last_state = Constants.SERVE_RIGHT

    def set_coordinates(self, x, y):
        if len(self.positions) >= 30:
            self.positions.pop(0)
            self.positions.append((x, y))
        else:
            self.positions.append((x, y))

    def get_x(self):
        return self.positions[-1][0]

    def get_y(self):
        return self.positions[-1][1]
