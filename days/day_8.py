ACC = "acc"
NOP = "nop"
JMP = "jmp"


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
        self.is_loop = False

    def tinker(self):
        for command in self.commands:
            old_name = command.name
            new_name = old_name
            if old_name == JMP:
                new_name = NOP
            elif old_name == NOP:
                new_name = JMP

            if not old_name == new_name:
                command.name = new_name
                self.execute()
                command.name = old_name

                if not self.is_loop:
                    return

    def execute(self):
        self.reset()
        while not self.stop:
            self.run_next()

    def reset(self):
        self.accumulator = 0
        self.command_position = 0
        self.stop = False
        self.is_loop = False
        for command in self.commands:
            command.execution_count = 0

    def run_next(self):
        if self.command_position >= len(self.commands):
            self.stop = True
            return

        command = self.commands[self.command_position]
        if command.execution_count > 0:
            self.stop = True
            self.is_loop = True
            return

        self.run_command(command)
        command.execution_count += 1

    def run_command(self, command):
        name = command.name
        if name == ACC:
            self.acc(command)
        elif name == JMP:
            self.jmp(command)
        elif name == NOP:
            self.nop()

    def jmp(self, command):
        self.command_position += command.value

    def acc(self, command):
        self.command_position += 1
        self.accumulator += command.value

    def nop(self):
        self.command_position += 1

    def __repr__(self):
        return f"{self.accumulator} {self.command_position} {self.is_loop}"


def build_command(command_data):
    arg1, arg2 = command_data.split(" ")
    return Command(arg1, arg2)


###############################################################################
def run_a(input_data):
    console = Console(list(map(build_command, input_data)))
    console.execute()
    print(console)
    return [console.accumulator]


def run_b(input_data):
    console = Console(list(map(build_command, input_data)))
    console.tinker()
    print(console)
    return [console.accumulator]
