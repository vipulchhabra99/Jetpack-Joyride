from input import _getChUnix as getChar
from base_frame import base_frame
import signal
import numpy as np
from alarmexception import AlarmException

class Person:

    positiony = 27
    positionx = 0

    def __init__(self):
        self.person = np.array([['  ','@@','  '],['--','||','--'],['//',' ','\\\\']])
        self.__power = 20
        self.__score = 0

    def show_score(self):
        scr = self.__score
        return scr

    def add_score(self):
        self.__score += 1

    def generate_person(self):

        if(base_frame.current_frame <= self.positionx):
            base_frame.frame[self.positiony:self.positiony+3,self.positionx:self.positionx+3] = self.person

        else:
            base_frame.frame[self.positiony:self.positiony+3,base_frame.current_frame:base_frame.current_frame+3] = self.person

    def show_life(self):
        return self.__power

    def reset_person(self):
        if(base_frame.current_frame <= self.positionx):
            base_frame.frame[self.positiony:self.positiony+3,self.positionx:self.positionx+3] = "  "

        else:
            base_frame.frame[self.positiony:self.positiony+3,base_frame.current_frame:base_frame.current_frame+3] = "  "        

    def gravity(self):
        if(self.positiony < 27):
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

        def gravity():
            pass

        char = user_input()

        # Press 'q' for quit.
        if char == 'q':
            quit()

        if char == 'd':
            if(self.positionx - base_frame.current_frame < 77):
                self.reset_person()
                self.positionx += 1
        
        if char == 'w':
            if(self.positiony > 1):
                self.reset_person()
                self.positiony -=1

        if char == 's':
            if(self.positiony < 27):
                self.reset_person()
                self.positiony += 1

        if char == 'a':
            if(self.positionx - base_frame.current_frame > 0):
                self.reset_person()
                self.positionx -= 1
            
        # Press 'w' for up.
        """if char == 'w' and checkboard(self, Bomberman.bombera,
                                      Bomberman.bomberb - 1) == 'empty':
            if checkboard(self, Bomberman.bombera,
                          Bomberman.bomberb) != 'bomb':
                for j in range(0, 4):
                    Board.board[(Bomberman.bomberb + 1) *
                                2][(Bomberman.bombera + 1) * 4 + j] = ' '
                    Board.board[(Bomberman.bomberb + 1) * 2 +
                                1][(Bomberman.bombera + 1) * 4 + j] = ' '

            Bomberman.bomberb = Bomberman.bomberb - 1

            for j in range(0, 4):
                Board.board[(Bomberman.bomberb + 1) *
                            2][(Bomberman.bombera + 1) * 4 + j] = 'B'
                Board.board[(Bomberman.bomberb + 1) * 2 +
                            1][(Bomberman.bombera + 1) * 4 + j] = 'B'

        # Press 's' for down.
        if char == 's' and checkboard(self, Bomberman.bombera,
                                      Bomberman.bomberb + 1) == 'empty':
            if checkboard(self, Bomberman.bombera,
                          Bomberman.bomberb) != 'bomb':
                for j in range(0, 4):
                    Board.board[(Bomberman.bomberb + 1) *
                                2][(Bomberman.bombera + 1) * 4 + j] = ' '
                    Board.board[(Bomberman.bomberb + 1) * 2 +
                                1][(Bomberman.bombera + 1) * 4 + j] = ' '

            Bomberman.bomberb = Bomberman.bomberb + 1

            for j in range(0, 4):
                Board.board[(Bomberman.bomberb + 1) *
                            2][(Bomberman.bombera + 1) * 4 + j] = 'B'
                Board.board[(Bomberman.bomberb + 1) * 2 +
                            1][(Bomberman.bombera + 1) * 4 + j] = 'B'

        # Press 'a' for left.
        if char == 'a' and checkboard(self,
                                      Bomberman.bombera - 1,
                                      Bomberman.bomberb) == 'empty':
            if checkboard(self, Bomberman.bombera,
                          Bomberman.bomberb) != 'bomb':
                for j in range(0, 4):
                    Board.board[(Bomberman.bomberb + 1) *
                                2][(Bomberman.bombera + 1) * 4 + j] = ' '
                    Board.board[(Bomberman.bomberb + 1) * 2 +
                                1][(Bomberman.bombera + 1) * 4 + j] = ' '

            Bomberman.bombera = Bomberman.bombera - 1

            for j in range(0, 4):
                Board.board[(Bomberman.bomberb + 1) *
                            2][(Bomberman.bombera + 1) * 4 + j] = 'B'
                Board.board[(Bomberman.bomberb + 1) * 2 +
                            1][(Bomberman.bombera + 1) * 4 + j] = 'B'

        # Press 'd' for right.
        if char == 'd' and checkboard(self,
                                      Bomberman.bombera + 1,
                                      Bomberman.bomberb) == 'empty':
            if checkboard(self, Bomberman.bombera,
                          Bomberman.bomberb) != 'bomb':
                for j in range(0, 4):
                    Board.board[(Bomberman.bomberb + 1) *
                                2][(Bomberman.bombera + 1) * 4 + j] = ' '
                    Board.board[(Bomberman.bomberb + 1) * 2 +
                                1][(Bomberman.bombera + 1) * 4 + j] = ' '

            Bomberman.bombera = Bomberman.bombera + 1

            for j in range(0, 4):
                Board.board[(Bomberman.bomberb + 1) *
                            2][(Bomberman.bombera + 1) * 4 + j] = 'B'
                Board.board[(Bomberman.bomberb + 1) * 2 +
                            1][(Bomberman.bombera + 1) * 4 + j] = 'B'

                """