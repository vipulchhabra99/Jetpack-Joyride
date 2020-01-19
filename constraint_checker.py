from base_frame import base_frame
import numpy as np
from obstacles import Obstacles


def check_constraint(posx, posy, base_frame):

    score = 0

    if(base_frame.frame[posx][posy] == '$'):
        score += 1
        base_frame.frame[posx][posy] = ' '
        base_frame.user_frame[posx][posy] = ' '

    if(base_frame.frame[posx][posy+1] == '$'):
        score += 1
        base_frame.frame[posx][posy+1] = ' '
        base_frame.user_frame[posx][posy+1] = ' '

    if(base_frame.frame[posx][posy+2] == '$'):
        score += 1
        base_frame.frame[posx][posy+2] = ' '
        base_frame.user_frame[posx][posy+2] = ' '

    if(base_frame.frame[posx+1][posy] == '$'):
        score += 1
        base_frame.frame[posx+1][posy] = ' '
        base_frame.user_frame[posx+1][posy] = ' '

    if(base_frame.frame[posx+1][posy+1] == '$'):
        score += 1
        base_frame.frame[posx+1][posy+1] = ' '
        base_frame.user_frame[posx+1][posy+1] = ' '

    if(base_frame.frame[posx+1][posy+2] == '$'):
        score += 1
        base_frame.frame[posx+1][posy+2] = ' '
        base_frame.user_frame[posx+1][posy+2] = ' '

    if(base_frame.frame[posx+2][posy] == '$'):
        score += 1
        base_frame.frame[posx+2][posy] = ' '
        base_frame.user_frame[posx+2][posy] = ' '

    if(base_frame.frame[posx+2][posy+1] == '$'):
        score += 1
        base_frame.frame[posx+2][posy+1] = ' '
        base_frame.user_frame[posx+2][posy+1] = ' '

    if(base_frame.frame[posx+2][posy+2] == '$'):
        score += 1
        base_frame.frame[posx+2][posy+2] = ' '
        base_frame.user_frame[posx+2][posy+2] = ' '

    return score


def check_obstacle(posx, posy, Frame):

    for obs in Frame.obstacles_placed:
        for i in range(3):
            for j in range(3):
                if(obs[3].check_status() is True and [posx+i, posy+j] in obs[0:3]):
                    return 2


def bullet_collision(posx, posy, Frame, Enemy):
    for obs in Frame.obstacles_placed:
        if(obs[3].check_status() is True and ([posx, posy] in obs[0:3] or [posx, posy-1] in obs[0:3] or [posx, posy+1] in obs[0:3])):
            obs[3].remove_obstacle(obs[3].get_x(), obs[3].get_y(), Frame)
            return 2


def iceball_collision(posx, posy, Frame, Person):

    for i in range(3):
        for j in range(3):
            if((Person.get_y()+i) == posx and (Person.get_x()+j) == posy):
                return 2


def dragon_bullet(posx, posy, Enemy):

    for i in range(8):
        for j in range(30):
            if(Enemy.get_y()+i == posy and Enemy.get_x()+j == posx):
                return 3


def speedboost_check(posx, posy, Frame):

    for i in range(3):
        for j in range(3):
            if(Frame.frame[posx+i][posy+j] == 'S'):
                Frame.frame[posx+i][posy+j] = ' '
                Frame.user_frame[posx+i][posy+j] = ' '
                return True
