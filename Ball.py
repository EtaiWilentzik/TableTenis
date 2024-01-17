from Constants import Constants


class Ball:
    def __init__(self):
        self.positions = []
        # if first_serve == Constants.LEFT:
        #     self.last_state = Constants.SERVE_LEFT
        # else:
        #     self.last_state = Constants.SERVE_RIGHT

    def set_coordinates(self, x, y):
        if len(self.positions) >= 30:
            self.positions.pop(0)
        self.positions.append((x, y, False))

    def get_positions(self):
        return self.positions

    def get_x(self):
        return self.positions[-1][0]

    def get_y(self):
        return self.positions[-1][1]

    def bounce(self, table):
        if len(self.positions) < 3:
            return
        # y1table<posList[-2][1]<y2table:
        if self.positions[-1][1] < self.positions[-2][1] and self.positions[-2][1] > self.positions[-3][1] and \
                table.get_bottom_right()[Constants.X_COORDINATE] > \
                self.positions[-2][
                    0] > table.get_top_left()[Constants.X_COORDINATE] and (
                table.get_top_left()[Constants.Y_COORDINATE] - 100) < self.positions[-2][1] < table.get_bottom_right()[
            Constants.Y_COORDINATE]:
            self.positions[-2] = (self.positions[-2][0], self.positions[-2][1], True)
