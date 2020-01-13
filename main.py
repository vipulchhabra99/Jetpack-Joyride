import os
import numpy as np
import signal
from base_frame import base_frame
from person import Person
from obstacles import horizontal_obstacle,vertical_obstacle,new_obstacle
import random
import sys
np.set_printoptions(threshold=sys.maxsize)


Frame = base_frame()
boundary = Frame.generate_boundary()
Runner = Person()
iteration = 0
ob1 = horizontal_obstacle()
ob2 = vertical_obstacle()
ob3 = new_obstacle()

while(True):
    print("\033[0;0f")
    print()
    print()
    print("                SCORE : ",end = "   ") 
    print(Runner.show_score(),end = "            ")
    print("               LIFE : ",end = "    ")
    print(Runner.show_life())

    print()

    Runner.generate_person()
    Frame.generate_boundary()

    for i in range(0,31):
        for j in range(80):
            print(Frame.frame[i][Frame.current_frame+j],end = "")
        print()

    print()
    '''if(iteration%30 == 0):
        x = random.randint(0,2)

        if(x == 0):
            ob1.place_obstacles()

        if(x == 1):
            ob2.place_obstacles()

        if(x == 2):
            ob3.place_obstacles()'''

    #Frame.place_obstacles()
    Runner.move_person()
    #constraint_checker()
    #os.system('clear')
    iteration += 1
    if(iteration%7 == 0):
        base_frame.current_frame += 1;
    
    if(iteration%2 == 0):
        Runner.gravity()
    #print("\033[1;0H")




