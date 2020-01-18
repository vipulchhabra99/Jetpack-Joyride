from base_frame import base_frame
import numpy as np
import random
from config import *

class background:

    def __init__(self):
        self.clouds = np.array([[' ','@','@',' '],['@','@','@','@']])

    def place_background(self,Frame):
        
        i = random.randint(20,30)

        while(i < TOTAL_GAME_FRAME - 70):
            j = random.randint(30,50)
            i += j
            y = random.randint(1,3)
            Frame.frame[y+1:y+3,i+1:i+5] = self.clouds
