import numpy as np
import random

class base_frame:

    current_frame = 0
    frame = np.array([['  ']*1000]*50)

    def generate_boundary(self):
        for i in range(100):
            self.frame[0][self.current_frame+i] = 'XX'
        
        for i in range(100):
            self.frame[30][self.current_frame+i] = 'XX'


    def getFrame(self):
        return self.current_frame

