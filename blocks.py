from block import Block
from position import Position

class LBlock(Block): # Create child classes, one for each block. # This block inherits the attributes and methods of the Block class. We declare that inside the parenthesis LBlock(Block). The LBlock class is a child of the block class.
    def __init__(self): # Create the init method. 
        super().__init__(id = 1) # We need to initialize the Block class. So we have to call the init method of the Block class. The block constructor requires an ID. We give this block the id 1 or for better readability id = 1 'super().__init__(id = 1)'.
        self.cells = { # Declare which cells are occupied. We  use the cells attribute of the block class. The cells attribute is going to be a dictionary. The key of this dictionary will be the rotation state, a value from 0 to 3. So the dictionary have 4 keys. The value of each key is a list containing the positions of the occupied cells, 4 cells for each block. 
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)], # Create a list with occupied cells for 0 rotation state using the Position class.
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3) # In classical Tetris game each block spawns at the middle of the grid. One easy way to do this is to alter the child class for each block. We will move each block 3 cells to the right. 

class JBlock(Block): # Create separate class for each block, such as IBlock, JBlock, SBlock. For each class we define the positions of the occupied cells for each rotation state, similar to LBlock. When all the block classes defined, we can easily create instances of each block type in our main program. 
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)

class IBlock(Block):  
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3) # The IBlock spawns differently, so we correct its offset by moving spawn point one cell up. 

class OBlock(Block):  
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)] # The OBlock has the same rotation positions for each state, so we use only one rotation state and deal with it in a code later. 
        }
        self.move(0, 4) # The OBlock also spawns differently, so we correct its offset by moving spawn point one cell to the right. 

class SBlock(Block):  
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class TBlock(Block):  
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class ZBlock(Block):  
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3)
