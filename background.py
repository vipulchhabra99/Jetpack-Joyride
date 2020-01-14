from base_frame import base_frame
import numpy as np
import random

class background:

    clouds = np.array([[' ','@','@',' '],['@','@','@','@']])

    def place_background(self):
        
        i = random.randint(20,30)

        while(i < 3900):
            j = random.randint(40,50)
            i += j
            y = random.randint(1,3)
            base_frame.frame[y+1:y+3,i+1:i+5] = self.clouds
