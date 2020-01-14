from base_frame import base_frame
import numpy as np
from obstacles import Obstacles

def check_constraint(posx, posy):

    score = 0

    if(base_frame.user_frame[posx][posy] == '$'):
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

def check_obstacle(posx,posy):

    for i in range(3):
        for j in range(3):
            if([posx+i,posy+j] in Obstacles.placements):
                return 2

def bullet_collision(posx,posy):

    if([posx,posy] in Obstacles.placements):
        quit()