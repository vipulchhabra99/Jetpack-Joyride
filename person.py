from input import _getChUnix as getChar
from base_frame import base_frame
import signal
import numpy as np
from rewards import *
from alarmexception import AlarmException
from constraint_checker import *
from config import *
from firing import *

class Person:

    def __init__(self):
        self.__person = np.array([[' ','@',' '],['-','|','-'],['/',' ','\\']])
        self.__life = 20
        self.__score = 0
        self.__shield = 0
        self.__jetflag = 0
        self.__bulletflag = 0
        self.__magnetflag = False
        self.__boost = False
        self.__positiony = 27
        self.__positionx = 0
        self.__magnetposx = 0
        self.__shield_activate = False

    def get_person(self):
        return self.__person

    def get_magnetx(self):
        return self.__magnetposx

    def set_magnetx(self,value):
        self.__magnetposx = value

    def get_x(self):
        return self.__positionx

    def set_x(self,value):
        self.__positionx = value

    def get_y(self):
        return self.__positiony

    def set_y(self,value):
        self.__positiony = value

    def deactivate_shield(self):
        self.__shield_activate = False

    def check_shield(self):
        return self.__shield_activate

    def show_shield(self):
        return self.__shield

    def decrease_shield(self):
        self.__shield -= 1

    def increase_shield(self):
        self.__shield += 1

    def check_boost(self):
        return self.__boost

    def change_boostflag(self):
        self.__boost = False

    def show_score(self):
        scr = self.__score
        return scr

    def check_score(self,score):
        self.__score += score

    def set_magnet(self):
        self.__magnetflag = True

    def reset_magnet(self):
        self.__magnetflag = False
    
    def check_magnet_flag(self):
        return self.__magnetflag
    
    def show_flag(self):
        return self.__jetflag

    def generate_person(self,base_frame,Enemy):

        if(DRAGON_PLACE_X-2 > self.__positionx):

            if(base_frame.get_frame() < self.__positionx):
                base_frame.user_frame[self.__positiony:self.__positiony+3,self.__positionx:self.__positionx+3] = self.__person

            else:
                self.__positionx = base_frame.get_frame()
                base_frame.user_frame[self.__positiony:self.__positiony+3,base_frame.get_frame():base_frame.get_frame()+3] = self.__person

        else:
            self.__positionx = DRAGON_PLACE_X-3
            if(base_frame.get_frame() < self.__positionx):
                base_frame.user_frame[self.__positiony:self.__positiony+3,self.__positionx:self.__positionx+3] = self.__person

            else:
                self.__positionx = base_frame.get_frame()
                base_frame.user_frame[self.__positiony:self.__positiony+3,base_frame.get_frame():base_frame.get_frame()+3] = self.__person

    def show_life(self):
        return self.__life

    def decrease_life(self):
        self.__life -= 1

    def reset_person(self,base_frame):
        if(base_frame.get_frame() <= self.__positionx):
            base_frame.user_frame[self.__positiony:self.__positiony+3,self.__positionx:self.__positionx+3] = " "

        else:
            base_frame.user_frame[self.__positiony:self.__positiony+3,base_frame.get_frame():base_frame.get_frame()+3] = " "        

    def gravity(self,Frame):
        if(self.__positiony < 27):
            if(check_obstacle(self.__positiony+1,self.__positionx,Frame) and self.__shield_activate is False):
                print("GAME OVER !")
                quit()
            self.__score += check_constraint(self.__positiony+1,self.__positionx,Frame)
            if(speedboost_check(self.__positiony+1,self.__positionx,Frame)):
                self.__boost = True
            self.reset_person(Frame)
            self.__positiony += 1


    def move_person(self,Frame):
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
            if(self.__positionx - Frame.get_frame() < 97):
                if(check_obstacle(self.__positiony,self.__positionx+1,Frame) and self.__shield_activate is False):
                    print("GAME OVER !")
                    quit()
                self.__score += check_constraint(self.__positiony,self.__positionx+1,Frame)
                if(speedboost_check(self.__positiony,self.__positionx+1,Frame)):
                    self.__boost = True
                self.reset_person(Frame)
                self.__jetflag = 0
                self.__positionx += 1
        
        elif char == 'w':
            if(self.__positiony > 1):
                if(check_obstacle(self.__positiony-1,self.__positionx,Frame) and self.__shield_activate is False):
                    print("GAME OVER !")
                    quit()
                self.__score += check_constraint(self.__positiony-1,self.__positionx,Frame)
                if(speedboost_check(self.__positiony-1,self.__positionx,Frame)):
                    self.__boost = True                                
                self.reset_person(Frame)
                self.__positiony -=1
                self.__jetflag = 1

        elif char == 's':
            if(self.__positiony < 27):
                if(check_obstacle(self.__positiony+1,self.__positionx,Frame) and self.__shield_activate is False):
                    print("GAME OVER !")
                    quit()
                self.__score += check_constraint(self.__positiony+1,self.__positionx,Frame)
                if(speedboost_check(self.__positiony+1,self.__positionx,Frame)):
                    self.__boost = True 
                self.reset_person(Frame)
                self.__positiony += 1

        elif char == 'a':
            if(self.__positionx - Frame.get_frame() > 0):
                if(check_obstacle(self.__positiony,self.__positionx-1,Frame) and self.__shield_activate is False):
                    print("GAME OVER !")
                    quit()
                self.__score += check_constraint(self.__positiony,self.__positionx-1,Frame)               
                if(speedboost_check(self.__positiony,self.__positionx-1,Frame)):
                    self.__boost = True                
                self.reset_person(Frame)
                self.__jetflag = 0
                self.__positionx -= 1
        elif char == 'b':
            self.__jetflag = 0
            Frame.bullets.append(Bullet(self.__positionx+1,self.__positiony+1))

        elif char.isspace():
            self.__jetflag = 0
            if(self.__shield == 20):
                self.__shield_activate = True

        else:
            self.__jetflag = 0


