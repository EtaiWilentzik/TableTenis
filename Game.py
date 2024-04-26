import cv2

from Constants import *


class Game:
    def __init__(self, ball, table):
        self.min_height = 0  #put zeero becuase its the maximum i.e the top of the frame
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

    def double_bounce(self, frame, counter):
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

                 ########## remove the comment from here at the end #########
                # if self.ball.left_counter > 1:  # ball hits twice in the same table - means losing the game
                #
                #
                #     cv2.putText(frame, f" player right won and the counter is {counter}", (int(100), int(500)),
                #                 cv2.FONT_HERSHEY_SIMPLEX, 1.0, Color.BLUE, 3, cv2.LINE_AA, )

            # checks if x coordinate is in the right table
            right_table_x = self.table.right_table[2] > self.ball.positions[-2].x > self.table.right_table[0]

            # checks if y coordinate is the same as height of the table
            right_on_table_y = self.table.right_table[1] - Constants.EPSILON < self.ball.positions[-2].y < \
                               self.table.right_table[3]

            if right_table_x and right_on_table_y:  # if ball hits right table
                self.ball.positions[-2].set_vertical()  # indicates ball hits table
                self.ball.right_counter += 1  # ball hits right table one more time

                ########## remove the comment from here at the end #########

                # if self.ball.right_counter > 1:  # ball hits twice in the same table - means losing the game
                #
                #     cv2.putText(frame, f" player left won and the counter is {counter}", (int(800), int(800)),
                #                 cv2.FONT_HERSHEY_SIMPLEX, 1.0, Color.RED, 2, cv2.LINE_AA, )

    def hit_table_point(self, frame):
        if len(self.ball.positions) < 3:
            return
        #this purpule line is where we put the min height param.
        cv2.line(frame, (int(self.min_height), int(self.min_height)),
                 (int(self.min_height) + 500, int(self.min_height)), Color.PURPLE, 2)
        if self.ball.get_y() > self.min_height:

            if self.ball.left_counter > 0:  # that mean that the last frame the ball is very low  we assume the other player cant touch it.

                cv2.putText(frame, f" player right won in hit table point", (int(230), int(150)),  cv2.FONT_HERSHEY_SIMPLEX,
                            1.0, Color.MAGENTA, 5, cv2.LINE_AA, )
            elif self.ball.right_counter > 0:
                cv2.putText(frame, f" player left won in hit table point", (int(300), int(700)),  cv2.FONT_HERSHEY_SIMPLEX,
                            1.0, Color.MAGENTA, 5, cv2.LINE_AA, )

    def set_game_constants(self):
        self.table.set_coordinates_table()
        self.table.set_coordinates_net()
        self.table.set_two_sides()
        self.ball.net_x = self.table.netlist[0]
        # this is the minimum value that we expect someone to hit the ball. i.e lower than this is a point to the
        # opponent.
        self.min_height = (self.table.list[1] + 2 * self.table.list[3]) / 3  # avrage

    def test_frame(self, frame, counter):
        self.ball.set_side_of_table()
        self.hit_table_point(frame)
        #i think this function need to called last  because only here i change the left and right counting but im not sure about it yet.
        self.double_bounce(frame, counter)
        # need to create here function that checks if the ball hit the table and now he is lower than something we can say its a point to the other side
        #todo: create function that checks if the ball does not hit the table when hitting the floor first.
        #todo: somhow to check if the player touch the ball before its hits the table.
        #todo: identify if its a server or not
        #todo: identify when point is ending
        #todo: maybe to use threads on each function that being called in test_frame

    # def ball_is_out(self):
    #
    #     if self.ball.positions[-1].y > self.min_height:
    #         if self.count_left == 1:
    #             print("player right won ")
    #
    #         elif self.count_right == 1:
    #             print("player left won")
