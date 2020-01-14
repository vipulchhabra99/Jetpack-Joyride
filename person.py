from input import _getChUnix as getChar
from base_frame import base_frame
import signal
import numpy as np
from rewards import Rewards
from alarmexception import AlarmException
from constraint_checker import *

class Bullet:
    
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.bullet = '*'
        self.veocityx = 2

    def on_frame(self,x):
        base_frame.user_frame[self.__y][x] = self.bullet

    def forward(self):
        self.__x += self.veocityx

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def detect_collision(self):
        if(bullet_collision(self.__y,self.__x) == 2):
            print("collision detected")


class Person:

    positiony = 27
    positionx = 0

    def __init__(self):
        self.person = np.array([[' ','@',' '],['-','|','-'],['/',' ','\\']])
        self.__power = 20
        self.__score = 0
        self.__shield = 0
        self.__jetflag = 0
        self.__bulletflag = 0
        self.rew = Rewards()

    def show_score(self):
        scr = self.__score
        return scr

    def check_score(self,score):
        self.__score += score

    def increase_shield(self):
        self.__shield += 1
    
    def show_shield(self):
        return self.__shield

    def show_flag(self):
        return self.__jetflag

    def place_rewards(self):
        self.rew.board_place()


    def generate_person(self):

        if(base_frame.current_frame < self.positionx):
            base_frame.user_frame[self.positiony:self.positiony+3,self.positionx:self.positionx+3] = self.person

        else:
            self.positionx = base_frame.current_frame
            base_frame.user_frame[self.positiony:self.positiony+3,base_frame.current_frame:base_frame.current_frame+3] = self.person

    def show_life(self):
        return self.__power

    def reset_person(self):
        if(base_frame.current_frame <= self.positionx):
            #print(base_frame.frame[self.positiony:self.positiony+3,self.positionx:self.positionx+3])
            base_frame.user_frame[self.positiony:self.positiony+3,self.positionx:self.positionx+3] = " "

        else:
            #print(base_frame.frame[self.positiony:self.positiony+3,self.positionx:self.positionx+3])
            base_frame.user_frame[self.positiony:self.positiony+3,base_frame.current_frame:base_frame.current_frame+3] = " "        

    def gravity(self):
        if(self.positiony < 27):
            if(check_obstacle(self.positiony+1,self.positionx)):
                print("GAME OVER !")
                quit()
            self.__score += check_constraint(self.positiony+1,self.positionx)
            self.reset_person()
            self.positiony += 1


    def move_person(self):
        def alarmhandler(signum, frame):
            raise AlarmException

        def user_input(timeout=0.1):
            """input method."""
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        char = user_input()

        # Press 'q' for quit.
        if char == 'q':
            quit()

        elif char == 'd':
            if(self.positionx - base_frame.current_frame < 97):
                if(check_obstacle(self.positiony,self.positionx+1)):
                    print("GAME OVER !")
                    quit()
                self.__score += check_constraint(self.positiony,self.positionx+1)
                self.reset_person()
                self.__jetflag = 0
                self.positionx += 1
        
        elif char == 'w':
            if(self.positiony > 1):
                if(check_obstacle(self.positiony-1,self.positionx)):
                    print("GAME OVER !")
                    quit()
                self.__score += check_constraint(self.positiony-1,self.positionx)                
                self.reset_person()
                self.positiony -=1
                self.__jetflag = 1

        elif char == 's':
            if(self.positiony < 27):
                if(check_obstacle(self.positiony+1,self.positionx)):
                    print("GAME OVER !")
                    quit()
                self.__score += check_constraint(self.positiony+1,self.positionx)
                self.reset_person()
                self.positiony += 1

        elif char == 'a':
            if(self.positionx - base_frame.current_frame > 0):
                if(check_obstacle(self.positiony,self.positionx-1)):
                    print("GAME OVER !")
                    quit()
                self.__score += check_constraint(self.positiony,self.positionx-1)               
                self.reset_person()
                self.__jetflag = 0
                self.positionx -= 1
        elif char == 'b':
            self.__jetflag = 0
            base_frame.bullets.append(Bullet(self.positionx+1,self.positiony+1))

        else:
            self.__jetflag = 0