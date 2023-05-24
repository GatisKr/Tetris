import pygame
from colors import Colors

class Grid:
    def __init__(self): # Create the init method which will initialize the grid object. We need to know how many rows and haw many columns contains the grid.
        self.num_rows = 20 # Create two attributes to store row and column information.
        self.num_cols = 10
        self.cell_size = 30 # Define the size of each cell of the grid in pixels. Each cell will be 30 pixels in width and height.
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] # Create a 2 dimensional array to represent the grid itself using a list of lists. This line is called a list comprehension. It's a shorthand way to create a list of lists or a 2D list. The inner part [0 for j in range(self.num_columns)] creates a list of zeroes with length equal self.num_columns, which in this case is 10 zeroes. This is done self.num_rows times because it's wrapped in another list comprehension, which repeats this process for self.num_rows times, which in this case is 20 times. So, the resulting ilst is a 2D list with self.num_rows and self.num_cols, where each cell is initialized to 0. 
        self.colors = Colors.get_cell_colors() # Create a list to hold all the colours the Grid will use. We have 7 blocks in the Tetris game and each block has its unique colour. We need 7 colours for the cells of the blocks and one colour for the empty cell, a dark grey colour. Here in the __init__ method we load the list of colours. 
        # In the init method call the get_cell_colors() of the Colors class like this: Colors.get_cell_colors().

    def print_grid(self): # Create a method to print the grid on the screen. This code iterates over every cell in the grid and prints out its value, row by row, with each row printed on a new line. This print_grid method will be useful to see the state of the grid later on. 
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    # Method def get_cell_colors(self): removed as we created colors class and we don't need it any more. 
    
    def draw(self, screen): # Create a Draw method. This code will draw each cell of the grid with a specific colour. With dark_grey colour if the cell contains 0, with green colour if the cell contains the value of 1 and so on. First, we get the value stored in each cell of the grid. We use a nested loop for this.
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column] # This code iterates through each cell in the grid and assigns the value of that cell to the variable "cell_value".
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, self.cell_size -1, self.cell_size -1) # Draw a cell of the grid. Create a rect to contain the cell. This rectangle will be invisible but it will help to draw the cell on the screen. In order to build a rect we need four parameters: the x and y coordinate of its top left corner, its width and its height. The x is going to be column, but since we are using a grid we have to multiply this by the self.cell_size. We do the same thing for the y row * self.cell_size. The width is going to be cell_size and the height is also going to be cell_size. We are going to draw the cell as a square by calling the pygame.draw.rect method. Before using this method we need to import the Pygame module. At the beginning of the Grid class we import Pygame.
                # All the cells are dark_grey colour. To make the cells visible, we need to add a margin of 1 pixel to each cell. Cell size is 30x30 pixels, so we can draw a 29x29 pixels grey rectangle for each cell to create the margin. In the draw rect method we need to make some changes: (column*self.cell_size '+1', row*self.cell_size '+1', self.cell_size, self.cell_size). This way we add a 1 pixel offsetath the x and y position of the grey rectangle we are drawing. Also we nee to substract 1 pixel from the width and the height of the rectangle we draw, because we said we need it be 29 pixels: (self.cell_size -1, self.cell_size -1).
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) # The pygame.draw.rect method requires 3 arguments. The surface to draw the object on, a colour and a rect (surface, color, rect). The surface we are going to draw on is the display surface we created in the main.py, named screen. Since we are in the Grid class and not in the main.py file, we have to pass the display_surface named 'screen' as an argument to the method, so we type screen in def draw(self, screen). The colour is the colour stored at the colours list. We can use the 'cell_value' to index into the colours list and retrieve the colour tuple for that specific cell by typing 'self.colors[cell_value]'. Since the grid now only contains zeros, the cell_value will be 0, so this will return the first colour of the list, which is a dark_grey colour. We have to tell the Draw function that the rect we want to draw is the 'cell_rect'. 
