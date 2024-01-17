class Table:
    def __init__(self):
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
