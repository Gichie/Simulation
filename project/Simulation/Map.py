class Map:
    '''Карта, содержит в себе коллекцию для хранения существ и их расположения.'''
    def __init__(self, width, height):
        self.map = {}
        self.width = width
        self.height = height
        for i in range(height):
            for j in range(width):
                self.map[(i, j)] = None