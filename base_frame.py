import numpy as np
class base_frame:

    current_frame = 0
    frame = np.array([[""]*4002]*100)

    def generate_boundary(self):
        boundary = np.array(['X']*100)
        return boundary


    def print_base_frame(self):
        print()
        print("         SCORE : ",end = "   ") 
        print(Frame.show_score(),end = "            ")

    def getFrame(self):
        return self.current_frame

