from utils.Validation import is_int

OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

OPEN_EXP = "("
CLOSE_EXP = ")"


def calculate_expression(exp, index):
    result = 0
    operation = OPERATIONS["+"]

    i = index
    while i < len(exp):
        arg = exp[i]

        if is_int(arg):
            result = operation(result, int(arg))
        elif arg == OPEN_EXP:
            new_result, new_index = calculate_expression(exp, i + 1)
            result = operation(result, new_result)
            i = new_index
        elif arg == CLOSE_EXP:
            return result, i
        else:
            operation = OPERATIONS[arg]

        i += 1

    return result, index


def calculate_expression_b(exp, index):
    # TODO - convert args and operation in single line expression
    args = []
    operations = []

    i = index
    while i < len(exp):
        arg = exp[i]

        if is_int(arg):
            args.append(int(arg))
        elif arg == OPEN_EXP:
            exp_result, new_index = calculate_expression(exp, i + 1)
            args.append(int(exp_result))
            i = new_index
        elif arg == CLOSE_EXP:
            return calculate(args, operations), i
        else:
            operations.append(arg)

        i += 1

    return calculate(args, operations), i


def calculate(args, operations):
    result = 0
    expression = ""

    # TODO - convert to string expression, add open parenthesis on arg before first + operation. Close after last.
    # TODO - should work with default eval.

    return eval(expression)


###############################################################################
def run_a(input_data):
    result = [calculate_expression(line.replace(" ", ""), 0)[0] for line in input_data]
    return [sum(result)]


def run_b(input_data):
    result = [calculate_expression(line.replace(" ", ""), 0)[0] for line in input_data]
    print(result)
    return [sum(result)]
