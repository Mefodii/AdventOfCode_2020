from copy import copy

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"


class State:
    def __init__(self, data):
        self.data = data

    def get_adjacent(self, x, y, part_two):
        if part_two:
            return self.get_visible_adjacent(x, y)

        adjacent = [
            self.get_seat(x + 1, y),
            self.get_seat(x - 1, y),
            self.get_seat(x, y + 1),
            self.get_seat(x, y - 1),
            self.get_seat(x + 1, y + 1),
            self.get_seat(x + 1, y - 1),
            self.get_seat(x - 1, y + 1),
            self.get_seat(x - 1, y - 1),
        ]

        return [seat for seat in adjacent if seat]

    def get_visible_adjacent(self, x, y):
        adjacent = [
            self.get_seat_in_line(x, y, 1, 0),
            self.get_seat_in_line(x, y, -1, 0),
            self.get_seat_in_line(x, y, 0, 1),
            self.get_seat_in_line(x, y, 0, -1),
            self.get_seat_in_line(x, y, 1, 1),
            self.get_seat_in_line(x, y, 1, -1),
            self.get_seat_in_line(x, y, -1, 1),
            self.get_seat_in_line(x, y, -1, -1),
        ]

        return [seat for seat in adjacent if seat]

    def get_seat_in_line(self, x, y, x_offset, y_offset):
        seat = self.get_seat(x + x_offset, y + y_offset)
        if seat == FLOOR:
            seat = self.get_seat_in_line(x + x_offset, y + y_offset, x_offset, y_offset)
        return seat

    def get_seat(self, x, y):
        if y < 0 or y >= len(self.data):
            return None

        if x < 0 or x >= len(self.data[y]):
            return None

        return self.data[y][x]

    def next_state(self, x, y, part_two):
        adjacent = self.get_adjacent(x, y, part_two)
        occupied_seats = adjacent.count(OCCUPIED)
        current_seat = self.data[y][x]

        if occupied_seats == 0 and current_seat == EMPTY:
            return OCCUPIED

        if part_two:
            seat_tolerance = 5
        else:
            seat_tolerance = 4

        if occupied_seats >= seat_tolerance and current_seat == OCCUPIED:
            return EMPTY

        return current_seat

    def __eq__(self, other):
        return str(self.data) == str(other.data)

    def __str__(self):
        return "\n".join(self.data)

    def __copy__(self):
        return State(self.data.copy())


class Layout:
    def __init__(self, init_state, part_two=False):
        self.current_state = init_state
        self.width = len(init_state.data[0])
        self.height = len(init_state.data)
        self.history = []
        self.part_two = part_two

    def simulate(self):
        self.next_state()
        while not self.current_state == self.history[-1]:
            self.next_state()

    def next_state(self):
        self.history.append(copy(self.current_state))
        state = []
        for y in range(0, self.height):
            line = ""
            for x in range(0, self.width):
                line += self.current_state.next_state(x, y, self.part_two)
            state.append(line)

        self.current_state = State(state)

    def count_occupied(self):
        return str(self.current_state).count(OCCUPIED)

    def __str__(self):
        return str(self.current_state)


###############################################################################
def run_a(input_data):
    init_state = State(input_data)
    layout = Layout(init_state)
    layout.simulate()

    result = layout.count_occupied()
    print(result)
    return [result]


def run_b(input_data):
    init_state = State(input_data)
    layout = Layout(init_state, part_two=True)
    layout.simulate()

    result = layout.count_occupied()
    print(result)
    return [result]
