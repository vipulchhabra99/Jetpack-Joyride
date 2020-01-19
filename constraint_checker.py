from base_frame import base_frame
import numpy as np
from obstacles import Obstacles

def iceball_collision(posx, posy, Frame, Person):

    for i in range(3):
        for j in range(3):
            if((Person.get_y()+i) == posx and (Person.get_x()+j) == posy):
                return 2

def speedboost_check(posx, posy, Frame):

    for i in range(3):
        for j in range(3):
            if(Frame.frame[posx+i][posy+j] == 'S'):
                Frame.frame[posx+i][posy+j] = ' '
                Frame.user_frame[posx+i][posy+j] = ' '
                return True
