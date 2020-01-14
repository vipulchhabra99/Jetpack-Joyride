import os
import numpy as np
import signal
from base_frame import base_frame
from person import Person
from obstacles import horizontal_obstacle,vertical_obstacle,new_obstacle
import random
import sys
from constraint_checker import *
from obstacles import *
np.set_printoptions(threshold=sys.maxsize)


Frame = base_frame()
boundary = Frame.generate_boundary()
Runner = Person()
iteration = 0
ob1 = horizontal_obstacle()
ob2 = vertical_obstacle()
ob3 = new_obstacle()
Runner.place_rewards()
obstacle_place()

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

    Runner.generate_person()
    
    Frame.generate_boundary()

    if(Frame.frame[Runner.positiony][Runner.positionx] == '=' or Frame.frame[Runner.positiony][Runner.positionx] == '|'):
            print("oye")

    for i in range(0,31):
        for j in range(100):
            print(Frame.frame[i][Frame.current_frame+j],end = "")
        print()

    print()

    if(Frame.current_frame >= Runner.positionx):
        Runner.reset_person()
    '''if(iteration%30 == 0):
        x = random.randint(0,2)

        if(x == 0):
            ob1.place_obstacles()

        if(x == 1):
            ob2.place_obstacles()

        if(x == 2):
            ob3.place_obstacles()'''

    #Frame.place_obstacles()
    #score = check_constraint(Runner.positiony,Runner.positionx)
    #print(score)
    #Runner.check_score(score)
    Runner.move_person()
    #os.system('clear')
    iteration += 1
    if(iteration%7 == 0):
        base_frame.current_frame += 1;
    
    if(iteration%(1.5) == 0 and Runner.show_flag() == 0):
        Runner.gravity()
    #print("\033[1;0H")




