import numpy as np
import random

class base_frame:

    current_frame = 0
    frame = np.array([[' ']*4500]*50)
    user_frame = np.array([[' ']*4500]*50)

    def generate_boundary(self):
        for i in range(4000):
            self.frame[0][self.current_frame+i] = 'X'
        
        for i in range(4000):
            self.frame[30][self.current_frame+i] = 'X'


    def getFrame(self):
        return self.current_frame

