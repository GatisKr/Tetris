from grid import Grid
from blocks import * # Asterisk symbol '*' imports everything from file blacks.py
import random

class Game:
    def __init__(self): # The game class must create and hold a grid. So we import the Grid class. 
        self.grid = Grid() # Create Grid attribute. 
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()] # Create the attribute to hold the current block that is visible on the screen. To do this we have to select a random block from all the available blocks in the game. First we create a list of all the blocks. Now we create all the blocks. 
        self.current_block = self.get_random_block() # Create the two attributes for the current and the next block. 
        self.next_block = self.get_random_block()
        
    def get_random_block(self): # Now we can create a method that returns a random block from this list, so we need to import the random module. 
        if len(self.blocks) == 0: # At some point, the list will become empty, meaning no more blocks will be available. In that case we can simply refill the list with all the blocks again. So before selecting a random block we have to check if the list is empty.
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks) # Instead of randomly selecting a block from the list every time we call the method, in the original game each of the 7 blocks appears at least once before re-appearing. So we need to implement a way to cycle through the list of blocks ensuring that each block appears at least once before repeating the cycle. First we select random block from the list.
        self.blocks.remove(block) # We need to remove random called block from the list, so the next time the method is called, this block would not be available. 
        return block # Return that block
    
    def move_left(self): # Create block move method
        self.current_block.move(0, -1) # This moves current block to the left for one tile.
        if self.block_inside() == False: # Modify the move_left, move_right and move_down methods to check if after moving the block it is still inside the game window. 
            self.current_block.move(0, 1) # If the block moves outside of the game window we have to move it back in, so we undo the move. 

    def move_right(self): # Create block move method
        self.current_block.move(0, 1)
        if self.block_inside() == False:
            self.current_block.move(0, -1)
        
    def move_down(self): # Create block move method
        self.current_block.move(1, 0)
        if self.block_inside() == False:
            self.current_block.move(-1, 0)

    def rotate(self): # Create rotate method
        self.current_block.rotate()
        if self.block_inside() == False:
            self.current_block.undo_rotation() # Undo the rotation if the block is otside the grid.

    def block_inside(self): # Check if the block is inside game window using the is_inside method of the Grid class.
        tiles = self.current_block.get_cell_positions() # First get the list of all the tiles or cells of the block.
        for tile in tiles: # Check if any tile of the block is outside of the grid.
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False # If the tile is outside the grid return false
        return True # For loop runs through all the tiles and in none of them is outside the grid, then Else condition returns value True.

    def draw(self, screen): # The game class will also have a draw method which will be responsible for drawing all the objects on the screen. We need to take the display surface to draw on as an argument. 
        self.grid.draw(screen)
        self.current_block.draw(screen)
