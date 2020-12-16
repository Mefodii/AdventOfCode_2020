def play_game(numbers, turns=2020):
    turn = 0
    log = {}
    last_say = None
    for number in numbers:
        turn += 1
        log[number] = [turn, turn]
        last_say = number

    while turn < turns:
        turn += 1

        occurrences = log.get(last_say)
        last_say = occurrences[-1] - occurrences[-2]

        occurrences = log.get(last_say, None)
        if occurrences:
            occurrences[0] = occurrences[1]
            occurrences[1] = turn
        else:
            log[last_say] = [turn, turn]

    return last_say


###############################################################################
def run_a(input_data):
    result = []
    for line in input_data:
        numbers = [int(n) for n in line.split(",")]
        result.append(play_game(numbers))
    return result


def run_b(input_data):
    result = []
    for line in input_data:
        numbers = [int(n) for n in line.split(",")]
        result.append(play_game(numbers, 30000000))
    return result
