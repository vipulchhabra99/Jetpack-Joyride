from base_frame import base_frame
import numpy as np
import random
from config import *

class Obstacles:

    def __init__(self,x,y):
        self.__active = True
        self.__locx = x
        self.__locy = y

    def change_status(self):
        self.__active = False

    def check_status(self):
        return self.__active

    def set_x(self,value):
        self.__locx = value

    def set_y(self,value):
        self.__locy = value

    def get_x(self):
        return self.__locx

    def get_y(self):
        return self.__locy


class horizontal_obstacle(Obstacles):

    def __init__(self,x,y):
        self.__obstacle = np.array(['=','=','='])
        Obstacles.__init__(self,x,y)

    def get_obstacle(self):
        return self.__obstacle

    def remove_obstacle(self,posx,posy,base_frame):
        self.change_status()
        for i in range(3):
            base_frame.frame[posx][posy+i] = ' '
            base_frame.user_frame[posx][posy+i] = ' '

class vertical_obstacle(Obstacles):
    
    def __init__(self,x,y):
        self.__obstacle = np.array(['|','|','|'])
        Obstacles.__init__(self,x,y)

    def get_obstacle(self):
        return self.__obstacle

    def remove_obstacle(self,posx,posy,base_frame):
        self.change_status()
        for i in range(3):
            base_frame.frame[posx+i][posy] = ' '
            base_frame.user_frame[posx+i][posy] = ' '

class new_obstacle(Obstacles):

    def __init__(self,x,y):
        self.__obstacle = np.array(['=','=','='])
        Obstacles.__init__(self,x,y)

    def get_obstacle(self):
        return self.__obstacle

    def remove_obstacle(self,posx,posy,base_frame):
        self.change_status()
        
        for i in range(3):
            base_frame.frame[posx+i][posy+i] = ' '
            base_frame.user_frame[posx+i][posy+i] = ' '

class Magnet(Obstacles):

    def __init__(self,x,y):
        self.__magnet = np.array([['|','=','|'],['|',' ','|']])
        Obstacles.__init__(self,x,y)

    def get_magnet(self):
        return self.__magnet

    def magnet_on_frame(self,Frame):
        for i in range(2):
            for j in range(3):
                Frame.user_frame[self.get_y()+i][self.get_x()+j] = self.__magnet[i][j]

    def forward(self):
        self.set_x(self.get_x()+MAGNET_SPEED)


def obstacle_place(Frame):

    i = 0;

    empty_array = np.array([[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']])

    while(i < TOTAL_GAME_FRAME-200):
        j = random.randint(10,30)
        i += j
        y = random.randint(7,25)
        if(np.array_equal(Frame.frame[y:y+4,i:i+4], empty_array)):
            choice = random.randint(1,3)

            if(choice == 1):
                Frame.obstacles_placed.append([[y+1,i],[y+1,i+1],[y+1,i+2],horizontal_obstacle(y+1,i)])
                for zi in range(3):
                    Frame.frame[y+1][i+zi] = Frame.obstacles_placed[-1][-1].get_obstacle()[zi]

            elif(choice == 2):
                Frame.obstacles_placed.append([[y,i+1],[y+1,i+1],[y+2,i+1],vertical_obstacle(y,i+1)])
                for zi in range(3):
                    Frame.frame[y+zi][i+1] = Frame.obstacles_placed[-1][-1].get_obstacle()[zi]

            elif(choice == 3):
                pass
                #base_frame[y:y+3,i:i+3] = ob3().obstacle
                Frame.obstacles_placed.append([[y,i],[y+1,i+1],[y+2,i+2],new_obstacle(y,i)])
                for zi in range(3):
                    Frame.frame[y+zi][i+zi] = Frame.obstacles_placed[-1][-1].get_obstacle()[zi]
