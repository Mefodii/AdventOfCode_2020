from utils.Validation import is_int


class Bus:
    def __init__(self, interval):
        self.interval = interval

    def get_next_earliest(self, client_time):
        return (int(client_time / self.interval) + 1) * self.interval

    def __repr__(self):
        return f"{self.interval}"


def get_earliest_depart(buses, client_time):
    depart = 999999999999999999
    earliest_bus = None
    for bus in buses:
        bus_depart = bus.get_next_earliest(client_time)
        if bus_depart < depart:
            depart = bus_depart
            earliest_bus = bus

    return earliest_bus, depart


###############################################################################
def run_a(input_data):
    client_time = int(input_data[0])
    buses = [Bus(int(arg)) for arg in input_data[1].split(",") if is_int(arg)]
    bus, depart_time = get_earliest_depart(buses, client_time)
    result = (depart_time - client_time) * bus.interval
    return [result]


def run_b(input_data):
    for i in range(1, 500):
        x = 7 * i
        for j in range(1, 500):
            y = 13 * j
            if x + 1 == y:
                print(x, i, j)
            elif y > x + 1:
                break

    print()
    for i in range(1, 500):
        x = 13 * i
        for j in range(1, 500):
            y = 59 * j
            if x + 3 == y:
                print(x, i, j)
            elif y > x + 3:
                break

    print()
    for i in range(1, 500):
        x = 59 * i
        for j in range(1, 500):
            y = 31 * j
            if x + 2 == y:
                print(x, i, j)
            elif y > x + 2:
                break

    print()
    for i in range(1, 500):
        x = 31 * i
        for j in range(1, 500):
            y = 19 * j
            if x + 1 == y:
                print(x, i, j)
            elif y > x + 1:
                break
    return ""
