import pygame, sys # Import Pygame and SYS modules. 
from game import Game
# prior creating Game class. from grid import Grid # Import the Grid class from the file grid.py. 
# prior creating Game class. from blocks import * # Import the all the classes from the file blocks.py. Asterisk '*' symbol is used to import all the classes.

pygame.init()
dark_blue = (44, 44, 127) # Drawing. Pygame provides several built-in colours, however we can define our all colours for this game. In Pygame colours are represented as a tuple of three values, each value representing the amount of red, green and blue in the colour. The values for each component range from 0 to 255, where 0 represents the absence of the colour and 255 represents the full intensity of the colour. For example, to create a red colour, we would create a tuple with the following values: red = (255, 0 ,0). These values represent the red, green and blue components respectively. To create a dark blue colour we will create a tuple like this.

screen = pygame.display.set_mode((300, 600)) # Create dispay surface # This line of code creates a display surface object named screen. The set_mode() method takes a tuple as an argument. The first value is the width and the second value is the height of the display surface, our canvas. This line created the game window and to draw on it a top-left corner coordinate system with unique x and y values is used (0, 0 value is in the top left corner, which is different from standart Cartesian coordinate system. The x-coordinate increases as we move to the right and the y-coordinate increases as we move down).
pygame.display.set_caption("Python Tetris") # Create game window title

clock = pygame.time.Clock() # Create clock object. 

game = Game() # Create game object. 
# prior creating Game class. game_grid = Grid() # Create Grid object.

GAME_UPDATE = pygame.USEREVENT # USEREVENT is a special event type in pygame that can be used to create custom events. In this case it is used to create an event that will be triggered every time the block's position needs to be updated.
pygame.time.set_timer(GAME_UPDATE, 400) # We want to triger this event every 200 milliseconds. This function creates a timer that will trigger the GAME_UPDATE event every 200 milliseconds. The first argument is the event that needs to be triggered and the second argument is interval in milliseconds. In this way we are ensuring that the game is updating the position of the block every 200 milliseconds and not 60 times per second, avoiding the problem of the block moving too fast.

while True: # Game Loop starts with a wile loop like this. While loop is essential part of the game. It runs continuously until the player closes the game. At each iteration of the loop three key steps are performed: checking for events, updating positions of game objects and drawing the game objects in their new positions. Important to note that before running the game it is essential to ensure that the code inside the wile loop has been fully written. If the code is run at this point, the while loop will run indefinitely since there is no defined way to stop its execution. In the next step adding the necessary code to stop the while loop is needed.
    for event in pygame.event.get(): # This line of code gets all the events that Pygame recognizes and happened since the last time the while loop ran and puts them in a list. Then we loop through the list of events and check if any of the events is the QUIT event. The QUIT event is when we click on the close button of the window. If the event is the QUIT event, we break out of the while loop.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # This command closes the game completely. This command is part of the SYS module, so it has to be imported as Pygame module.
        if event.type == pygame.KEYDOWN: # Create block movement by player input. This line of code checks if the event type is equal to the KEYDOWN constant, which means the player has pressed a key. We need to determine which key the player pressed. We can do this by using the 'event.key' attribute. This attribute returns a constant representing the key that was pressed. For example, to check if the player pressed tle LEFT arrow key, we can use this if statement:
            if event.key == pygame.K_LEFT: # This line of code checks if the event.key constant is equal to the pygame.K_LEFT constant, which represents the LEFT arrow key. If the player presses the LEFT arrow key, we have to move the block one cell to the left. We can acheve this by using the move method of the block class to move the block one column to the left. However, instead of calling the move method of the block directly, we will create a new method called move_left in the game class, as we want to encapsulate the game logic for handling the movement of the block. 
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP: # Assign the action of pressing the up arrow key to rotating the block clockwise. In the game loop where we check for key presses we add this line.
                game.rotate()
        if event.type == GAME_UPDATE: # Check for the last event. This code checks if the event type is equal to GAME_UPDATE and if it is, it calls the move_down() method of the game object. This ensures that the block's position is updated only when the GAME_UPDATE event is triggered and not every time the game loop is executed.
            game.move_down()

    # Drawing
    screen.fill(dark_blue) # Inside the game loop, before updating the screen, we call the fill method of the screen like this. The fill method just fills the display surface, our canvas, with the colour we define. In this case, dark_blue.
    # prior creating Game class. game_grid.draw(screen) # Call the draw method of the grid object we have created inside the main loop. We type here game_grid.draw() and pass in the screen display surface.
    # prior creating Game class. block.draw(screen) # Call draw method to draw the LBlock. 
    game.draw(screen)

    pygame.display.update() # Update screen. This line of code takes all the changes made to the game objects and draws a picture from them. Since no any game objejcts are created yet, this line just draws a black screen. This wa the gridlines become visible, making the game more understandable and easier to play. 
    clock.tick(60) # Game clock object sets the speed how fast the game should run. This is done by using the tick() method. The tick() method takes an integer as an argument and that integer is the number of frames per second that we want. 60 frames per seconds are used in this game. This means that the wile loop and all the code inside it will run 60 times every second. If a frame rate is not set, the game would run as fast as the computer can handle, which could lead to inconsistencies in the games's speed. By setting the frame rate we make sure that the game runs smoothly and at the same speed for all players. 
