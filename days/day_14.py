MASK_CMD = "mask"
MEM_CMD = "mem"


class Mask:
    def __init__(self, value):
        self.value = value


class Memory:
    def __init__(self, mask):
        self.mask = mask
        self.value = None
        self.write_value(0)

    def write_value(self, value):
        binary_value = format(value, "036b")
        self.value = ""
        for i in range(len(binary_value)):
            if self.mask.value[i:i + 1] == "X":
                self.value += binary_value[i:i + 1]
            else:
                self.value += self.mask.value[i:i + 1]


def parse_line(line):
    args = {}
    command, value = line.split(" = ")
    if command == MASK_CMD:
        return {MASK_CMD: value}

    #  Get value between brackets
    mem_index = int(command.split("[")[1][:-1])
    return {MEM_CMD: [mem_index, int(value)]}


def run_commands(data):
    memory = {}
    mask = Mask("")

    for line in data:
        cmd = parse_line(line)
        if cmd.get(MASK_CMD, None):
            mask.value = cmd[MASK_CMD]
        else:
            index, value = cmd[MEM_CMD]
            if index not in memory:
                memory[index] = Memory(mask)

            memory[index].write_value(value)

    return memory, mask


def calc_memory_sum(memory):
    checksum = 0
    for mem in memory.values():
        checksum += int(mem.value, 2)

    return checksum


def apply_mask_to_memory(index, mask):
    binary_value = format(index, "036b")
    result = ""
    pows = []
    for i in range(len(binary_value)):
        if mask.value[i:i + 1] == "0":
            result += binary_value[i:i + 1]
        else:
            result += mask.value[i:i + 1]

        if mask.value[i:i + 1] == "X":
            pows.append(35 - i)

    offset = int(result.replace("X", "0"), 2)
    return generate_memories(pows, offset)


def generate_memories(pows, offset):
    current_pow = pows[0]
    result = [offset, offset + pow(2, current_pow)]

    if len(pows) > 1:
        rest_pows = pows[1:]
        result += generate_memories(rest_pows, offset) + generate_memories(rest_pows, offset + pow(2, current_pow))
    return result


def run_commands_b(data):
    memory = {}
    mask = Mask("")

    for line in data:
        cmd = parse_line(line)
        if cmd.get(MASK_CMD, None):
            mask.value = cmd[MASK_CMD]
        else:
            index, value = cmd[MEM_CMD]
            indexes = apply_mask_to_memory(index, mask)
            for i in set(indexes):
                memory[i] = value

    return memory, mask


###############################################################################
def run_a(input_data):
    memory, mask = run_commands(input_data)
    result = calc_memory_sum(memory)
    return [result]


def run_b(input_data):
    memory, mask = run_commands_b(input_data)
    result = sum(memory.values())
    return [result]
