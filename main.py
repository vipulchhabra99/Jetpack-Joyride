import os
import numpy as np
import signal
from base_frame import base_frame
from person import Person

Frame = base_frame()
boundary = Frame.generate_boundary()
Runner = Person()

while(True):
    print()
    print("         SCORE : ",end = "   ") 
    print(Runner.show_score(),end = "            ")
    print("             LIFE : ",end = "    ")
    print(Runner.show_life())

    print()

    Runner.generate_person()

    for i in range(100):
        print(boundary[i],end = "")

    for i in range(0,30):
        for j in range(100):
            print(Frame.frame[i][j],end = "")
        print()


    for i in range(100):
        print(boundary[i],end = "")

    print()
    Runner.move_person()
    os.system('clear')
    #print("\033[%d;%dH" % (0, 0))



