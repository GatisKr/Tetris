# Tetris game
import pygame, sys
pygame.init()

'''
Create Game Loop.
    1. Event Handling: to check for any events that occur in the game, such as quitting the game, a key pressed on the keyboard, etc. This is done using the Pygame event handling system.
    2. Updating positions: to update the positions of all game objects, the blocks, based on the events detected in step 1. 
    3. Drawing objects: to draw all the game objects in their new positions on the screen. This step uses the Pygame graphics functions to render the objects in the display.
These three steps allow creting a dynamic and interactive game that responds to user inputs and updates its state accordingly.
'''

dark_blue = (44, 44, 127) # Drawing. Pygame provides several built-in colors, however we can define our all colours for this game. In Pygame colors are represented as a tuple of three values, each value representing the amount of red, green and blue in the color. The values for each component range from 0 to 255, where 0 represents the absence of the color and 255 represents the full intensity of the color. For example, to create a red color, we would create a tuple with the following values: red = (255, 0 ,0). These values represent the red, green and blue components respectively. To create a dark blue color we will create a tuple like this.

# Create dispay surface
screen = pygame.display.set_mode((300, 600)) # This line of code creates a display surface object named screen. The set_mode() method takes a tuple as an argument. The first value is the width and the second value is the height of the display surface, our canvas. This line created the game window and to draw on it a top-left corner coordinate system with unique x and y values is used (0, 0 value is in the top left corner, which is different from standart Cartesian coordinate system. The x-coordinate increases as we move to the right and the y-coordinate increases as we move down).
pygame.display.set_caption("Python Tetris") # Create game window title
clock = pygame.time.Clock() # Create clock object. 

while True: # Game Loop starts with a wile loop like this. While loop is essential part of the game. It runs continuously until the user closes the game. At each iteration of the loop three key steps are performed: checking for events, updating positions of game objects and drawing the game objects in their new positions. Important to note that before running the game it is essential to ensure that the code inside the wile loop has been fully written. If the code is run at this point, the while loop will run indefinitely since there is no defined way to stop its execution. In the next step adding the necessary code to stop the while loop is needed.
    for event in pygame.event.get(): # This line of code gets all the events that Pygame recognizes and happened since the last time the while loop ran and puts them in a list. Then we loop through the list of events and check if any of the events is the QUIT event. The QUIT event is when we click on the close button of the window. If the event is the QUIT event, we break out of the while loop.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit # This command closes the game completely. This command is part of the SYS module, so it has to be imported as Pygame module.
    screen.fill(dark_blue) # Drawing. Inside the game loop, before updating the screen, we call the fill method of the screen like this. The fill method just fills the display surface, our canvas, with the color we define. In this case, dark_blue.
    pygame.display.update() # Update screen. This line of code takes all the changes made to the game objects and draws a picture from them. Since no any game objejcts are created yet, this line just draws a black screen.
    clock.tick(60) # Game clock object sets the speed how fast the game should run. This is done by using the tick() method. The tick() method takes an integer as an argument and that integer is the number of frames per second that we want. 60 frames per seconds are used in this game. This means that the wile loop and all the code inside it will run 60 times every second. If a frame rate is not set, the game would run as fast as the computer can handle, which could lead to inconsistencies in the games's speed. By setting the frame rate we make sure that the game runs smoothly and at the same speed for all players. 
    