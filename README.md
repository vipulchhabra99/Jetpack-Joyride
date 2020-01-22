DESIGN AND ANALYSIS OF SYSTEM SOFTWARE
MANDALORIAN - OOPS CONCEPTS


  

Introduction
A terminal-based python game is designed. The game is heavily inspired by Jet-pack joy ride, Concepts of object-oriented programming are used to learn the basics of it. The game has the following rules:
1. There are coins suspended in the air the Mandalorian can jump and collect them to increase the score.
2. If the Mandalorian touches any fire beam the game gets over immediately.
3. There is Magnet as an obstacle as soon as Mandalorian comes in its range it gets attracted towards the x component of the magnet.
4. Also, there is limited time so the Mandalorian has to defeat the enemy in the given time
5. Mandalorian can shoot the bullets and remove obstacles from its path
6. Mandalorian can activate his shield and hence his color changes until the shield is activated and he can pass over any fire beam without being killed.
7. Mandalorian has to kill the enemy in given time to win the game.


THE FILE STRUCTURE
1. The game has the following files :
1. Main.py - Contains all the objects of the classes being used and the system logic and their arrangements.
2. Config.py - Contains all the variables of the configuration used in the game like screen width, positions, etc and hence can be varied easily.
3. Base_frame.py - Contains class for the background with the array and relevant functions to it.
4. Endscreen.py - Contains the class for the message to be displayed at the end of the game.
5. Firing.py - Contains the class for the bullets being fired by the Mandalorian and the ice balls of the dragon with their relevant functions.
6. Input.py - Contains the declaration to get the input from the user asynchronously.
7. Obstacles.py - Contains the class of the obstacles in the game - the fire beams and the magnets and their relevant functions.
8. Person.py - Contains the declarations of Mandalorian and the enemy and their relevant functions.
9. Rewards.py - COntains the declaration of the coins suspended and speed boost to speed the gameplay and their relevant functions.


THE OOPS CONCEPTS USED IN THE DEVELOPMENT
1. Iceballs are inherited from class Bullet and forward function is being redefined in it.
2. Similarly, the enemy class is inherited from a person’s class.
3. All the coins suspended, speedups , obstacles are also the objects created from their respective class.
4. The base frame is also a class with the object created in main file.