
class Piece:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.rotation = 0

    def rotate(self):
        self.rotation += 1
        return self.get_positions()
    
    def moveRight(self):
        self.x = self.x + 1
        return self.get_positions()

    def moveLeft(self):
        self.x = self.x - 1
        return self.get_positions()
    
    def moveUp(self):
        self.y = self.y - 1
        return self.get_positions()

    def moveDown(self):
        self.y = self.y + 1
        return self.get_positions()

    def get_positions(self):
        positions = []
        format = self.shape[self.rotation % len(self.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((self.x + j, self.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions
