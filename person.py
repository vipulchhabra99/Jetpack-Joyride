"""Person module containg methods and varaibles for runner and enemies."""
import signal
import numpy as np
from input import _getChUnix as getChar
from base_frame import base_frame
from rewards import *
from alarmexception import AlarmException
from config import *
from firing import *


class Person:
    """Person class used for Mandalorain on screen."""

    def __init__(self):
        self.__person = np.array(
            [[' ', '@', ' '], ['-', '|', '-'], ['/', ' ', '\\']])
        self.__life = 20
        self.__score = 0
        self.__shield = 0
        self.__jetflag = 0
        self.__bulletflag = 0
        self.__magnetflag = False
        self.__boost = False
        self.__boostdur = 0
        self.__positiony = 27
        self.__positionx = 0
        self.__magnetposx = 0
        self.__shield_activate = False
        self.__magnetperiod = 0

    def get_magnetperiod(self):
        """Used to get remaining period of magnet."""
        return self.__magnetperiod

    def decrease_magnetperiod(self):
        """Used to decrease remaining period of the magnet."""
        self.__magnetperiod -= 1

    def get_boostdur(self):
        """Used to get duration of the boost."""
        return self.__boostdur

    def set_boostdur(self, value):
        """

        Args:
          value: To set value of the boost duration.

        """
        self.__boostdur = value

    def decrease_boost(self):
        """Used to decrease value of the boost duration."""
        self.__boostdur -= 1

    def get_person(self):
        """Used to get structure of mandalorain."""
        return self.__person

    def get_magnetx(self):
        """Used to get position of magnet."""
        return self.__magnetposx

    def set_magnetx(self, value):
        """

        Args:
          value: value of x coordinate of magnet.

        """
        self.__magnetposx = value

    def get_x(self):
        """Used to get x coordinate of mandalorian."""
        return self.__positionx

    def set_x(self, value):
        """

        Args:
          value: Used to set value of x coordinate of Mandalorian.

        """
        self.__positionx = value

    def get_y(self):
        """Used to get y coordinate of the Mandalorain."""
        return self.__positiony

    def set_y(self, value):
        """

        Args:
          value: Value to set to y coordinate.

        """
        self.__positiony = value

    def deactivate_shield(self):
        """Used to deactivate shield of the Mandalorain."""
        self.__shield_activate = False

    def check_shield(self):
        """Used to check shield status of the Mandalorain."""
        return self.__shield_activate

    def show_shield(self):
        """Used to get shield status of Mandalorain."""
        return self.__shield

    def decrease_shield(self):
        """Used to decrease shield of Mandalorain."""
        self.__shield -= 1

    def increase_shield(self):
        """Used to increase shield of Mandalorain."""
        self.__shield += 1

    def check_boost(self):
        """Used to check if boost flag is true of Mandalorain."""
        return self.__boost

    def change_boostflag(self):
        """Used to change boost flag of Mandalorain."""
        self.__boost = False

    def show_score(self):
        """Used to show score of the Mandalorain."""
        scr = self.__score
        return scr

    def check_score(self, score):
        """

        Args:
          score: Value to be added to score variable.

        Returns:
            None

        """
        self.__score += score

    def set_magnet(self):
        """Used to set magnet flag and its duration on screen."""
        self.__magnetflag = True
        self.__magnetperiod += 300

    def reset_magnet(self):
        """Used to remove magnet from frame."""
        self.__magnetflag = False

    def check_magnet_flag(self):
        """Used to get value of magnet flag."""
        return self.__magnetflag

    def show_flag(self):
        """Used to get value of the jet flag."""
        return self.__jetflag

    def check_constraint(self, posx, posy, base_frame):
        """

        Args:
          posx: position x of the Mandalorain.
          posy: position y of the Mandalorain.
          base_frame: frame object.

        Returns:
            int : Score obtained for the particualr position of the person.

        """
        score = 0

        for i in range(3):
            for j in range(3):

                if(base_frame.get_particular_frame(posx+i,posy+j) == '=' or
                   base_frame.get_particular_frame(posx+i,posy+j) == '|'):
                    return 'obstacle'

                elif base_frame.get_particular_frame(posx+i,posy+j) == '$':
                    score += 1
                    base_frame.set_frame_scene(posx+i,posy+j,' ')
                    base_frame.set_user_frame(posx+i,posy+j,' ')

        return score

    def generate_person(self, base_frame, Enemy):
        """

        Args:
          base_frame: Frame object on which Mandalorian has to be generated.
          Enemy: Enemy object to constraint location of Mandalorian.

        Returns:
            None

        """

        if DRAGON_PLACE_X-2 > self.__positionx:

            if base_frame.get_frame() < self.__positionx:
                x_cor = self.__positionx
                y_cor = self.__positiony
                person = self.__person
                for i in range(3):
                    for j in range(3):
                        base_frame.set_user_frame(y_cor+i,x_cor+j,person[i][j])

            else:
                self.__positionx = base_frame.get_frame()
                x_cor = base_frame.get_frame()
                y_cor = self.__positiony
                person = self.__person
                for i in range(3):
                    for j in range(3):
                        base_frame.set_user_frame(y_cor+i, x_cor+j,person[i][j])

        else:
            self.__positionx = DRAGON_PLACE_X-3
            if base_frame.get_frame() < self.__positionx:
                x_cor = self.__positionx
                y_cor = self.__positiony
                person = self.__person
                for i in range(3):
                    for j in range(3):
                        base_frame.set_user_frame(y_cor+i, x_cor+j,person[i][j])

            else:
                self.__positionx = base_frame.get_frame()
                y_cor = self.__positiony
                x_cor = base_frame.get_frame()
                person = self.__person
                for i in range(3):
                    for j in range(3):
                        base_frame.set_user_frame(y_cor+i, x_cor+j,person[i][j])

    def show_life(self):
        """Used to get value of life of Mandalorian."""
        return self.__life

    def decrease_life(self):
        """Used to decrease value of life of Mandalorian."""
        self.__life -= 1

    def speedboost_check(self, posx, posy, Frame):
        """

        Args:
          posx: X coordinate of the Mandalorian.
          posy: Y coordinate of the Mandalorian.
          Frame: Frame object to check speed boost.

        Returns:
            Bool : True if Speed boost exist on given portion.

        """

        for i in range(3):
            for j in range(3):
                if Frame.get_particular_frame(posx+i,posy+j) == 'S':
                    Frame.set_frame_scene(posx+i,posy+j,' ')
                    Frame.set_user_frame(posx+i,posy+j,' ')
                    return True

    def reset_person(self, base_frame):
        """

        Args:
          base_frame: frame object from which madalorain has to be removed.

        Returns:
            None

        """
        if base_frame.get_frame() <= self.__positionx:
            x_cor = self.__positionx
            y_cor = self.__positiony
            for i in range(3):
                for j in range(3):
                    base_frame.set_user_frame(y_cor+i, x_cor+j,' ')

        else:
            y_cor = self.__positiony
            x_cor = base_frame.get_frame()
            for i in range(3):
                for j in range(3):
                    base_frame.set_user_frame(y_cor+i, x_cor+j," ")

    def gravity(self, Frame):
        """

        Args:
          Frame: Frame object from which mandalorain has to be removed.

        Returns:
            None

        """
        if self.__positiony < 27:
            value = self.check_constraint(
                self.__positiony+1, self.__positionx, Frame)
            if(value is 'obstacle' and self.__shield_activate is False):
                print("GAME OVER !")
                quit()

            elif(value is 'obstacle' and self.__shield_activate is True):
                value = 0

            self.__score += value
            if self.speedboost_check(self.__positiony+1,
                                     self.__positionx, Frame):
                self.__boost = True
                self.__boostdur += 200
            self.reset_person(Frame)
            self.__positiony += 1

    def move_person(self, Frame):
        """

        Args:
          Frame: Frame object from which mandalorian has to be removed.

        Returns:
            None

        """
        def alarmhandler(signum, frame):
            """

            Args:
              signum: Signal Number.
              frame: Frame Object.

            Returns:
                None

            """
            raise AlarmException

        def user_input(timeout=0.1):
            """input method.

            Args:
              timeout:  (Default value = 0.1)

            Returns:
            """
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
            if self.__positionx - Frame.get_frame() < 97:
                value = self.check_constraint(
                    self.__positiony, self.__positionx+1, Frame)
                if(value is 'obstacle' and self.__shield_activate is False):
                    print("GAME OVER !")
                    quit()

                elif(value is 'obstacle' and self.__shield_activate is True):
                    value = 0

                self.__score += value
                if self.speedboost_check(self.__positiony,
                                         self.__positionx+1, Frame):
                    self.__boost = True
                    self.__boostdur += 200
                self.reset_person(Frame)
                self.__jetflag = 0
                self.__positionx += 1

        elif char == 'w':
            if self.__positiony > 1:
                value = self.check_constraint(
                    self.__positiony-1, self.__positionx, Frame)
                if(value is 'obstacle' and self.__shield_activate is False):
                    print("GAME OVER !")
                    quit()

                elif(value is 'obstacle' and self.__shield_activate is True):
                    value = 0

                self.__score += value
                if self.speedboost_check(self.__positiony-1,
                                         self.__positionx, Frame):
                    self.__boost = True
                    self.__boostdur += 200
                self.reset_person(Frame)
                self.__positiony -= 1
                self.__jetflag = 1

        elif char == 's':
            if self.__positiony < 27:
                value = self.check_constraint(
                    self.__positiony+1, self.__positionx, Frame)
                if(value is 'obstacle' and self.__shield_activate is False):
                    print("GAME OVER !")
                    quit()

                elif(value is 'obstacle' and self.__shield_activate is True):
                    value = 0

                self.__score += value
                if self.speedboost_check(self.__positiony+1,
                                         self.__positionx, Frame):
                    self.__boost = True
                    self.__boostdur += 200
                self.reset_person(Frame)
                self.__positiony += 1

        elif char == 'a':
            if self.__positionx - Frame.get_frame() > 0:
                value = self.check_constraint(
                    self.__positiony, self.__positionx-1, Frame)
                if(value is 'obstacle' and self.__shield_activate is False):
                    print("GAME OVER !")
                    quit()

                elif(value is 'obstacle' and self.__shield_activate is True):
                    value = 0

                self.__score += value
                if(self.speedboost_check(self.__positiony,
                                         self.__positionx-1, Frame)):
                    self.__boost = True
                    self.__boostdur += 200
                self.reset_person(Frame)
                self.__jetflag = 0
                self.__positionx -= 1
        elif char == 'b':
            self.__jetflag = 0
            Frame.add_bullet(Bullet(self.__positionx+1, self.__positiony+1))

        elif char.isspace():
            self.__jetflag = 0
            if self.__shield == 20:
                self.__shield_activate = True

        else:
            self.__jetflag = 0


class Enemy(Person):
    """Enemy class to represet Dragon."""

    def __init__(self):
        self.__drgaon = [[' ', ' ', ' ', ';', '.', '_', "'", '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', '-', "'", ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '(', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '-', '.', '/', ' ', ';', '.', '-', ';', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ';', ' ', '_', ' ', ' ', ' ', ' ', ' ', ' ', '|', "'", '-', '-', ',', '|', ' ', '`', ' ', ' ', "'", '<', ' ', '_', '_', '_', ','], [' ', ' ', ' ', ' ', ' ', ' ', '_', '_', ')', ' ', ' ', ' ', ' ', ' ', '\\', '`', '-', '.', '_', '_', '.', ' ', ' ', ' ', '/', '`', '.', '-', "'", '/'], [
            ' ', ' ', ' ', ' ', '{', ';', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '/', 'o', '(', 'o', ' ', '\\', ' ', '|', ' ', '/', ' ', ',', "'", ' '], [' ', ' ', ' ', ' ', ' ', ' ', ';', ' ', ' ', '_', ' ', ' ', '_', '_', '.', '-', "'", '-', "'", '`', '-', "'", ' ', ' ', "'", '`', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', "'", ' ', '(', '-', ',', '`', ' ', ' ', '.', '-', '.', ' ', ' ', ' ', ' ', ' ', '_', ' ', '-', '.', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '_', ')', ')', ' ', ' ', '_', '/', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ']]
        Person.__init__(self)
        self.set_x(DRAGON_PLACE_X)
        self.set_y(TOTAL_WIDTH-9)

    def place_dragon(self, Frame, Person):
        """

        Args:
          Frame: Frame object to place dragon on it.
          Person: Person object to place Dragon according to Mandalorian.

        Returns:
            None

        """
        locs = 0
        locs = Person.get_y()+random.randint(-3, 3)
        if locs < 22:
            self.set_y(locs)
            for i in range(8):
                for j in range(30):
                    Frame.set_user_frame(locs+i,DRAGON_PLACE_X+j,self.__drgaon[i][j])

        else:
            self.set_y(TOTAL_WIDTH-9)
            for i in range(8):
                for j in range(30):
                    Frame.set_user_frame(TOTAL_WIDTH-9+i,DRAGON_PLACE_X+j,self.__drgaon[i][j])

    def fire_ice(self, Frame):
        """

        Args:
          Frame: Frame object to show ice balls.

        Returns:

        """
        Frame.add_ice_balls(Iceballs(self.get_x()+1, self.get_y()+5))
