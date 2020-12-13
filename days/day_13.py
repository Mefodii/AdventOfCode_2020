from utils.Validation import is_int


class Bus:
    def __init__(self, interval):
        self.interval = interval

    def get_next_earliest(self, client_time):
        return (int(client_time / self.interval) + 1) * self.interval

    def __repr__(self):
        return f"{self.interval}"


class ComboBus:
    def __init__(self, interval, bus_id, offset):
        self.interval = interval
        self.bus_id = bus_id
        self.offset = offset

    def get_next_earliest(self, client_time):
        return (int(client_time / self.interval) + 1) * self.interval

    def combine(self, other_bus):
        distance = other_bus.bus_id - self.bus_id

        run = True
        i = 0
        j = int(self.offset / other_bus.interval) if self.offset > 0 else 1
        jump = int(self.interval / other_bus.interval) - 1 if self.interval > other_bus.interval else 0

        while run:
            this_sum = self.interval * i + self.offset
            while True:
                other_sum = other_bus.interval * j + other_bus.offset
                if this_sum + distance == other_sum:
                    bus = ComboBus(self.interval * other_bus.interval, 0, this_sum - self.bus_id)
                    return bus
                elif other_sum > this_sum + distance:
                    j += jump
                    break
                j += 1
            i += 1

    def __repr__(self):
        return f"{self.interval} {self.offset}"


def get_earliest_depart(buses, client_time):
    depart = 999999999999999999
    earliest_bus = None
    for bus in buses:
        bus_depart = bus.get_next_earliest(client_time)
        if bus_depart < depart:
            depart = bus_depart
            earliest_bus = bus

    return earliest_bus, depart


def build_combo(data):
    buses = []
    bus_data = data.split(",")
    for i in range(len(bus_data)):
        if is_int(bus_data[i]):
            buses.append(ComboBus(int(bus_data[i]), i, 0))

    return buses


def combine(buses):
    combined = buses[0]
    for bus in buses[1:]:
        combined = combined.combine(bus)

    return combined


###############################################################################
def run_a(input_data):
    client_time = int(input_data[0])
    buses = [Bus(int(arg)) for arg in input_data[1].split(",") if is_int(arg)]
    bus, depart_time = get_earliest_depart(buses, client_time)
    result = (depart_time - client_time) * bus.interval
    return [result]


def run_b(input_data):
    combo = build_combo(input_data[1])
    combined = combine(combo)
    return [combined.offset]
