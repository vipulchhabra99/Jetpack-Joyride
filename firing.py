from base_frame import *
from constraint_checker import *

class Bullet:
    
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__bullet = '*'
        self.__velocityx = 2
        self.status = True

    def on_frame(self,x,Frame):
        Frame.user_frame[self.__y][x] = self.__bullet

    def forward(self):
        self.__x += self.__velocityx

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
    def bullet_remove(self,Frame):
        Frame.user_frame[self.__y][self.__x] = ' '
        self.status = False

    def detect_collision(self,Frame,Enemy):
        if(bullet_collision(self.__y,self.__x,Frame,Enemy) == 2):
            self.bullet_remove(Frame)

        else:
            if(dragon_bullet(self.__x,self.__y,Enemy) == 3):
                self.bullet_remove(Frame)
                Enemy.decrease_life()
        

class Iceballs:
    
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__iceballs= '#'
        self.status = True
        self.velocity = ICE_BALL_VELOCITY

    def get_x(self):
        return self.__x

    def get_status(self):
        return self.status

    def on_frame(self,Frame):
        Frame.user_frame[self.__y][self.__x] = self.__iceballs

    def forward(self):
        self.__x -= ICE_BALL_VELOCITY

    def check_collision(self,Frame,Person):
        if(iceball_collision(self.__y,self.__x,Frame,Person) == 2):
            Person.decrease_life()
            self.status = False

