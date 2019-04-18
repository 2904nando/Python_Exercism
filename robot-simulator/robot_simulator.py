# Globals for the bearings
# Change the values as you see fit
EAST = "E"
NORTH = "N"
WEST = "W"
SOUTH = "S"

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y
        self.coordinates = tuple([self.x, self.y])

    def turn_right(self):
        if self.bearing == "N":
            self.bearing = "E"
        elif self.bearing == "E":
            self.bearing = "S"
        elif self.bearing == "S":
            self.bearing = "W"
        elif self.bearing == "W":
            self.bearing = "N"

    def turn_left(self):
        if self.bearing == "N":
            self.bearing = "W"
        elif self.bearing == "W":
            self.bearing = "S"
        elif self.bearing == "S":
            self.bearing = "E"
        elif self.bearing == "E":
            self.bearing = "N"

    def advance(self):
        if self.bearing == "N":
            self.y += 1
        elif self.bearing == "E":
            self.x += 1
        elif self.bearing == "S":
            self.y -= 1
        elif self.bearing == "W":
            self.x -= 1
        self.coordinates = (self.x,self.y)

    def simulate(self, commands):
        for char in commands:
            if char == "A":
                self.advance()
            elif char == "L":
                self.turn_left()
            elif char == "R":
                self.turn_right()
