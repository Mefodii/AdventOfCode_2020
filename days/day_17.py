from copy import copy

ACTIVE = "#"
INACTIVE = "."

class State:
    def __init__(self, cells):
        self.cells = cells

    def get_adjacent(self, x, y, z):
        return [self.get_cell(x + x1, y + y1, z + z1)
                for x1 in range(-1, 2, 1)
                for y1 in range(-1, 2, 1)
                for z1 in range(-1, 2, 1)
                if not x1 == y1 == z1 == 0]

    def get_cell(self, x, y, z):
        if z < 0 or z >= len(self.cells):
            return False

        if y < 0 or y >= len(self.cells[z]):
            return False

        if x < 0 or x >= len(self.cells[z][y]):
            return False

        return self.cells[z][y][x]

    def active_count(self):
        active_count = 0
        for z_slice in self.cells:
            for line in z_slice:
                active_count += line.count(True)

        return active_count

    def extend(self):
        new_cells = []
        for z_slice in self.cells:
            new_slice = []
            for line in z_slice:
                new_line = [False] + line.copy() + [False]
                new_slice.append(new_line)
            new_slice = [[False] * len(new_slice[0])] + new_slice + [[False] * len(new_slice[0])]
            new_cells.append(new_slice)

        empty_slice = []
        for line in new_cells[0]:
            empty_slice.append([False] * len(new_cells[0][0]))

        self.cells = [empty_slice] + new_cells + [empty_slice]

    def next_state(self, x, y, z):
        adjacent = self.get_adjacent(x, y, z)
        active_count = adjacent.count(True)
        current_state = self.cells[z][y][x]

        if (not 2 <= active_count <= 3) and current_state:
            return False
        if active_count == 3 and not current_state:
            return True

        return current_state

    def __str__(self):
        def value_to_char(value):
            if value:
                return ACTIVE
            return INACTIVE

        result = []
        for z_line in self.cells:
            z_slice = []
            for line in z_line:
                z_slice.append("".join([value_to_char(x) for x in line]))
            result.append("\n".join(z_slice))
        return "\n\n".join(result)

    def __copy__(self):
        return State(self.cells.copy())


class State4D:
    def __init__(self, cells):
        self.cells = cells

    def get_adjacent(self, x, y, z, w):
        return [self.get_cell(x + x1, y + y1, z + z1, w + w1)
                for x1 in range(-1, 2, 1)
                for y1 in range(-1, 2, 1)
                for z1 in range(-1, 2, 1)
                for w1 in range(-1, 2, 1)
                if not x1 == y1 == z1 == w1 == 0]

    def get_cell(self, x, y, z, w):
        if w < 0 or w >= len(self.cells):
            return False

        if z < 0 or z >= len(self.cells[w]):
            return False

        if y < 0 or y >= len(self.cells[w][z]):
            return False

        if x < 0 or x >= len(self.cells[w][z][y]):
            return False

        return self.cells[w][z][y][x]

    def active_count(self):
        active_count = 0
        for w_slice in self.cells:
            for z_slice in w_slice:
                for line in z_slice:
                    active_count += line.count(True)

        return active_count

    def extend(self):
        new_cells = []
        for w_slice in self.cells:
            new_w = []
            for z_slice in w_slice:
                new_z = []
                for line in z_slice:
                    new_line = [False] + line.copy() + [False]
                    new_z.append(new_line)
                new_z = [[False] * len(new_z[0])] + new_z + [[False] * len(new_z[0])]
                new_w.append(new_z)

            empty_z = []
            for _ in new_w[0]:
                empty_z.append([False] * len(new_w[0][0]))

            new_w = [empty_z] + new_w + [empty_z]
            new_cells.append(new_w)

        empty_w = []
        for z_slice in new_cells[0]:
            empty_z = []
            for _ in z_slice[0]:
                empty_z.append([False] * len(z_slice[0]))
            empty_w.append(empty_z)

        self.cells = [empty_w] + new_cells + [empty_w]

    def next_state(self, x, y, z, w):
        adjacent = self.get_adjacent(x, y, z, w)
        active_count = adjacent.count(True)
        current_state = self.cells[w][z][y][x]

        if (not 2 <= active_count <= 3) and current_state:
            return False
        if active_count == 3 and not current_state:
            return True

        return current_state

    def __str__(self):
        def value_to_char(value):
            if value:
                return ACTIVE
            return INACTIVE

        result = []

        for w_slice in self.cells:
            w_line = []
            for z_slice in w_slice:
                z_line = []
                for line in z_slice:
                    z_line.append("".join([value_to_char(x) for x in line]))
                w_line.append("\n".join(z_line))
            result.append("\n\n".join(w_line))
        return "\n\n".join(result)

    def __copy__(self):
        return State(self.cells.copy())


def init_state(data):
    z0 = []
    for line in data:
        z0.append([char == ACTIVE for char in line])

    z1 = []
    for line in z0:
        z1.append([False for x in line])

    return State([z1, z0, z1])


def init_state4d(data):
    z0 = []
    for line in data:
        z0.append([char == ACTIVE for char in line])

    z1 = []
    for line in z0:
        z1.append([False for x in line])

    cells = [[z1, z1, z1], [z1, z0, z1.copy()], [z1, z1, z1]]
    return State4D(cells)


def cycle(state, cycles=6):
    for i in range(cycles):
        state.extend()
        next_state = []

        depth, height, width = len(state.cells), len(state.cells[0]), len(state.cells[0][0])
        for z in range(0, depth):
            z_slice = []
            for y in range(0, height):
                z_slice.append([state.next_state(x, y, z) for x in range(0, width)])
            next_state.append(z_slice)

        state = State(next_state)

    return state


def cycle4d(state, cycles=6):
    for i in range(cycles):
        state.extend()
        next_state = []

        hyper, depth, height, width = len(state.cells), len(state.cells[0]), len(state.cells[0][0]), len(state.cells[0][0][0])
        for w in range(0, hyper):
            w_slice = []
            for z in range(0, depth):
                z_slice = []
                for y in range(0, height):
                    z_slice.append([state.next_state(x, y, z, w) for x in range(0, width)])
                w_slice.append(z_slice)
            next_state.append(w_slice)

        state = State4D(next_state)

    return state


###############################################################################
def run_a(input_data):
    state = init_state(input_data)
    state = cycle(state)
    result = state.active_count()
    return [result]


def run_b(input_data):
    state = init_state4d(input_data)
    state = cycle4d(state)
    result = state.active_count()
    return [result]
