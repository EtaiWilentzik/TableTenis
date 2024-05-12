import os
import torch
from ultralytics import YOLO
from Ball import Ball
from Table import Table
from Game import Game
from Constants import Constants
from video_handler import VideoHandler
from mini_court import MiniCourt

# in the screen - (0, 0) is top left corner

video_handler = VideoHandler()
# create mini_court draw
mini_court = MiniCourt(VideoHandler.frame)
model_path = os.path.join('.', 'train5', 'weights', 'best.pt')  # get the training set
#use cuda if possible
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')
#do it only for etai
torch.cuda.set_device(0)

model = YOLO(model_path)  # load a custom model
model.to(device=device)
game = Game(Ball(), Table())
while video_handler.get_ret():  # until no more frames

    # start_time = time.time()

    # max_det=3 in model.predict say how many object i want to detect
    results = model.predict(video_handler.get_frame())[0]

    for left_x, top_y, right_x, bottom_y, score, class_id in results.boxes.data.tolist():  # coordinates, accuracy ,
        # class_id(like train)
        xCenter = (left_x + right_x) // 2  # Calculate x-center
        yCenter = (top_y + bottom_y) // 2  # Calculate y-center
        if score > Constants.THRESHOLD:
            if class_id == Constants.TABLE_ID:
                if Constants.counterUntilFrame <= 2 * Constants.FPS:  # 2 seconds of fixing table coordinates until beginning

                    game.table.sum_table((left_x, top_y), (right_x, bottom_y))  # summing coordinates to calc avg

            if class_id == Constants.NET_ID:
                if Constants.counterUntilFrame <= 2 * Constants.FPS:  # 2 seconds of fixing table coordinates until beginning
                    game.table.sum_net((left_x, top_y), (right_x, bottom_y))

            if class_id == Constants.Ball_ID:
                game.ball.set_coordinates(xCenter, yCenter)  # adding new coordinates to the list

                game.ball.set_speed()
                # etai moved it here from the same indentation as the if classes conditions i.e. one after the if
                # threshold.
                video_handler.paint_ball_movement(game)

                #################### CHECKING THE VIDEO ########################

                # if ball.direction == Constants.LEFT:
                #     cv2.putText(frame, " left", (int(x1), int(y1 - 10)),
                #                 cv2.FONT_HERSHEY_SIMPLEX, 1.3, Constants.GREEN, 3, cv2.LINE_AA, )
                # else:
                #     cv2.putText(frame, " right", (int(x1), int(y1 - 10)),
                #                 cv2.FONT_HERSHEY_SIMPLEX, 1.3, Constants.GREEN, 3, cv2.LINE_AA, )
                # top left is first, bottom right is second, color is third, and thickness is the last

                #moved it here under the if of the ball because  all the test in test_frame are only when i deteacte ball.
                game.test_frame(video_handler.get_frame(),Constants.counterUntilFrame, )  # checks if there was a bounce and determine the rest of the
        video_handler.paint_all(left_x, top_y, right_x, bottom_y,results.names[int(class_id)])
    if Constants.counterUntilFrame == 2 * Constants.FPS:  # setting the position of table after calculating avg of coordinates
        game.set_game_constants()

    # video_handler.draw_result()
    #this need to be last because at the end there is self.out.write(self.frame)
    video_handler.paint_two_sides(game)
    # video_handler.paint_ball_movement(game)
    #think this function must be last beacue we are changing the frame.
    # mini_court.draw_mini_court(VideoHandler.frame)
    mini_court.draw_mini_court(VideoHandler.frame, game)
    video_handler.paint_frame_counter()
    #put this line in comment after finishing


    # write the frame to the video this function must be last.
    video_handler.write_video()
    # elapsed_time_ms = (time.time() - start_time) * 1000
    Constants.counterUntilFrame += 1

    video_handler.read_next_frame()

video_handler.release()
