import os
from ultralytics import YOLO
from Ball import Ball
from Table import Table
from Game import Game
from Constants import Constants
from video_handler import VideoHandler

# in the screen - (0, 0) is top left corner

video_handler = VideoHandler()
model_path = os.path.join('.', 'train8', 'weights', 'last.pt')  # get the training set

model = YOLO(model_path)  # load a custom model
counterUntilFrame = 0  # count up until table is fixed
game = Game(Ball(), Table())
while video_handler.get_ret():  # until no more frames

    # start_time = time.time()

    # max_det=3 in model.predict say how many object i want to detect
    results = model.predict(video_handler.get_frame())[0]

    for left_x, top_y, right_x, bottom_y, score, class_id \
            in results.boxes.data.tolist():  # coordinates, accuracy ,class_id(like train)

        xCenter = (left_x + right_x) // 2  # Calculate x-center
        yCenter = (top_y + bottom_y) // 2  # Calculate y-center

        if score > Constants.THRESHOLD:

            if class_id == Constants.TABLE_ID:
                if counterUntilFrame <= 2 * Constants.FPS:  # 2 seconds of fixing table coordinates until beginning

                    game.table.sum_table((left_x, top_y), (right_x, bottom_y))  # summing coordinates to calc avg

            if class_id == Constants.NET_ID:
                if counterUntilFrame <= 2 * Constants.FPS:  # 2 seconds of fixing table coordinates until beginning
                    game.table.sum_net((left_x, top_y), (right_x, bottom_y))

            if class_id == Constants.Ball_ID:
                game.ball.set_coordinates(xCenter, yCenter)  # adding new coordinates to the list

                #################### CHECKING THE VIDEO ########################

                # if ball.direction == Constants.LEFT:
                #     cv2.putText(frame, " left", (int(x1), int(y1 - 10)),
                #                 cv2.FONT_HERSHEY_SIMPLEX, 1.3, Constants.GREEN, 3, cv2.LINE_AA, )
                # else:
                #     cv2.putText(frame, " right", (int(x1), int(y1 - 10)),
                #                 cv2.FONT_HERSHEY_SIMPLEX, 1.3, Constants.GREEN, 3, cv2.LINE_AA, )
                # top left is first, bottom right is second, color is third, and thickness is the last

            video_handler.paint_all(left_x, top_y, right_x, bottom_y)
            game.test_frame(video_handler.get_frame())  # checks if there was a bounce and determine the rest of the

            ################################ painting ###########################################
            video_handler.paint_ball_movement(game)

    if counterUntilFrame == 2 * Constants.FPS:  # setting the position of table after calculating avg of coordinates
        game.set_game_constants()

    video_handler.paint_two_sides(game)

    # elapsed_time_ms = (time.time() - start_time) * 1000
    counterUntilFrame += 1

    video_handler.read_next_frame()

video_handler.release()
