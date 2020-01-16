import os
import numpy as np
import signal
from base_frame import base_frame
from person import *
from obstacles import horizontal_obstacle,vertical_obstacle,new_obstacle
from background import background
import random
import sys
from constraint_checker import *
from obstacles import *
from config import *
np.set_printoptions(threshold=sys.maxsize)

def bullet_printer(base_frame):
    for bullet in base_frame.bullets:
        if(base_frame.current_frame <= bullet.get_x() < base_frame.current_frame+100 and bullet.status == True):
            bullet.forward()
            bullet.detect_collision(base_frame)
            #print(bullet.get_x())
            bullet.on_frame(bullet.get_x(),base_frame)

def magnet_printer(magnet,frame):
    magnet.magnet_on_frame(frame)
        


Frame = base_frame()
boundary = Frame.generate_boundary()
Runner = Person()
iteration = 0
Runner.place_rewards(Frame)
Runner.place_speedboost(Frame)
obstacle_place(Frame)
cloud = background()
cloud.place_background(Frame)
magnet = Magnet(random.randint(MAGNET_LOCATION_MIN,MAGNET_LOCATION_MAX),MAGNET_LOC_Y)
mag_loc = magnet.get_x()
Runner.magnetlocx = magnet.get_x()
magnet_period = 0
boost_check = 0
enemy = Enemy()

while(Frame.getGameRun()):
    print("\033[0;0f")
    print()
    print()
    print("     SCORE : ",end = "   ") 
    print(Runner.show_score(),end = "        ")
    print("      LIFE : ",end = "    ")
    print(Runner.show_life(),end = "        ")
    print("      SHIELD : ",Runner.show_shield(),end = '    ')
    print("    TIME REMAINING : ",0)
    
    print()


    for i in range(TOTAL_WIDTH):
        for j in range(FRAME_PER_SCENE):
            Frame.user_frame[i][Frame.current_frame+j] = Frame.frame[i][Frame.current_frame+j]

    Runner.generate_person(Frame)
    bullet_printer(Frame)

    if(Frame.current_frame <= mag_loc < Frame.current_frame+80 and magnet_period < 300):
        magnet_printer(magnet,Frame)
        Runner.set_magnet()
        magnet_period += 1
        
        if(Runner.check_boost() == True and boost_check < 200):
            if(iteration % 2 == 0):
                magnet.forward()
                Runner.magnetlocx = magnet.get_x()
                Runner.positionx = magnet.get_x()
    

        else:
            if(iteration % 6 == 0):
                magnet.forward()
                Runner.magnetlocx = magnet.get_x()
                Runner.positionx = magnet.get_x()

    if(magnet_period > 300):
        Runner.reset_magnet()

    if(Frame.current_frame > 50):
        enemy.place_dragon(Frame,Runner)


    for i in range(TOTAL_WIDTH):
        for j in range(FRAME_PER_SCENE):
            print(Frame.user_frame[i][Frame.current_frame+j],end = "")
        print()

    print()

    if(Frame.current_frame >= Runner.positionx):
        Runner.reset_person(Frame)

    if(Runner.show_shield() < 20 and Runner.check_shield() == False):
        if(iteration % 6 == 0):
            Runner.increase_shield()

    elif(Runner.show_shield() == 0 and Runner.check_shield() == True):
        Runner.deactivate_shield()

    elif(Runner.check_shield() == True):
        if(iteration % 2 == 0):
            Runner.decrease_shield()

        

    #Frame.place_obstacles()
    #score = check_constraint(Runner.positiony,Runner.positionx)
    #print(score)
    #Runner.check_score(score)
    Runner.move_person(Frame)
    #os.system('clear')
    iteration += 1

    #print(Runner.check_boost())

    if(Runner.check_boost() == True and boost_check < 200):
        if(iteration % 2 == 0 and Frame.current_frame < STATIC_FRAME):
            Frame.current_frame += 1
        boost_check += 1
    else:
        boost_check = 0
        Runner.change_boostflag()
        if(iteration%5 == 0 and Frame.current_frame < STATIC_FRAME):
            Frame.current_frame += 1
    
    if(iteration%(1.5) == 0 and Runner.show_flag() == 0):
        Runner.gravity(Frame)
    #print("\033[1;0H")




