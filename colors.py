class Colors:
    dark_grey = (26,31,40)
    forest_green = (34,139,34)
    red = (232,18,18)
    orange = (226,116,17)
    yellow = (237,234,4)
    purple = (166,0,247)
    cyan = (21,204,209)
    blue = (13,64,216)
    white = (255,255,255)
    dark_blue = (44,44,127)
    light_blue = (59,85,162)

    @classmethod # decorator that allows to define a method that can be called
    def get_cell_colors(cls):
        return [cls.dark_grey,cls.forest_green,cls.red,cls.orange,cls.yellow,cls.purple,cls.cyan,cls.blue]
