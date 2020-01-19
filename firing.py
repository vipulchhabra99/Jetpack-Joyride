from base_frame import *

class Bullet:
    
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__bullet = '*'
        self.__velocityx = BULLET_VELOCITY
        self.__status = True

    def on_frame(self,x,Frame):
        Frame.user_frame[self.__y][x] = self.__bullet

    def forward(self):
        self.__x += self.__velocityx

    def change_status(self):
        self.__status = False

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self,value):
        self.__x = value

    def get_status(self):
        return self.__status
    
    def bullet_remove(self,Frame):
        Frame.user_frame[self.__y][self.__x] = ' '
        self.__status = False

    def bullet_collision(self, posx, posy, Frame, Enemy):
        for obs in Frame.obstacles_placed:
            if(obs[3].check_status() is True and ([posx, posy] in obs[0:3] or [posx, posy-1] in obs[0:3] or [posx, posy+1] in obs[0:3])):
                obs[3].remove_obstacle(obs[3].get_x(), obs[3].get_y(), Frame)
                return 2

    def dragon_bullet(self, posx, posy, Enemy):
        for i in range(8):
            for j in range(30):
                if(Enemy.get_y()+i == posy and Enemy.get_x()+j == posx):
                    return 3

    def detect_collision(self,Frame,Enemy):
        if(self.bullet_collision(self.__y,self.__x,Frame,Enemy) == 2):
            self.bullet_remove(Frame)

        else:
            if(self.dragon_bullet(self.__x,self.__y,Enemy) == 3):
                self.bullet_remove(Frame)
                Enemy.decrease_life()
        

class Iceballs(Bullet):
    
    def __init__(self,x,y):
        Bullet.__init__(self,x,y)
        self.__iceballs= '#'
        self.__velocity = ICE_BALL_VELOCITY

    def on_frame(self,Frame):
        Frame.user_frame[self.get_y()][self.get_x()] = self.__iceballs

    def forward(self):
        self.set_x(self.get_x()-self.__velocity)

    def iceball_collision(self,posx, posy, Frame, Person):
    
        for i in range(3):
            for j in range(3):
                if((Person.get_y()+i) == posx and (Person.get_x()+j) == posy):
                    return 2

    def check_collision(self,Frame,Person):
        if(self.iceball_collision(self.get_y(),self.get_x(),Frame,Person) == 2):
            Person.decrease_life()
            self.change_status()

