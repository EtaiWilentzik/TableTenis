import cv2

from Constants import Constants
from Ball import Ball
from Table import Table


class Game:
    def __init__(self, ball, table):
        self.min_height = None
        self.ball = ball
        self.table = table
        self.count_left = 0
        self.count_right = 0


    def get_ball(self):
        return self.ball

    def set_ball(self, new_ball):
        self.ball = new_ball

    def get_table(self):
        return self.table

    def set_table(self, new_table):
        self.table = new_table

    def bounce(self,frame):
        if len(self.ball.positions) < 3:
            return
            # y1table < posList[-2][1] < y2table:
        if self.ball.positions[-1][1] < self.ball.positions[-2][1] and self.ball.positions[-2][1] > self.ball.positions[-3][1]:
            if self.table.left_table[2] > self.ball.positions[-2][0] > self.table.left_table[0] and \
                    (self.table.left_table[1]-Constants.EPSILON) < self.ball.positions[-2][1] < self.table.left_table[3]:
                self.ball.positions[-2] = (self.ball.positions[-2][0], self.ball.positions[-2][1], True)
                self.count_left+=1
                if self.count_left>1:
                    #need to think what to do here. for now we will print it on the screen.
                    print("player right won")
                    cv2.putText(frame, " player right won" , (int(100), int(500)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, Constants.BLUE, 12, cv2.LINE_AA, )

            if self.table.right_table[2] > self.ball.positions[-2][0] > self.table.right_table[0] and \
                    (self.table.right_table[1] - Constants.EPSILON) < self.ball.positions[-2][1] < self.table.right_table[3]:
                self.ball.positions[-2] = (self.ball.positions[-2][0], self.ball.positions[-2][1], True)
                self.count_right += 1
                if self.count_right > 1:
                    # need to think what to do here. for now we will print it on the screen.
                    print("player left won")
                    cv2.putText(frame, " player left won", (int(400), int(800)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, Constants.RED, 12, cv2.LINE_AA, )

    def set_game_constants(self):
        self.table.set_coordinates_table()
        self.table.set_coordinates_net()
        self.table.set_two_sides()
        #this is the minimum value that we expect someone to hit the ball. i.e lower than this is a point to the opponent.
        self.min_height = (self.table.list[1] + 2 * self.table.list[3]) / 3  # avrage
    def ball_is_out(self):

        if self.ball.positions[-1][1]>self.min_height:
            if self.count_left==1:
                print("player right won ")

            elif self.count_right==1:
                print("player left won")





