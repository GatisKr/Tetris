import pygame, sys # Import Pygame and SYS modules.
from game import Game
from colors import Colors
# prior creating Game class. from grid import Grid # Import the Grid class from the file grid.py. 
# prior creating Game class. from blocks import * # Import the all the classes from the file blocks.py. Asterisk '*' symbol is used to import all the classes.

pygame.init()

title_font = pygame.font.Font(None, 40) # Create a font. Arguments for the font command are: Font(font family, size). In current code line 'None' stands for the default font.
score_surface = title_font.render("Score", True, Colors.white) # Create a surface for the title. We use the render method from title_font object. We pass in the string that we want to display, "Score". We set the anti-alias argument to True and finally we set the color of the font.
next_surface = title_font.render("Next", True, Colors.white) # Create 'next block' title.
game_level = 1 # Initialize game_level variable.
game_over_surface = title_font.render("GAME OVER", True, Colors.white) # Create GAME OVER surface.
level_surface = title_font.render(f"LEVEL {game_level}", True, Colors.white) # Create Level surface.
level_sound_played = 0 # level_sound_played variable is used to play the next level sound only once within the game loop.

score_rect = pygame.Rect(320, 55, 170, 60) # Add a rounded rectangle of light_blue color to draw the score on. First create a rectangle object. We need the x and y coordinate of its top left corner, eidth and the height of the rectangle.
next_rectangle = pygame.Rect(320, 210, 170, 180) # Create a rect to display the next shape.

# Drawing. Pygame provides several built-in colours, however we can define our all colours for this game. In Pygame colours are represented as a tuple of three values, each value representing the amount of red, green and blue in the colour. The values for each component range from 0 to 255, where 0 represents the absence of the colour and 255 represents the full intensity of the colour. For example, to create a red colour, we would create a tuple with the following values: red = (255, 0 ,0). These values represent the red, green and blue components respectively. To create a dark blue colour we will create a tuple like this 'dark_blue = (44, 44, 127)'.

screen = pygame.display.set_mode((500, 620)) # Create dispay surface # This line of code creates a display surface object named screen. The set_mode() method takes a tuple as an argument. The first value is the width and the second value is the height of the display surface, our canvas. This line created the game window and to draw on it a top-left corner coordinate system with unique x and y values is used (0, 0 value is in the top left corner, which is different from standart Cartesian coordinate system. The x-coordinate increases as we move to the right and the y-coordinate increases as we move down).
pygame.display.set_caption("Python Tetris") # Create game window title

clock = pygame.time.Clock() # Create clock object. 

game = Game() # Create game object. 
# prior creating Game class. game_grid = Grid() # Create Grid object.

GAME_UPDATE = pygame.USEREVENT # USEREVENT is a special event type in pygame that can be used to create custom events. In this case it is used to create an event that will be triggered every time the block's position needs to be updated.
pygame.time.set_timer(GAME_UPDATE, 500) # We want to triger this event every 200 milliseconds. This function creates a timer that will trigger the GAME_UPDATE event every 200 milliseconds. The first argument is the event that needs to be triggered and the second argument is interval in milliseconds. In this way we are ensuring that the game is updating the position of the block every 200 milliseconds and not 60 times per second, avoiding the problem of the block moving too fast.

def game_speed():
    if game.score >= 14000: # Level 8
        pygame.time.set_timer(GAME_UPDATE, 100)
    if game.score >= 12000: # Level 7
        pygame.time.set_timer(GAME_UPDATE, 125)
    elif game.score >= 10000: # Level 6
        pygame.time.set_timer(GAME_UPDATE, 150)
    elif game.score >= 8000: # Level 5
        pygame.time.set_timer(GAME_UPDATE, 175)
    elif game.score >= 6000: # Level 4
        pygame.time.set_timer(GAME_UPDATE, 200)
    elif game.score >= 4000: # Level 3
        pygame.time.set_timer(GAME_UPDATE, 300)
    elif game.score >= 2000: # Level 2
        pygame.time.set_timer(GAME_UPDATE, 400)
    elif game.score < 2000: # Level 1
        pygame.time.set_timer(GAME_UPDATE, 500)

