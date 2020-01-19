import random
import numpy as np
from config import *
from colorama import Fore, Back, Style 


class speed_boost:
    
    def __init__(self):
        self.__boost = 'S'

    def get_boost(self):
        return self.__boost

class Rewards: 

    def __init__(self):
         self.__value = 1
         self.__coins = ["$"]
         self.__series1 = []
         self.__series2 = []
         self.__series3 = []
         self.__choice = 0

    def generate_series(self):
        for i in range(3):
            inter_row = []
            for j in range(8):
                inter_row.append(self.__coins[0])
            self.__series1.append(inter_row)

        self.__series1 = np.array(self.__series1)

        for i in range(8):
            self.__series2.append(self.__coins[0])

        self.__series2 = np.array(self.__series2)

        for i in range(8):
            inter_row = []
            for j in range(8):
                if(i == j):
                    inter_row.append(self.__coins[0])
                else:
                    inter_row.append(" ")
            self.__series3.append(inter_row)
        
        self.__series3 = np.array(self.__series3)

    def get_series1(self):
        return self.__series1

    def get_series2(self):
        return self.__series2

    def get_series3(self):
        return self.__series3

    def set_choice(self,choice):
        self.__choice = choice

    def get_choice(self):
        return self.__choice