import math

MAX_DIFF = 3


class Outlet:
    def __init__(self, adapters):
        self.adapters = adapters
        self.adapters.sort()
        self.joltage = 0
        self.stats = {}

    def connect(self):
        for adapter in self.adapters:
            difference = adapter - self.joltage
            self.stats[difference] = self.stats.get(difference, 0) + 1
            self.joltage = adapter

        self.joltage += 3
        self.stats[3] = self.stats.get(3, 0) + 1


def combinations(adapters):
    group_size = 0
    comb_map = []
    combs = {
        1: 2,
        2: 4,
        3: 7,
    }
    for i in range(1, len(adapters) - 1):
        removable = adapters[i+1] - adapters[i-1] <= MAX_DIFF
        if removable:
            group_size += 1
        else:
            if group_size > 0:
                comb_map.append(combs[group_size])
            group_size = 0

    return math.prod(comb_map)


###############################################################################
def run_a(input_data):
    adapters = [int(line) for line in input_data]
    outlet = Outlet(adapters)
    outlet.connect()

    result = outlet.stats.get(1, 0) * outlet.stats.get(3, 0)
    print(result)
    return [result]


def run_b(input_data):
    adapters = [int(line) for line in input_data]
    adapters.sort()
    result = combinations([0] + adapters + [adapters[-1] + 3])
    print(result)
    return [result]
