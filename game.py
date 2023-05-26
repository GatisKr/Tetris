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
        if self.block_inside() == False or self.block_fits() == False: # Modify the move_left, move_right and move_down methods to check if after moving the block it is still inside the game window. The line 'self.block_fits() == False' checks if the block after moving one column to the left is inside the game window or if the block fits in its new position. If this is False, we undo move, it is not a valid move.
            self.current_block.move(0, 1) # If the block moves outside of the game window we have to move it back in, so we undo the move. 

    def move_right(self): # Create block move method
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)
        
    def move_down(self): # Create block move method
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False: # We need to check if the block after moving one row down is inside the game window or if the block fits in its new position. So we add 'or self.block_fits == False' at the end of the line. Now if we attempt to move the block down and encounter a cell that is already occupied, we undo the move and lock the block in place.
            self.current_block.move(-1, 0)
            self.lock_block() # This method locks the block when it is at the bottom of the window.
    
    def lock_block(self):
        tiles = self.current_block.get_cell_positions() # In this method we need to update the game grid values to represent the location of each cell of the block on the grid at the time it touches the bottom of the screen. For each cell we will store the ID of the block, in the corresponding cell on the game grid. The ID value also corresponds to the block's colour. This will mark the cells as locked and indicate that the block has reached its final position at the bottom of the game window. First we get the current positions of all the tiles of the block.
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id # For each cell position we will store the ID of the block in the grid.
        self.current_block = self.next_block # Spawn new block on the screen. We already know which is the next block, it is saved in the next_block attribute.
        self.next_block = self.get_random_block() # This line spawns a new random block.

    def block_fits(self): # Create method that will check every cell of a block to see if it is on top of an empty cell of the grid or not.
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False: # We need to check if any of the cells is occupied.
                return False
        return True # If all the cells are empty we return True, the block can move to the specified position. 

    def rotate(self): # Create rotate method
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
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
