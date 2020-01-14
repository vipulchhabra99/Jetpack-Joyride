from base_frame import base_frame
import numpy as np
import random

class Obstacles:

    placements = []

    def __init__(self):
       self.__active = True

    def change_status():
        self.__active = False

class horizontal_obstacle(Obstacles):
    
    obstacle = np.array(['=','=','='])

    def change_status(posx,posy):
        self.__active = False
        
        for i in range(3):
            base_frame.frame[posx+i][posy] = ' '

class vertical_obstacle(Obstacles):
    
    
    obstacle = np.array([['|'],['|'],['|']])

    def change_status(posx,posy):
        self.__active = False
        
        for i in range(3):
            base_frame.frame[posx][posy+i] = ' '

class new_obstacle(Obstacles):
    
    obstacle = np.array([['=',' ',' '],[' ','=',' '],[' ',' ','=']])

    def change_status(posx,posy):
        self.__active = False
        
        for i in range(3):
            for j in range(3):
                base_frame.frame[posx+i][posy+j] = ' '


def obstacle_place():

    i = 0;
    ob1 = horizontal_obstacle()
    ob2 = vertical_obstacle()
    ob3 = new_obstacle()
    empty_array = np.array([[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']])

    while(i < 3900):
        j = random.randint(20,30)
        i += j
        y = random.randint(7,25)
        if(np.array_equal(base_frame.frame[y:y+4,i:i+4], empty_array)):
            choice = random.randint(1,3)

            if(choice == 1):
                #base_frame[y+1:y+1,i:i+3] = ob1.obstacle
                for zi in range(3):
                    Obstacles.placements.append([y+1,i+zi])
                    base_frame.frame[y+1][i+zi] = ob1.obstacle[zi]

            elif(choice == 2):
                #base_frame[y:y+3,i+1:i+1] = ob2.obstacle[0:3,0:0]
                for zi in range(3):
                    Obstacles.placements.append([y+1,i+zi])
                    base_frame.frame[y+zi][i+1] = ob2.obstacle[zi][0]

            elif(choice == 3):
                pass
                #base_frame[y:y+3,i:i+3] = ob3().obstacle
                for zi in range(3):
                    for yi in range(3):
                        if(zi == yi):
                            Obstacles.placements.append([y+zi,i+yi])
                        base_frame.frame[y+zi][i+yi] = ob3.obstacle[zi][yi]
