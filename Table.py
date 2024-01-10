from Constants import Constants


class Table:
    def __init__(self, top_right, top_left, bottom_net, top_net):
        self.top_right = top_right
        self.top_left = top_left
        self.bottom_net = bottom_net
        self.top_net = top_net

    def get_top_left(self):
        return self.top_left

    def get_top_right(self):
        return self.top_right

    def get_bottom_net(self):
        return self.bottom_net

    def get_top_net(self):
        return self.top_net
