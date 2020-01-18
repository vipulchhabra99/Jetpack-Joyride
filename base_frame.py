import numpy as np
import random
from config import *

class base_frame:

    def __init__(self):
        self.__game_run = True
        self.current_frame = 0
        self.frame = np.array([[' ']*TOTAL_GAME_FRAME]*TOTAL_WIDTH)
        self.user_frame = np.array([[' ']*TOTAL_GAME_FRAME]*TOTAL_WIDTH)
        self.bullets = []
        self.obstacles_placed = []
        self.ice_balls = []

    def generate_boundary(self):
        for i in range(TOTAL_GAME_FRAME):
            self.frame[0][i] = 'X'
        
        for i in range(TOTAL_GAME_FRAME):
            self.frame[TOTAL_WIDTH-1][i] = 'X'


    def getFrame(self):
        return self.current_frame

    def getGameRun(self):
        return self.__game_run




