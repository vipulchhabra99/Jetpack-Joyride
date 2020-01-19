''' Module containing obtacle class and respective functions'''
import random
import numpy as np
from config import TOTAL_GAME_FRAME, MAGNET_SPEED


class Obstacles:
    """This class is used to set obstacles in the game."""

    def __init__(self, x, y):
        self.__active = True
        self.__locx = x
        self.__locy = y

    def remove_obstacle(self):
        """Basic Function to remove any obstacle."""
        self.__active = False

    def check_status(self):
        """Used to check status of the obstacle. """
        return self.__active

    def set_status(self, value):
        """

        Args:
          value: Value that is to be set to active flag

        """
        self.__active = value

    def set_x(self, value):
        """

        Args:
          value: Value that is to be set to x location of obs.

        """
        self.__locx = value

    def set_y(self, value):
        """

        Args:
          value: Value that is to be set to y location of obs.

        """
        self.__locy = value

    def get_x(self):
        """ Getter function for the x coordinate of obstacle. """
        return self.__locx

    def get_y(self):
        """Getter function for the x coordinate of obstacle. """
        return self.__locy


class horizontal_obstacle(Obstacles):
    """Horizontal obstacle being inherited from obstacle. """

    def __init__(self, x, y):
        self.__obstacle = np.array(['=', '=', '='])
        Obstacles.__init__(self, x, y)

    def get_obstacle(self):
        """Used to get value of obstacle. """
        return self.__obstacle

    def remove_obstacle(self, posx, posy, base_frame):
        """

        Args:
          posx: X location of the obstacle that is to be removed.
          base_frame: Frame from which the obtacle has to be removed.
          posy: Y location of the obstacle that is to be removed.

        """
        self.set_status(False)
        for i in range(3):
            base_frame.frame[posx][posy+i] = ' '
            base_frame.user_frame[posx][posy+i] = ' '


class vertical_obstacle(Obstacles):
    """Vertical obstacle being inherited from obstacle. """

    def __init__(self, x, y):
        self.__obstacle = np.array(['|', '|', '|'])
        Obstacles.__init__(self, x, y)

    def get_obstacle(self):
        """Used to get value of obstacle. """
        return self.__obstacle

    def remove_obstacle(self, posx, posy, base_frame):
        """

        Args:
          posx: X location of the obstacle that is to be removed.
          base_frame: Frame from which the obtacle has to be removed.
          posy: Y location of the obstacle that is to be removed.

        """
        self.set_status(False)
        for i in range(3):
            base_frame.frame[posx+i][posy] = ' '
            base_frame.user_frame[posx+i][posy] = ' '


class new_obstacle(Obstacles):
    """45 Degree obstacle being inherited from obstacle.  """

    def __init__(self, x, y):
        self.__obstacle = np.array(['=', '=', '='])
        Obstacles.__init__(self, x, y)

    def get_obstacle(self):
        """Used to get value of obstacle. """
        return self.__obstacle

    def remove_obstacle(self, posx, posy, base_frame):
        """

        Args:
          posx: X location of the obstacle that is to be removed.
          base_frame: Frame from which the obtacle has to be removed.
          posy: Y location of the obstacle that is to be removed.

        """
        self.set_status(False)

        for i in range(3):
            base_frame.frame[posx+i][posy+i] = ' '
            base_frame.user_frame[posx+i][posy+i] = ' '


class Magnet(Obstacles):
    """Magnet obstacle being inherited from obstacle. """

    def __init__(self, x, y):
        self.__magnet = np.array([['|', '=', '|'], ['|', ' ', '|']])
        Obstacles.__init__(self, x, y)

    def get_magnet(self):
        """Used to get value of magnet. """
        return self.__magnet

    def magnet_on_frame(self, Frame):
        """

        Args:
          Frame: Used to get the frame on which magent has to be placed.

        """
        for i in range(2):
            for j in range(3):
                Frame.user_frame[self.get_y()+i][self.get_x() +
                                                 j] = self.__magnet[i][j]

    def forward(self):
        """Used to move the magnet forward. """
        self.set_x(self.get_x()+MAGNET_SPEED)


def obstacle_place(Frame):
    """

    Args:
      Frame: To place the object on frame contained in Frame object

    """

    i = 0

    empty_array = np.array([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']])

    while i < (TOTAL_GAME_FRAME-200):
        j = random.randint(10, 30)
        i += j
        y = random.randint(7, 25)
        if np.array_equal(Frame.frame[y:y+4, i:i+4], empty_array):
            choice = random.randint(1, 3)

            if choice == 1:
                Frame.obstacles_placed.append(
                    [[y+1, i], [y+1, i+1], [y+1, i+2],
                     horizontal_obstacle(y+1, i)])
                for zi in range(3):
                    obs = Frame.obstacles_placed[-1][-1].get_obstacle()[zi]
                    Frame.frame[y+1][i+zi] = obs

            elif choice == 2:
                Frame.obstacles_placed.append(
                    [[y, i+1], [y+1, i+1], [y+2, i+1],
                     vertical_obstacle(y, i+1)])
                for zi in range(3):
                    obs = Frame.obstacles_placed[-1][-1].get_obstacle()[zi]
                    Frame.frame[y+zi][i+1] = obs

            elif choice == 3:
                Frame.obstacles_placed.append(
                    [[y, i], [y+1, i+1], [y+2, i+2], new_obstacle(y, i)])
                for zi in range(3):
                    obs = Frame.obstacles_placed[-1][-1].get_obstacle()[zi]
                    Frame.frame[y+zi][i+zi] = obs
