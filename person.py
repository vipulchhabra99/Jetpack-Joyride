from input import _getChUnix as getChar
from base_frame import base_frame
import signal
from alarmexception import AlarmException

class Person:

    def __init__(self):
        self.person = [['  ','@@','  '],['--','||','--'],['//',' ','\\\\']]
        self.__power = 20
        self.__score = 0

    def show_score(self):
        scr = self.__score
        return scr

    def add_score(self):
        self.__score += 1

    def generate_person(self):

        for i in range(3):
            for j in range(3):
                base_frame.frame[base_frame.current_frame+27+i][40+j] = self.person[i][j]

    def show_life(self):
        return self.__power

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