class Enemy(Person):

    def __init__(self):
        self.__drgaon = [[' ', ' ', ' ', ';', '.', '_', "'", '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', '-', "'",' ',' ',' ',' ',' ',' '],[' ', ' ', ' ', '(', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '-', '.', '/', ' ', ';', '.', '-', ';',' ',' ',' ',' '],[' ', ' ', ' ', ' ', ';', ' ', '_', ' ', ' ', ' ', ' ', ' ', ' ', '|', "'", '-', '-', ',', '|', ' ', '`', ' ', ' ', "'", '<', ' ', '_', '_', '_', ','],[' ', ' ', ' ', ' ', ' ', ' ', '_', '_', ')', ' ', ' ', ' ', ' ', ' ', '\\', '`', '-', '.', '_', '_', '.', ' ', ' ', ' ', '/', '`', '.', '-', "'", '/'],[' ', ' ', ' ', ' ', '{', ';', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '/', 'o', '(', 'o', ' ', '\\', ' ', '|', ' ', '/', ' ', ',', "'",' '],[' ', ' ', ' ', ' ', ' ', ' ', ';', ' ', ' ', '_', ' ', ' ', '_', '_', '.', '-', "'", '-', "'", '`', '-', "'", ' ', ' ', "'", '`',' ',' ',' ',' '],[' ', ' ', ' ', ' ', ' ', ' ', "'", ' ', '(', '-', ',', '`', ' ', ' ', '.', '-', '.', ' ', ' ', ' ', ' ', ' ', '_', ' ', '-', '.',' ',' ',' ',' '],[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '_', ')', ')', ' ', ' ', '_', '/', ' ', ' ', ' ', ' ', '|',' ',' ',' ']]
        Person.__init__(self)
        self.set_x(DRAGON_PLACE_X)
        self.set_y(TOTAL_WIDTH-9)

    def place_dragon(self,Frame,Person):
        locs = 0
        locs = Person.get_y()+random.randint(-3,3)
        if(locs < 22):
            self.set_y(locs)
            Frame.user_frame[locs:locs+8,DRAGON_PLACE_X:DRAGON_PLACE_X+30] = self.__drgaon

        else:
            self.set_y(TOTAL_WIDTH-9)
            Frame.user_frame[TOTAL_WIDTH-9:TOTAL_WIDTH-1,DRAGON_PLACE_X:DRAGON_PLACE_X+30] = self.__drgaon

    def fire_ice(self,Frame):
        Frame.ice_balls.append(Iceballs(self.get_x()+1,self.get_y()+5))

