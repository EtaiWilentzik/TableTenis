from Constants import Constants
class Table:
    def __init__(self):
        self.list = [0.0, 0.0, 0.0, 0.0]
        self.counter = 0
        self.top_left = (0, 0)
        self.bottom_right = (0, 0)
        self.bottom_net = (0, 0)
        self.top_net = (0, 0)

    def get_top_left(self):
        return self.top_left

    def set_top_left(self, top_left):
        self.top_left = top_left

    def get_bottom_right(self):
        return self.bottom_right

    def set_bottom_right(self, bottom_right):
        self.bottom_right = bottom_right

    def get_bottom_net(self):
        return self.bottom_net

    def set_bottom_net(self, bottom_net):
        self.bottom_net = bottom_net

    def get_top_net(self):
        return self.top_net

    def set_top_net(self, top_net):
        self.top_net = top_net

    def set_table(self, top_left, bottom_right):
        self.list[0] += top_left[0]
        self.list[1] += top_left[1]
        self.list[2] += bottom_right[0]
        self.list[3] += bottom_right[1]
        self.counter += 1
        if self.counter == 2 * Constants.FPS:
            for i in range(len(self.list)):
                # int divide is //
                self.list[i] = int(self.list[i] / (2 * Constants.FPS))

            self.set_top_left((self.list[0], self.list[1]))
            self.set_bottom_right((self.list[2], self.list[3]))
