import os
import numpy as np
import signal
from base_frame import base_frame
from person import *
from obstacles import horizontal_obstacle, vertical_obstacle, new_obstacle
from background import background
import random
import sys
from obstacles import *
from config import *
import time
from colorama import Fore
from firing import *
from endscreen import *

np.set_printoptions(threshold=sys.maxsize)


def bullet_printer(base_frame, Enemy):
    # To print the bullets that has been released
    # By the runner that are either unused or are
    # not on current running frame
    bullet_list = base_frame.get_bullets()
    for bullet in bullet_list:
        if(base_frame.get_frame() <= bullet.get_x() < base_frame.get_frame()+100 and bullet.get_status() == True):
            bullet.forward()
            bullet.detect_collision(base_frame, Enemy)
            bullet.on_frame(bullet.get_x(), base_frame)


def magnet_printer(magnet, frame):
    # To print magnet on the screen
    magnet.magnet_on_frame(frame)


def ice_ball_printer(Frame, Runner):
    # To print the ice balls being released from dragon
    ice_balls_list = Frame.get_ice_balls()
    for ice_ball in ice_balls_list:
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
enemy = Enemy()

# The game will run untill either time_remaining gets zero
# And Untill the runner has life
# And untill enemy has time
while(Frame.get_time() and Runner.show_life() and enemy.show_life()):

    # Print the required stats of the game
    print("\033[0;0f")
    os.system("tput civis")
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
            Frame.set_user_frame(i,Frame.get_frame()+j,Frame.get_particular_frame(i,Frame.get_frame()+j))

    # Used To generate person on user frame and print the bullets
    Runner.generate_person(Frame, enemy)
    bullet_printer(Frame, enemy)

    # Used for the magnet as an obstacle which will only be available for small period
    if(Frame.get_frame() <= mag_loc < Frame.get_frame()+80):
        magnet_printer(magnet, Frame)
        Runner.set_magnet()
        Runner.decrease_magnetperiod()

        if(Runner.check_boost() == True and Runner.get_boostdur() > 0):
            if(iteration % 2 == 0):
                magnet.forward()
                Runner.set_magnetx(magnet.get_x())
                if(magnet.get_x()-magnet.get_range() <= Runner.get_x() <= magnet.get_x()+magnet.get_range()):
                    Runner.set_x(magnet.get_x())

        else:
            if(iteration % 6 == 0):
                magnet.forward()
                Runner.set_magnetx(magnet.get_x())
                if(magnet.get_x()-magnet.get_range() <= Runner.get_x() <= magnet.get_x()+magnet.get_range()):
                    Runner.set_x(magnet.get_x())

    # When the magnet cross the period it would be reset
    if(Runner.get_magnetperiod() == 0):
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
                print("\u001b[31;1m"+Frame.get_particular_user_frame(i,Frame.get_frame()+j),end="")
            else:
                if(((i == Runner.get_y() and j == Runner.get_x()+1-Frame.get_frame()) or (i == Runner.get_y()+1 and j == Runner.get_x()+1-Frame.get_frame())) and Runner.check_shield() is False):
                    print('\u001b[37m'+Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")

                elif(((i == Runner.get_y() and j == Runner.get_x()+1-Frame.get_frame()) or (i == Runner.get_y()+1 and j == Runner.get_x()+1-Frame.get_frame())) and Runner.check_shield() is True):
                    print('\u001b[38;5;84m'+Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")

                elif((Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '/' or Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '\\' or Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '-') and Runner.check_shield() is False):
                    print('\u001b[37m'+Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")

                elif((Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '/' or Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '\\' or Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '-') and Runner.check_shield() is True):
                    print('\u001b[38;5;84m'+Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")
                
                elif(Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '@'):
                    print('\u001b[38;5;50m'+Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")

                elif(Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '$'):
                    print('\u001b[38;5;226m'+Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")

                elif(Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '|' or Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '='):
                    print('\u001b[38;5;202m'+Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")

                elif(Frame.get_particular_user_frame(i,Frame.get_frame()+j) == 'S'):
                    print('\u001b[32;1m'+Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")

                elif(Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '*'):
                    print('\u001b[38;5;172m'+Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")

                elif(Frame.get_particular_user_frame(i,Frame.get_frame()+j) == '#'):
                    print('\u001b[38;5;50m'+Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")

                elif(Frame.get_frame()+j >= DRAGON_PLACE_X):
                    print('\u001b[32;1m'+Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")

                else:
                    print(Fore.WHITE +
                          Frame.get_particular_user_frame(i,Frame.get_frame()+j), end="")
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

    if(Runner.check_boost() == True and Runner.get_boostdur() > 0):
        if(iteration % 2 == 0 and Frame.get_frame() < STATIC_FRAME):
            Frame.increase_frame()
            Frame.decrease_time()
        Runner.decrease_boost()
    else:
        Runner.change_boostflag()
        if(iteration % 5 == 0 and Frame.get_frame() < STATIC_FRAME):
            Frame.increase_frame()
            Frame.decrease_time()

    if(Frame.get_frame() >= STATIC_FRAME):
        if(iteration % 5 == 0):
            Frame.decrease_time()

    if(iteration % (1.5) == 0 and Runner.show_flag() == 0):
        Runner.gravity(Frame)

os.system('clear')

if(Runner.show_life() > 0 and Frame.get_time() > 0 and enemy.show_life() == 0):
    endscreen = EndScreen(1)
    print(endscreen.get_text())

else:
    endscreen = EndScreen(2)
    print(endscreen.get_text())


print("GAME OVER !")
quit()
