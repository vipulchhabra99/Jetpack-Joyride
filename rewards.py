from base_frame import base_frame 
import random
import numpy as np

class Rewards: 

    def __init__(self):
         self.__value = 1
         self.__coins = ["$"]
         self.__series1 = []
         self.__series2 = []
         self.__series3 = []

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

        #print(self.__series2)

        for i in range(8):
            inter_row = []
            for j in range(8):
                if(i == j):
                    inter_row.append(self.__coins[0])
                else:
                    inter_row.append(" ")
            self.__series3.append(inter_row)
        
        self.__series3 = np.array(self.__series3)

    def board_place(self):

        self.generate_series()
        
        i = 10
        j = 0

        while(i < 3900):
            
            choice = random.randint(1, 3)
            j = random.randint(30,40)
            i += j

            if choice == 1:
                y = random.randint(6,20)
                base_frame.frame[y:y+3,i:i+8] = self.__series1
                #for xi in range(3):
                    #for zi in range(8):
                        #base_frame.frame[y+xi][i+zi] = self.__series1[xi][zi]
                        #print(self.__series1[xi][zi])

            elif choice == 2:
                y = random.randint(6,23)

                base_frame.frame[y,i:i+8] = self.__series2    
                #for zi in range(8):
                    #print(self.__series2[zi])

                        #base_frame.frame[y+xi][i+zi] = self.__series2[xi][zi]
                #base_frame.frame[y:(y+1),i:(i+8)] = self.__series2

            elif choice == 3:
                y = random.randint(6,23)
                #for xi in range(8):
                    #for zi in range(8):
                        #print(self.__series3[xi][zi])
                        #base_frame.frame[y+xi][i+zi] = self.__series3[xi][zi]
                base_frame.frame[y:(y+8),i:(i+8)] = self.__series3

