from Constants import Constants


class Ball:
    def __init__(self):
        # list of (x, y, is_bounce_vertical, is_bounce_horizontal)
        self.positions = []
        self.left_counter = 0
        self.right_counter = 0
        self.direction = -1

    def set_coordinates(self, x, y):
        if len(self.positions) >= 30:
            self.positions.pop(0)
        self.positions.append((x, y, False))
        self.bounce_horizontal()

    def get_positions(self):
        return self.positions

    def get_x(self):
        return self.positions[-1][0]

    def get_y(self):
        return self.positions[-1][1]

    ### if the ball went right or left
    def bounce_horizontal(self):
        if len(self.positions) > 2:
            # check direction of last 2 frames
            d_last = self.positions[-1][Constants.X_COORDINATE] - self.positions[-2][Constants.X_COORDINATE]
            if d_last < 0:
                if self.direction == Constants.RIGHT:
                    self.positions[-2] = self.positions[-2][0], self.positions[-2][1], self.positions[-2][2], True
                self.direction = Constants.LEFT
            elif d_last > 0:
                if self.direction == Constants.LEFT:
                    self.positions[-2] = self.positions[-2][0], self.positions[-2][1], self.positions[-2][2], True
                self.direction = Constants.RIGHT
        # if len(self.positions) < 6:
        #     return
        # # check direction of last 2 frames
        # d_last = self.positions[-1][Constants.X_COORDINATE] - self.positions[-2][Constants.X_COORDINATE]
        # # check direction of the previous last 2 frames
        # d_prev_last = self.positions[-2][Constants.X_COORDINATE] - self.positions[-3][Constants.X_COORDINATE]
        #
        # if d_last > 0 > d_prev_last or d_last < 0 < d_prev_last:
        #     self.positions[-2][Constants.IS_BOUNCE_HORIZONTAL] = True
        #     return
        #
        # # check if there is no change in x coordinate in d_prev_last
        # if d_prev_last == 0:
        #     # check direction of the previousX4 last 2 frames
        #     d_prevX4_last = self.positions[-5][Constants.X_COORDINATE] - self.positions[-6][Constants.X_COORDINATE]
        #
        #     if d_last > 0 > d_prevX4_last or d_last < 0 < d_prevX4_last:
        #         self.positions[-2] = self.positions[-2][0], self.positions[-2][1], self.positions[-2][2], True
        #         return

    def bounce_vertical(self, table):
        if len(self.positions) < 3:
            return
        # y1table < posList[-2][1] < y2table:
        if (self.positions[-1][1] < self.positions[-2][1] and self.positions[-2][1] > self.positions[-3][1] and
                table.get_bottom_right()[Constants.X_COORDINATE] > self.positions[-2][0] >
                table.get_top_left()[Constants.X_COORDINATE] and
                (table.get_top_left()[Constants.Y_COORDINATE] - Constants.EPSILON) < self.positions[-2][1] <
                table.get_bottom_right()[Constants.Y_COORDINATE]):
            self.positions[-2] = (self.positions[-2][0], self.positions[-2][1], True)


