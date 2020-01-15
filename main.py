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
np.set_printoptions(threshold=sys.maxsize)

def bullet_printer(base_frame):
    for bullet in base_frame.bullets:
        if(base_frame.current_frame <= bullet.get_x() < base_frame.current_frame+100 and bullet.status == True):
            bullet.forward()
            bullet.detect_collision(base_frame)
            #print(bullet.get_x())
            bullet.on_frame(bullet.get_x(),base_frame)


Frame = base_frame()
boundary = Frame.generate_boundary()
Runner = Person()
iteration = 0
Runner.place_rewards(Frame)
obstacle_place(Frame)
cloud = background()
cloud.place_background(Frame)

while(True):
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

    for i in range(0,31):
        for j in range(100):
            Frame.user_frame[i][Frame.current_frame+j] = Frame.frame[i][Frame.current_frame+j]

    Runner.generate_person(Frame)
    bullet_printer(Frame)
    
    for i in range(0,31):
        for j in range(100):
            print(Frame.user_frame[i][Frame.current_frame+j],end = "")
        print()

    print()

    if(Frame.current_frame >= Runner.positionx):
        Runner.reset_person(Frame)

    #Frame.place_obstacles()
    #score = check_constraint(Runner.positiony,Runner.positionx)
    #print(score)
    #Runner.check_score(score)
    Runner.move_person(Frame)
    #os.system('clear')
    iteration += 1
    if(iteration%7 == 0):
        Frame.current_frame += 1;
    
    if(iteration%(1.5) == 0 and Runner.show_flag() == 0):
        Runner.gravity(Frame)
    #print("\033[1;0H")




