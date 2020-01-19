import os
import numpy as np
import signal
from base_frame import base_frame
from person import *
from obstacles import horizontal_obstacle, vertical_obstacle, new_obstacle
from background import background
import random
import sys
from constraint_checker import *
from obstacles import *
from config import *
import time
from colorama import Fore, Back, Style
from firing import *

np.set_printoptions(threshold=sys.maxsize)


def bullet_printer(base_frame, Enemy):
    # To print the bullets that has been released
    # By the runner that are either unused or are
    # not on current running frame
    for bullet in base_frame.bullets:
        if(base_frame.get_frame() <= bullet.get_x() < base_frame.get_frame()+100 and bullet.get_status() == True):
            bullet.forward()
            bullet.detect_collision(base_frame, Enemy)
            bullet.on_frame(bullet.get_x(), base_frame)


def magnet_printer(magnet, frame):
    # To print magnet on the screen
    magnet.magnet_on_frame(frame)


def ice_ball_printer(Frame, Runner):
    # To print the ice balls being released from dragon
    for ice_ball in Frame.ice_balls:
        if(ice_ball.get_status() == True and ice_ball.get_x() > STATIC_FRAME-FRAME_PER_SCENE):
            ice_ball.forward()
            ice_ball.check_collision(Frame, Runner)
            ice_ball.on_frame(Frame)


# Objects of all created classes
Frame = base_frame()
boundary = Frame.generate_boundary()
Runner = Person()
iteration = 0  # No of iterations passed while game running
Frame.place_rewards()
obstacle_place(Frame)
cloud = background()
cloud.place_background(Frame)
magnet = Magnet(random.randint(MAGNET_LOCATION_MIN,
                               MAGNET_LOCATION_MAX), MAGNET_LOC_Y)
mag_loc = magnet.get_x()
Runner.set_magnetx(magnet.get_x())
magnet_period = 0  # This will used to define the period for which magnet has to be displayed
boost_check = 0
enemy = Enemy()

# The game will run untill either time_remaining gets zero
# And Untill the runner has life
# And untill enemy has time
while(Frame.get_time() and Runner.show_life() and enemy.show_life()):

    # Print the required stats of the game
    print("\033[0;0f")
    print("\n\n     SCORE : ", end="   ")
    print(Runner.show_score(), end="        ")
    print("      LIFE : ", end="    ")
    print(Runner.show_life(), end="        ")
    print("      SHIELD : ", Runner.show_shield(), end='    ')
    print("    TIME REMAINING : ", Frame.get_time())
    print()

    # Copy the background to frame
    for i in range(TOTAL_WIDTH):
        for j in range(FRAME_PER_SCENE):
            Frame.user_frame[i][Frame.get_frame() +
                                j] = Frame.frame[i][Frame.get_frame()+j]

    # Used To generate person on user frame and print the bullets
    Runner.generate_person(Frame, enemy)
    bullet_printer(Frame, enemy)

    # Used for the magnet as an obstacle which will only be available for small period
    if(Frame.get_frame() <= mag_loc < Frame.get_frame()+80 and magnet_period < 300):
        magnet_printer(magnet, Frame)
        Runner.set_magnet()
        magnet_period += 1

        if(Runner.check_boost() == True and boost_check < 200):
            if(iteration % 2 == 0):
                magnet.forward()
                Runner.set_magnetx(magnet.get_x())
                Runner.set_x(magnet.get_x())

        else:
            if(iteration % 6 == 0):
                magnet.forward()
                Runner.set_magnetx(magnet.get_x())
                Runner.set_x(magnet.get_x())

    # When the magnet cross the period it would be reset
    if(magnet_period > 300):
        Runner.reset_magnet()

    # When the dragon comes has to placed in frame in the end
    if(Frame.get_frame() + FRAME_PER_SCENE > DRAGON_PLACE_X):
        enemy.place_dragon(Frame, Runner)

        if(iteration % 15 == 0):
            enemy.fire_ice(Frame)

        ice_ball_printer(Frame, Runner)

    # Print the frame on the screen with the aprropriate colors
    for i in range(TOTAL_WIDTH):
        for j in range(FRAME_PER_SCENE):
            if(i == 0 or i == TOTAL_WIDTH-1):
                print("\u001b[31;1m"+Frame.user_frame[i]
                      [Frame.get_frame()+j], end="")
            else:
                if((i == Runner.get_y() and j == Runner.get_x()+1-Frame.get_frame()) or (i == Runner.get_y()+1 and j == Runner.get_x()+1-Frame.get_frame())):
                    print('\u001b[37m'+Frame.user_frame[i]
                          [Frame.get_frame()+j], end="")
                elif(Frame.user_frame[i][Frame.get_frame()+j] == '@'):
                    print('\u001b[38;5;50m'+Frame.user_frame[i]
                          [Frame.get_frame()+j], end="")

                elif(Frame.user_frame[i][Frame.get_frame()+j] == '$'):
                    print('\u001b[38;5;226m'+Frame.user_frame[i]
                          [Frame.get_frame()+j], end="")

                elif(Frame.user_frame[i][Frame.get_frame()+j] == '|' or Frame.user_frame[i][Frame.get_frame()+j] == '='):
                    print('\u001b[38;5;202m'+Frame.user_frame[i]
                          [Frame.get_frame()+j], end="")

                elif(Frame.user_frame[i][Frame.get_frame()+j] == 'S'):
                    print('\u001b[32;1m'+Frame.user_frame[i]
                          [Frame.get_frame()+j], end="")

                elif(Frame.user_frame[i][Frame.get_frame()+j] == '*'):
                    print('\u001b[38;5;172m'+Frame.user_frame[i]
                          [Frame.get_frame()+j], end="")

                elif(Frame.user_frame[i][Frame.get_frame()+j] == '#'):
                    print('\u001b[38;5;50m'+Frame.user_frame[i]
                          [Frame.get_frame()+j], end="")

                elif(Frame.get_frame()+j >= DRAGON_PLACE_X):
                    print('\u001b[32;1m'+Frame.user_frame[i]
                          [Frame.get_frame()+j], end="")

                else:
                    print(Fore.WHITE +
                          Frame.user_frame[i][Frame.get_frame()+j], end="")
        print()

    print()

    if(Runner.show_shield() < 20 and Runner.check_shield() == False):
        if(iteration % 6 == 0):
            Runner.increase_shield()

    elif(Runner.show_shield() == 0 and Runner.check_shield() == True):
        Runner.deactivate_shield()

    elif(Runner.check_shield() == True):
        if(iteration % 2 == 0):
            Runner.decrease_shield()

    Runner.move_person(Frame)
    iteration += 1

    if(Runner.check_boost() == True and boost_check < 200):
        if(iteration % 2 == 0 and Frame.get_frame() < STATIC_FRAME):
            Frame.increase_frame()
            Frame.decrease_time()
        boost_check += 1
    else:
        boost_check = 0
        Runner.change_boostflag()
        if(iteration % 5 == 0 and Frame.get_frame() < STATIC_FRAME):
            Frame.increase_frame()
            Frame.decrease_time()
    
    if(Frame.get_frame() >= STATIC_FRAME):
        if(iteration % 5 == 0):
            Frame.decrease_time()

    if(iteration % (1.5) == 0 and Runner.show_flag() == 0):
        Runner.gravity(Frame)


print("GAME OVER !")
quit()
