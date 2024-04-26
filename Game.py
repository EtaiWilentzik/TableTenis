import cv2

from Constants import Constants


class Game:
    def __init__(self, ball, table):
        self.min_height = None
        self.ball = ball
        self.table = table
        # self.count_left = 0
        # self.count_right = 0

    # def get_ball(self):
    #     return self.ball
    #
    # def set_ball(self, new_ball):
    #     self.ball = new_ball
    #
    # def get_table(self):
    #     return self.table
    #
    # def set_table(self, new_table):
    #     self.table = new_table

    def bounce(self, frame,counter):
        if len(self.ball.positions) < 3:
            return

        #  checks that the second last is the minimum of its neighbors (y coordinate only)
        if self.ball.positions[-1].y < self.ball.positions[-2].y and self.ball.positions[-2].y > \
                self.ball.positions[-3].y:
            # checks if x coordinate is in the left table
            left_table_x = self.table.left_table[2] > self.ball.positions[-2].x > self.table.left_table[0]

            # checks if y coordinate is the same as height of the table
            left_on_table_y = self.table.left_table[1] - Constants.EPSILON < self.ball.positions[-2].y < \
                              self.table.left_table[3]

            if left_table_x and left_on_table_y:  # if ball hits left table
                self.ball.positions[-2].set_vertical()  # indicates ball hits table
                self.ball.left_counter += 1  # ball hits left table one more time
                if self.ball.left_counter > 1:  # ball hits twice in the same table - means losing the game
                    #need to think what to do here. for now we will print it on the screen.
                    cv2.putText(frame, f" player right won and the counter is {counter}", (int(100), int(500)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, Constants.BLUE, 12, cv2.LINE_AA, )

            # checks if x coordinate is in the right table
            right_table_x = self.table.right_table[2] > self.ball.positions[-2].x > self.table.right_table[0]

            # checks if y coordinate is the same as height of the table
            right_on_table_y = self.table.right_table[1] - Constants.EPSILON < self.ball.positions[-2].y < \
                               self.table.right_table[3]

            if right_table_x and right_on_table_y:  # if ball hits right table
                self.ball.positions[-2].set_vertical()  # indicates ball hits table
                self.ball.right_counter += 1  # ball hits right table one more time
                if self.ball.right_counter > 1:  # ball hits twice in the same table - means losing the game
                    # need to think what to do here. for now we will print it on the screen.

                    cv2.putText(frame, f" player left won and the counter is {counter}", (int(800), int(800)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, Constants.RED, 12, cv2.LINE_AA, )

    def set_game_constants(self):
        self.table.set_coordinates_table()
        self.table.set_coordinates_net()
        self.table.set_two_sides()
        self.ball.net_x = self.table.netlist[0]
        # this is the minimum value that we expect someone to hit the ball. i.e lower than this is a point to the
        # opponent.
        self.min_height = (self.table.list[1] + 2 * self.table.list[3]) / 3  # avrage

    def test_frame(self, frame,counter):

        self.ball.set_side_of_table(counter)
        self.bounce(frame,counter)



    # def ball_is_out(self):
    #
    #     if self.ball.positions[-1].y > self.min_height:
    #         if self.count_left == 1:
    #             print("player right won ")
    #
    #         elif self.count_right == 1:
    #             print("player left won")
