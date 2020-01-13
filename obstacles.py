from base_frame import base_frame
import random
class Obstacles:

    def __init__(self):
       self.__active = True

    def change_status():
        self.__active = False

class horizontal_obstacle(Obstacles):
    obstacle = ['=','=','=']

    def place_obstacles(self):
        obs_posx = random.randint(20,45)
        obs_posy = random.randint(0,26)
        for i in range(3):
            base_frame.frame[obs_posy][obs_posx+base_frame.current_frame+i] = self.obstacle[i]

class vertical_obstacle(Obstacles):
    obstacle = [['||'],['||'],['||']]

    def place_obstacles(self):
        obs_posx = random.randint(20,45)
        obs_posy = random.randint(0,23)
        for i in range(3):
            base_frame.frame[obs_posy+i][obs_posx+base_frame.current_frame] = self.obstacle[i][0]

class new_obstacle(Obstacles):
    obstacle = [['  ','  ','=='],['  ','==','  '],['==','  ','  ']]

    def place_obstacles(self):
        obs_posx = random.randint(20,45)
        obs_posy = random.randint(0,23)
        for i in range(3):
            for j in range(3):
                base_frame.frame[obs_posy+i][obs_posx+base_frame.current_frame+j] = self.obstacle[i][j]