import math

TOTAL_ROWS = 127
TOTAL_COLUMNS = 7

F = "F"
B = "B"
L = "L"
R = "R"


def take_lower(low, high):
    return low, int((low + high) / 2)


def take_upper(low, high):
    return math.ceil((low + high) / 2), high


SLICES = {
    F: take_lower,
    B: take_upper,
    L: take_lower,
    R: take_upper,
}


class BoardPass:
    def __init__(self, data):
        self.seat_pass = data
        self.row = BoardPass.slice_it(0, TOTAL_ROWS, self.seat_pass[0:7])
        self.column = BoardPass.slice_it(0, TOTAL_COLUMNS, self.seat_pass[7:])
        self.seat_id = self.row * 8 + self.column

    @staticmethod
    def slice_it(low, high, data):
        for char in data:
            low, high = SLICES[char](low, high)
        return low


def find_missing_seat(board_passes):
    id_list = [board_pass.seat_id for board_pass in board_passes]
    id_list.sort()
    prev = id_list[0]
    for i in range(1, len(id_list)):
        current = id_list[i]
        if current - prev != 1:
            return current - 1
        prev = current

    return None


###############################################################################
def run_a(input_data):
    board_passes = [BoardPass(line) for line in input_data]
    max_id = -1
    for board_pass in board_passes:
        max_id = max(max_id, board_pass.seat_id)
    return [max_id]


def run_b(input_data):
    board_passes = [BoardPass(line) for line in input_data]
    missing_id = find_missing_seat(board_passes)
    return [missing_id]
