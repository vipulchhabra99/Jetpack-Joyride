from base_frame import base_frame
import numpy as np
import random
from config import *

class background:

    def __init__(self):
        self.__clouds = np.array([[' ','@','@',' '],['@','@','@','@']])

    def place_background(self,Frame):
        
        i = random.randint(20,30)

        while(i < TOTAL_GAME_FRAME - 70):
            j = random.randint(30,50)
            i += j
            y = random.randint(1,3)
            for xx in range(2):
                for xy in range(4):
                    Frame.set_frame_scene(y+1+xx,i+1+xy,self.__clouds[xx][xy])
