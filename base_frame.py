import numpy as np
import random
from config import *
from rewards import *


class base_frame:

    def __init__(self):
        self.__game_run = True
        self.__current_frame = 0
        self.__frame = np.array([[' ']*TOTAL_GAME_FRAME]*TOTAL_WIDTH)
        self.__user_frame = np.array([[' ']*TOTAL_GAME_FRAME]*TOTAL_WIDTH)
        self.__bullets = []
        self.__obstacles_placed = []
        self.__ice_balls = []
        self.__time_remaining = 570

    def get_obstacles(self):
        return self.__obstacles_placed

    def get_bullets(self):
        return self.__bullets

    def get_frame_scene(self):
        return self.__frame

    def get_particular_frame(self,posx,posy):
        return self.__frame[posx][posy]

    def get_user_frame(self):
        return self.__user_frame

    def set_frame_scene(self,i,j,value):
        self.__frame[i][j] = value

    def set_user_frame(self,i,j,value):
        self.__user_frame[i][j] = value

    def get_particular_user_frame(self,i,j):
        return self.__user_frame[i][j]

    def generate_boundary(self):
        for i in range(TOTAL_GAME_FRAME):
            self.__frame[0][i] = 'X'

        for i in range(TOTAL_GAME_FRAME):
            self.__frame[TOTAL_WIDTH-1][i] = 'X'

    def add_bullet(self, Bullet):
        self.__bullets.append(Bullet)

    def add_obstacles(self, Obstacles):
        self.__obstacles_placed.append(Obstacles)

    def add_ice_balls(self, ice_ball):
        self.__ice_balls.append(ice_ball)

    def get_ice_balls(self):
        return self.__ice_balls

    def get_frame(self):
        return self.__current_frame

    def increase_frame(self):
        self.__current_frame += 1

    def decrease_time(self):
        self.__time_remaining -= 1

    def get_time(self):
        return self.__time_remaining

    def getGameRun(self):
        return self.__game_run

    def place_rewards(self):
        # self.generate_series()
        i = 10
        j = 0

        while(i < TOTAL_GAME_FRAME-220):

            choice = random.randint(1, 4)
            # Random location to place on frame
            j = random.randint(10, 25)
            i += j

            if(choice != 4):
                # Rewards Object
                reward = Rewards()
                reward.generate_series()
                reward.set_choice(choice)

                if choice == 1:
                    y = random.randint(6, 20)
                    self.__frame[y:y+3, i:i+8] = reward.get_series1()

                elif choice == 2:
                    y = random.randint(6, 23)
                    self.__frame[y, i:i+8] = reward.get_series2()

                elif choice == 3:
                    y = random.randint(6, 20)
                    self.__frame[y:(y+8), i:(i+8)] = reward.get_series3()

            else:

                reward = speed_boost()
                y = random.randint(4, 24)
                self.__frame[y][i] = reward.get_boost()
