# In Tetris the gameplay area is a grid, consisting of 20 rows and 10 columns. The game pieces, or "tetrominoes", fall down the grid and the player must arrange them to form complete rows without any gaps. We will count the rows from top to bottom and the columns from left to the right, with the top left cell at row 0 and column 0 being the origin. To represent the grid we will use a two-dimensional array which can be inplemented as a list of lists in Python. In our implementation, empty cells will be represented by the value 0. When a tetromino, a block, is permanently placed on the grid by the player, the corresponding cells will be assigned a value reflecting its colour. For example, if we place a red tetromino on the grid, we will assign the value 2 to the cells it covers. Similarly, if we place a yellow block, we will assign the value 4 to its corresponding cells. Each colour has a unique numerical value and since there are 7 different colours in the game, the values used in the 2D array will range from 0 to 7. 0 for an empty cell and 1 to 7 for the colours of the blocks. However, the current block that can still be controlled by the player will not be reflected in the array and will instead be stored and managed separately in the game logic. 
import pygame

class Grid:
    def __init__(self): # Create the init method which will initialize the grid object. We need to know how many rows and haw many columns contains the grid.
        self.num_rows = 20 # Create two attributes to store row and column information.
        self.num_cols = 10
        self.cell_size = 30 # Define the size of each cell of the grid in pixels. Each cell will be 30 pixels in width and height.
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] # Create a 2 dimensional array to represent the grid itself using a list of lists. This line is called a list comprehension. It's a shorthand way to create a list of lists or a 2D list. The inner part [0 for j in range(self.num_columns)] creates a list of zeroes with length equal self.num_columns, which in this case is 10 zeroes. This is done self.num_rows times because it's wrapped in another list comprehension, which repeats this process for self.num_rows times, which in this case is 20 times. So, the resulting ilst is a 2D list with self.num_rows and self.num_cols, where each cell is initialized to 0. 
        self.colors = self.get_cell_colors() # Create a list to hold all the colours the Grid will use. We have 7 blocks in the Tetris game and each block has its unique colour. We need 7 colours for the cells of the blocks and one colour for the empty cell, a dark grey colour. Here in the __init__ method we load the list of colours. 

    def print_grid(self): # Create a method to print the grid on the screen. This code iterates over every cell in the grid and prints out its value, row by row, with each row printed on a new line. This print_grid method will be useful to see the state of the grid later on. 
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def get_cell_colors(self): # Create a method that will return a list of 8 colours. A colour is just a tuple of three values. Dark_grey is the colour for the empty cell, the other colours are for 7 blocks. 
        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue] # Put all the colours in the list and return that list. The order of the list is important. We use the index of each colour when we draw each cell on the screen. That index corresponds to the block ID. 
    '''
    Drawing in Pygame
    1. Display Surface. The surface where we see all the game objects. It's like blank Canvas. We can only have one per game. The display surface is created when we call the set_mode() function and it's the object we use when we call the update () function.
    2. The Regular Surface. The surface like the display surface that we can draw on it. Another type of blank Canvas. We can have as many surfaces as we want per game. Unlike the Display Surface which we can only have one per game. Regular Surfaces are used in this game to draw text on the display surface. 
    3. The Rect. A rectangular area. Rectangles are used for positioning, collision detection and for drawing objects. It has a position and a size. Rects are used for easy manipulation of objects and for easy drawing on a surface.
    '''
    def draw(self, screen): # Create a Draw method. This code will draw each cell of the grid with a specific colour. With dark_grey colour if the cell contains 0, with green colour if the cell contains the value of 1 and so on. First, we get the value stored in each cell of the grid. We use a nested loop for this.
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column] # This code iterates through each cell in the grid and assigns the value of that cell to the variable "cell_value".
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, self.cell_size -1, self.cell_size -1) # Draw a cell of the grid. Create a rect to contain the cell. This rectangle will be invisible but it will help to draw the cell on the screen. In order to build a rect we need four parameters: the x and y coordinate of its top left corner, its width and its height. The x is going to be column, but since we are using a grid we have to multiply this by the self.cell_size. We do the same thing for the y row * self.cell_size. The width is going to be cell_size and the height is also going to be cell_size. We are going to draw the cell as a square by calling the pygame.draw.rect method. Before using this method we need to import the Pygame module. At the beginning of the Grid class we import Pygame.
                # All the cells are dark_grey colour. To make the cells visible, we need to add a margin of 1 pixel to each cell. Cell size is 30x30 pixels, so we can draw a 29x29 pixels grey rectangle for each cell to create the margin. In the draw rect method we need to make some changes: (column*self.cell_size '+1', row*self.cell_size '+1', self.cell_size, self.cell_size). This way we add a 1 pixel offsetath the x and y position of the grey rectangle we are drawing. Also we nee to substract 1 pixel from the width and the height of the rectangle we draw, because we said we need it be 29 pixels: (self.cell_size -1, self.cell_size -1).
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) # The pygame.draw.rect method requires 3 arguments. The surface to draw the object on, a colour and a rect (surface, color, rect). The surface we are going to draw on is the display surface we created in the main.py, named screen. Since we are in the Grid class and not in the main.py file, we have to pass the display_surface named 'screen' as an argument to the method, so we type screen in def draw(self, screen). The colour is the colour stored at the colours list. We can use the 'cell_value' to index into the colours list and retrieve the colour tuple for that specific cell by typing 'self.colors[cell_value]'. Since the grid now only contains zeros, the cell_value will be 0, so this will return the first colour of the list, which is a dark_grey colour. We have to tell the Draw function that the rect we want to draw is the 'cell_rect'. 
                