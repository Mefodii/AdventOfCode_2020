class Command:
    def __init__(self, name, value):
        self.name = name
        self.value = int(value)
        self.execution_count = 0

    def __repr__(self):
        return f"{self.name} {self.value}"


class Console:

    def __init__(self, commands):
        self.commands = commands
        self.accumulator = 0
        self.command_position = 0
        self.stop = False

    def execute(self):
        while not self.stop:
            acc, next_cmd, stop = self.run_command(self.commands[self.command_position])

    def run_command(self, command):
        return 0, 0, True

    def jmp(self, command):
        pass

    def acc(self):
        pass

    def nop(self):
        pass

    COMMANDS = {
        "acc": acc,
        "jmp": jmp,
        "nop": nop,
    }


def build_command(command_data):
    arg1, arg2 = command_data.split(" ")
    return Command(arg1, arg2)


###############################################################################
def run_a(input_data):
    console = Console(list(map(build_command, input_data)))
    return ""


def run_b(input_data):
    return ""
