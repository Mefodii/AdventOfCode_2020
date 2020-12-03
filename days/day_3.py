TREE = "#"


def slide_down(forest_map, step_x, step_y):
    trees_encountered = 0
    x, y = 0, 0

    finish = len(forest_map) - 1
    max_x = len(forest_map[0])
    while y < finish:
        x, y = move(x, y, step_x, step_y, max_x)
        if forest_map[y][x] == TREE:
            trees_encountered += 1

    return trees_encountered


def move(x, y, step_x, step_y, max_x):
    return (x + step_x) % max_x, y + step_y


###############################################################################
def run_a(input_data):
    step_x, step_y = 3, 1
    trees_encountered = slide_down(input_data, step_x, step_y)
    return [trees_encountered]


def run_b(input_data):
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]
    encounters = [slide_down(input_data, slope[0], slope[1]) for slope in slopes]
    result = 1
    for encounter in encounters:
        result *= encounter

    return [result]
