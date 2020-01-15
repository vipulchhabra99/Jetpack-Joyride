from base_frame import base_frame
import numpy as np
import random

class Obstacles:

    def __init__(self,x,y):
        self.active = True
        self.locx = x
        self.locy = y

    def change_status(self,base_frame):
        self.active = False

    def check_status(self):
        return self.active

    def get_x(self):
        return self.locx

    def get_y(self):
        return self.locy


class horizontal_obstacle(Obstacles):

    def __init__(self,x,y):
        self.obstacle = np.array(['=','=','='])
        Obstacles.__init__(self,x,y)

    def change_status(self,posx,posy,base_frame):
        self.active = False
        
        for i in range(3):
            base_frame.frame[posx][posy+i] = ' '
            base_frame.user_frame[posx][posy+i] = ' '

class vertical_obstacle(Obstacles):
    
    def __init__(self,x,y):
        self.obstacle = np.array(['|','|','|'])
        Obstacles.__init__(self,x,y)

    def change_status(self,posx,posy,base_frame):
        self.active = False
        
        for i in range(3):
            base_frame.frame[posx+i][posy] = ' '
            base_frame.user_frame[posx+i][posy] = ' '

class new_obstacle(Obstacles):

    def __init__(self,x,y):
        self.obstacle = np.array(['=','=','='])
        Obstacles.__init__(self,x,y)


    def change_status(self,posx,posy,base_frame):
        self.active = False
        
        for i in range(3):
            base_frame.frame[posx+i][posy+i] = ' '
            base_frame.user_frame[posx+i][posy+i] = ' '



def obstacle_place(Frame):

    i = 0;
    '''ob1 = horizontal_obstacle()
    ob2 = vertical_obstacle()
    ob3 = new_obstacle()'''
    empty_array = np.array([[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']])

    while(i < 3900):
        j = random.randint(10,30)
        i += j
        y = random.randint(7,25)
        if(np.array_equal(Frame.frame[y:y+4,i:i+4], empty_array)):
            choice = random.randint(1,3)

            if(choice == 1):
                Frame.obstacles_placed.append([[y+1,i],[y+1,i+1],[y+1,i+2],horizontal_obstacle(y+1,i)])
                for zi in range(3):
                    Frame.frame[y+1][i+zi] = Frame.obstacles_placed[-1][-1].obstacle[zi]

            elif(choice == 2):
                Frame.obstacles_placed.append([[y,i+1],[y+1,i+1],[y+2,i+1],vertical_obstacle(y,i+1)])
                for zi in range(3):
                    Frame.frame[y+zi][i+1] = Frame.obstacles_placed[-1][-1].obstacle[zi]

            elif(choice == 3):
                pass
                #base_frame[y:y+3,i:i+3] = ob3().obstacle
                Frame.obstacles_placed.append([[y,i],[y+1,i+1],[y+2,i+2],new_obstacle(y,i)])
                for zi in range(3):
                    Frame.frame[y+zi][i+zi] = Frame.obstacles_placed[-1][-1].obstacle[zi]
