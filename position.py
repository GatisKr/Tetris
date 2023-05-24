class Position: # We need the position of each occupied cell of the block in order to draw it on the screen. But we don't have this information yet. So we have to create it. To make our lives easier let's create a new class named position. The position class will be helpful because it will allow us to represent a position in a two-dimensional grid using a single object. Position class will have only two attributes, row and column.
    def __init__(self, row, column): # We need to pass in the row and the column in the constructor, so we type (self, row, column). 
        self.row = row # Create the row and column attributes. 
        self.column = column
# Now when position class is ready we can represent a position on the grid with a single object. To simplify code we will use inheritance. We will create a separate class for each block, which will contain the cell positions for each rotation state. These classes will inherit from the block class. 
