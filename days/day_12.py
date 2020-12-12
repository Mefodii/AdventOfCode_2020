NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
RIGHT = "R"
LEFT = "L"
FORWARD = "F"

RIGHT_TURN = {
    WEST: NORTH,
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST
}

LEFT_TURN = {
    WEST: SOUTH,
    NORTH: WEST,
    EAST: NORTH,
    SOUTH: EAST
}

TURN = {
    90: RIGHT_TURN,
    -90: LEFT_TURN
}


class Boat:
    def __init__(self, instructions):
        self.instructions = instructions
        self.direction = EAST
        self.x = 0
        self.y = 0

    def distance(self):
        return abs(self.x) + abs(self.y)

    def start(self):
        for instruction in self.instructions:
            self.move(instruction[0:1], int(instruction[1:]))

    def move(self, direction, value):
        if direction == NORTH:
            self.move_vertically(value * -1)
        elif direction == SOUTH:
            self.move_vertically(value)
        elif direction == EAST:
            self.move_horizontally(value)
        elif direction == WEST:
            self.move_horizontally(value * -1)
        elif direction == RIGHT:
            self.turn(value)
        elif direction == LEFT:
            self.turn(value * -1)
        elif direction == FORWARD:
            self.move_forward(value)

    def turn(self, value):
        angle = 90 if value > 0 else -90
        for i in range(abs(int(value/90))):
            self.direction = TURN[angle][self.direction]

    def move_forward(self, value):
        self.move(self.direction, value)

    def move_horizontally(self, value):
        self.x += value

    def move_vertically(self, value):
        self.y += value

    def __str__(self):
        return f"{self.direction} {self.x} {self.y}"


class SuperBoat(Boat):
    def __init__(self, instructions):
        super().__init__(instructions)
        self.waypoint_x = 10
        self.waypoint_y = -1

    def turn(self, value):
        angle = 90 if value > 0 else -90
        for i in range(abs(int(value/90))):
            if angle > 0:
                self.waypoint_x, self.waypoint_y = (-1 * self.waypoint_y), self.waypoint_x
            else:
                self.waypoint_x, self.waypoint_y = self.waypoint_y, (-1 * self.waypoint_x)

    def move_forward(self, value):
        self.x += self.waypoint_x * value
        self.y += self.waypoint_y * value

    def move_horizontally(self, value):
        self.waypoint_x += value

    def move_vertically(self, value):
        self.waypoint_y += value

    def __str__(self):
        return super().__str__() + f" {self.waypoint_x} {self.waypoint_y}"


###############################################################################
def run_a(input_data):
    boat = Boat(input_data)
    boat.start()
    result = boat.distance()
    print(result)
    return [result]


def run_b(input_data):
    boat = SuperBoat(input_data)
    boat.start()
    result = boat.distance()
    print(result)
    return [result]
