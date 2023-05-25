from colors import Colors
from position import Position
import pygame

class Block:
    def __init__(self, id):
        self.id = id # The most important thing is to distinguish between different blocks, so each block will have a unique id. To add this attribute, we can create an "id" attribute in the class. We need to pass this id as an argument in the init method.
        self.cells = {} # To represent the cells that the block occupies in a 4x4 grid for all rotation states, we will create an attribute called cells. Self.cells = This attribute will be a dictionary, so we initialize it with an empty set of curly braces {}. We will use this dictionary to store the occupied cells in the bounding grid for each rotation state of the block. A dictionary in Python is a collection of key-value pairs, where each key is unique and maps to a corresponding value.
        self.cell_size = 30 # We need to know the size of each cell of the block in pixels. Let’s make each cell 30 pixels in width and height.
        self.row_offset = 0 # We need to offset the positions of all cells in block to move it. One way to do this is by adding two attributes to the block class. These attributes will hold the row and column offset of the block on the game grid. We can then update the position of each cell by adding the offste to its current position. So we create two attributes: 'self.row_offset' and 'self.row_offset' and place the value of 0 for each attribute.
        self.column_offset = 0
        self.rotation_state = 0 # The next thing we need to know is the rotation state of the block. So, let’s create a new attribute named rotation_state and set it to 0.
        self.colors = Colors.get_cell_colors() # Else we need to know for the block the colors it has to use to draw each occupied cell on the screen. The colors are the same ones we used in the grid class earlier. So, we can copy the method from the grid class and paste it in the block class. However, this will result in duplicate code, which is not a good programming practice. We want to avoid duplicate code as much as possible to keep our code organized and easy to maintain. So we will create another class to hold all the colors and use it in both the grid and block classes. This class will be called Colors and it will have attributes for each color we need in the game. # In this line of code we create colours attribute. We now have a list of all colours we need to use to draw a block on the screen. 
    
    def move(self, rows, columns): # Create a method that will move the block by adding a row and column offset. We need to know how many rows and columns we have to move. All we have to do is to change the offset attributes. 
        self.row_offset += rows # '+=' operator adds the value on the right-hand side to the current value of the variable on the left-hand side and then assigns the result back to the variable on the left-hand side.
        self.column_offset += columns
        
    def get_cell_positions(self): # We need to modify the positions of the cells in the block according to the offset. To achieve this we can create a new method in the block class which will calculate the actual position of each cell after the offset is applied. It's better to have a separate method for this, rather than modifying the positions in the draw method, because we will need to recalculate these positions later to check for collisions. This way we can avoid repetitive calculations. So we create another method get_cell_positions(self). This method will return the positions of the occupied cells with the offset applied in a list. 
        tiles = self.cells[self.rotation_state] # First, we get the default cell positions for the current rotation state. 
        moved_tiles = [] # Now we create a new empty list to hold the moved tiles. 
        for position in tiles: # We need to loop through all the tiles and add the offset to their positions. 
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position) # We have to append the new position to the moved_tiles list. 
        return moved_tiles # Returns the list

    def draw(self, screen): # Create draw method that will be responsible for drawing the block on the screen. We need to know the surface we are going to draw on, so we pass it as an argument (self, screen). 
        tiles = self.get_cell_positions() # We have access in Position class to all the cells of the block for every rotation state. This line retrieves the list of positions for the current rotation state of the tetromino, as determined by the value of the self.rotation_state attribute. After we created def get_cell_positions(self) method we changed this line 'tiles = self.cells[self.rotation_state]' to 'tiles = self.get_cells_positions()'. 
        for tile in tiles: # For each cell we can draw a rectangle. We will use a for loop. 
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size -1, self.cell_size -1) # Create rectangle for each cell. We use the pygame.Rect method, so we import Pygame. As we did in the grid class we leave a one pixel offset when we draw the cells. 
            pygame.draw.rect(screen, self.colors[self.id], tile_rect) # Draw the cell. The colour value of the cell is obtained from the colors list using the block's ID as the index. 