while True: # Game Loop starts with a wile loop like this. While loop is essential part of the game. It runs continuously until the player closes the game. At each iteration of the loop three key steps are performed: checking for events, updating positions of game objects and drawing the game objects in their new positions. Important to note that before running the game it is essential to ensure that the code inside the wile loop has been fully written. If the code is run at this point, the while loop will run indefinitely since there is no defined way to stop its execution. In the next step adding the necessary code to stop the while loop is needed.
    for event in pygame.event.get(): # This line of code gets all the events that Pygame recognizes and happened since the last time the while loop ran and puts them in a list. Then we loop through the list of events and check if any of the events is the QUIT event. The QUIT event is when we click on the close button of the window. If the event is the QUIT event, we break out of the while loop.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # This command closes the game completely. This command is part of the SYS module, so it has to be imported as Pygame module.
        if event.type == pygame.KEYDOWN: # Create block movement by player input. This line of code checks if the event type is equal to the KEYDOWN constant, which means the player has pressed a key. We need to determine which key the player pressed. We can do this by using the 'event.key' attribute. This attribute returns a constant representing the key that was pressed. For example, to check if the player pressed tle LEFT arrow key, we can use this if statement:
            if game.game_over == True: # Restart the game after game over by pressing a key.
                game.game_over = False # The game is over and the key is pressed, we need to restart the game. We have to set the game_over attribute to False.
                game.reset() # Calls a reset method to restart the game.
                del(game_level, level_sound_played)
                game_level = 1
                level_sound_played = 0
                pygame.time.set_timer(GAME_UPDATE, 500) # Reset game_update speed after game reset
            if event.key == pygame.K_LEFT and game.game_over == False: # This line of code checks if the event.key constant is equal to the pygame.K_LEFT constant, which represents the LEFT arrow key. If the player presses the LEFT arrow key, we have to move the block one cell to the left. We can acheve this by using the move method of the block class to move the block one column to the left. However, instead of calling the move method of the block directly, we will create a new method called move_left in the game class, as we want to encapsulate the game logic for handling the movement of the block. 
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1) # Add score when the down key is pressed
            if event.key == pygame.K_UP and game.game_over == False: # Assign the action of pressing the up arrow key to rotating the block clockwise. In the game loop where we check for key presses we add this line.
                game.rotate()

            game_speed() # This line calls function to update down movement speed for the block, increasing with next level.
        
        # This block of code moves block down at increased speed while down arrow key is pressed.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pygame.time.set_timer(GAME_UPDATE, 70) # This line overrides game update speed making the block move faster.
                game.move_sound.play(-1) # Move sound is played on the loop when down arrow key is pressed.
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_DOWN:
                game_speed() # Calls function to stop update speed override and return relevant level speed.
                game.move_sound.stop() # Stops move sound loop when key is not held down.

        if event.type == GAME_UPDATE and game.game_over == False: # Check for the last event. This code checks if the event type is equal to GAME_UPDATE and if it is, it calls the move_down() method of the game object. This ensures that the block's position is updated only when the GAME_UPDATE event is triggered and not every time the game loop is executed. # Stop the game from upating every 200 ms if the game is over and don't let the user move the block if the game is over. Added 'game.game_over == False'. This means the game will only update if it is not over.
            game.move_down()

    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white) # The score is dynamic and changes as the player moves the block. That's why we create a new surface for the score each time we want to update and display it on the screen. It is not a static text. So inside the game loop we create the 'score_surface'. The score is in integer, so we need to convert it to a string before displaying it, that's why we call the str() method here.
    screen.fill(Colors.dark_blue) # Inside the game loop, before updating the screen, we call the fill method of the screen like this. The fill method just fills the display surface, our canvas, with the colour we define. In this case, dark_blue.
    # prior creating Game class. game_grid.draw(screen) # Call the draw method of the grid object we have created inside the main loop. We type here game_grid.draw() and pass in the screen display surface.
    # prior creating Game class. block.draw(screen) # Call draw method to draw the LBlock. 
    screen.blit(score_surface, (365, 20, 50, 50)) # Call the blit method to display the score_surface on the display_surface which we have named screen. 'Blit' means 'block image transfer'. Most of the time in pygame we blitting images to the display_surface. We have to pass in the surface that we want to display and the location on the screen.
    screen.blit(next_surface, (375, 180, 50 ,50))
    
    if game.game_over == True: # Implement a check in the game loop before drawing the game over message to ensure that the message is only shown when th game is actually over.
        screen.blit(game_over_surface, (320, 450, 50 ,50))
    
    # This code creates the next 'Level' text surface with updated Level variable and plays the next Level sound.
    if game.score >= 16000: # Level 9
        level_surface = title_font.render(f"LEVEL {game_level}", True, Colors.white)
        screen.blit(level_surface, (350, 500, 50 ,50))
        if game_level == 8:
            game_level += 1
        if level_sound_played == 7:
            game.level_sound.play()
            level_sound_played += 1
    elif game.score >= 14000 and game.score < 16000: # Level 8
        level_surface = title_font.render(f"LEVEL {game_level}", True, Colors.white)
        screen.blit(level_surface, (350, 500, 50 ,50))
        if game_level == 7:
            game_level += 1
        if level_sound_played == 6:
            game.level_sound.play()
            level_sound_played += 1
    elif game.score >= 12000 and game.score < 14000: # Level 7
        level_surface = title_font.render(f"LEVEL {game_level}", True, Colors.white)
        screen.blit(level_surface, (350, 500, 50 ,50))
        if game_level == 6:
            game_level += 1
        if level_sound_played == 5:
            game.level_sound.play()
            level_sound_played += 1
    elif game.score >= 10000 and game.score < 12000: # Level 6
        level_surface = title_font.render(f"LEVEL {game_level}", True, Colors.white)
        screen.blit(level_surface, (350, 500, 50 ,50))
        if game_level == 5:
            game_level += 1
        if level_sound_played == 4:
            game.level_sound.play()
            level_sound_played += 1
    elif game.score >= 8000 and game.score < 10000: # Level 5
        level_surface = title_font.render(f"LEVEL {game_level}", True, Colors.white)
        screen.blit(level_surface, (350, 500, 50 ,50))
        if game_level == 4:
            game_level += 1
        if level_sound_played == 3:
            game.level_sound.play()
            level_sound_played += 1
    elif game.score >= 6000 and game.score < 8000: # Level 4
        level_surface = title_font.render(f"LEVEL {game_level}", True, Colors.white)
        screen.blit(level_surface, (350, 500, 50 ,50))
        if game_level == 3:
            game_level += 1
        if level_sound_played == 2:
            game.level_sound.play()
            level_sound_played += 1
    elif game.score >= 4000 and game.score < 6000: # Level 3
        level_surface = title_font.render(f"LEVEL {game_level}", True, Colors.white)
        screen.blit(level_surface, (350, 500, 50 ,50))
        if game_level == 2:
            game_level += 1
        if level_sound_played == 1:
            game.level_sound.play()
            level_sound_played += 1
    elif game.score >= 2000 and game.score < 4000: # Level 2
        level_surface = title_font.render(f"LEVEL {game_level}", True, Colors.white)
        screen.blit(level_surface, (350, 500, 50 ,50))
        if game_level == 1:
            game_level += 1
        if level_sound_played == 0:
            game.level_sound.play()
            level_sound_played += 1
    else: # Level 1
        level_surface = title_font.render(f"LEVEL {game_level}", True, Colors.white)
        screen.blit(level_surface, (350, 500, 50 ,50))
    
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10) # Print score_rect. '0, 10' makes rectangle with rounded corners.
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery)) # Display score_value_surface on top of the score_rect. We need to define the position on the screen where we want to draw the text. This is tricky, because the score is not static, its size will change. If we want it to be centered, we can use a small trick. The provided code calculates the rectangle that encloses the score_value_surface text and centers it on the score_rect horizontally and vertically, so that the score is displayed in the middle of the score rect.
    pygame.draw.rect(screen, Colors.light_blue, next_rectangle, 0, 10)
    game.draw(screen)
    
    pygame.display.update() # Update screen. This line of code takes all the changes made to the game objects and draws a picture from them. Since no any game objejcts are created yet, this line just draws a black screen. This wa the gridlines become visible, making the game more understandable and easier to play. 
    clock.tick(60) # Game clock object sets the speed how fast the game should run. This is done by using the tick() method. The tick() method takes an integer as an argument and that integer is the number of frames per second that we want. 60 frames per seconds are used in this game. This means that the wile loop and all the code inside it will run 60 times every second. If a frame rate is not set, the game would run as fast as the computer can handle, which could lead to inconsistencies in the games's speed. By setting the frame rate we make sure that the game runs smoothly and at the same speed for all players. 
