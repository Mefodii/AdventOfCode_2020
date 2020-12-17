from copy import copy

ACTIVE = "#"
INACTIVE = "."


class State:
    def __init__(self, cells):
        self.cells = cells

    def get_adjacent(self, x, y, z):
        return [self.get_cell(x+x1, y+y1, z+z1)
                for x1 in range(-1, 2, 1)
                for y1 in range(-1, 2, 1)
                for z1 in range(-1, 2, 1)
                if not x1 == y1 == z1 == 0]

    def get_cell(self, x, y, z):
        print(x, y, z)
        if z < 0 or z >= len(self.cells):
            return False

        if y < 0 or y >= len(self.cells[z]):
            return False

        if x < 0 or x >= len(self.cells[z][y]):
            return False

        return self.cells[z][y][x]

    def next_state(self, x, y, z):
        adjacent = self.get_adjacent(x, y, z)
        active_count = adjacent.count(True)
        current_state = self.cells[z][y][x]

        if 2 <= active_count <= 3 and current_state:
            return False
        if active_count == 3 and not current_state:
            return True

        return current_state

    def __str__(self):
        result = []
        for z_line in self.cells:
            z_slice = []
            for line in z_line:
                z_slice.append("".join([self.value_to_char(x) for x in line]))
            result.append("\n".join(z_slice))
        return "\n\n".join(result)

    def value_to_char(self, value):
        if value:
            return ACTIVE
        return INACTIVE

    def __copy__(self):
        return State(self.cells.copy())


def init_state(data):
    z0 = []
    for line in data:
        z0.append([char == ACTIVE for char in line])

    z1 = []
    for line in z0:
        z1.append([False for x in line])

    return State([z1, z0, z1.copy()])


def cycle(state, cycles=1):
    history = []
    depth = len(state.cells)
    height = len(state.cells[0])
    width = len(state.cells[0][0])

    for i in range(cycles):
        history.append(copy(state))
        next_state = []

        for z in range(0, depth):
            z_slice = []
            for y in range(0, height):
                z_slice.append([state.next_state(x, y, z) for x in range(0, width)])

        state = State(next_state)


###############################################################################
def run_a(input_data):
    state = init_state(input_data)
    print(state.next_state(1, 1, 1))
    # cycle(state)
    print(str(state))
    return ""


def run_b(input_data):
    return ""
