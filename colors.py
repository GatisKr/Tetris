class Colors: # Create a class that will return a list of 8 colours. A colour is just a tuple of three values. Dark_grey is the colour for the empty cell, the other colours are for 7 blocks. 
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod # is a Python decorator that allows to define a method that can be called on a class rather than on an instance of the class. Now we can create the method we want.
    def get_cell_colors(cls): # We  need to pass in 'cls' here. This way we can access the attributes of the class. 'cls' is a reference to the class itself and it allows us to access the class-level attributes and methods. It's similar to using self to access instance-level attributes and methods, but 'cls' is used for the class-level 
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue] # Put all the colours in the list and return that list. The order of the list is important. We use the index of each colour when we draw each cell on the screen. That index corresponds to the block ID. # Now we have to return a list with all the colours we need for the cells, just like we did in the grid class. So we copy the return statement from the grid to the colour class. We just have to add 'cls.' before each color definition to get these colours values.
