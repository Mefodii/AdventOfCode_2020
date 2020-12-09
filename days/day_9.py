class Preamble:
    def __init__(self, numbers, preamble_len):
        self.numbers = numbers
        self.preamble_len = preamble_len

        self.valid = True
        self.error_index = None
        self.error_number = None

        self.contiguous_range = None
        self.weakness = None

    def hack(self):
        self.contiguous_range = self.find_contiguous_range()
        self.weakness = max(self.contiguous_range) + min(self.contiguous_range)

    def validate(self):
        for i in range(self.preamble_len, len(self.numbers)):
            valid = self.validate_index(i)
            if not valid:
                self.error_index = i
                self.error_number = self.numbers[i]
                return

    def validate_index(self, index):
        expected_sum = self.numbers[index]

        for i in range(index - self.preamble_len, index - 1):
            first = self.numbers[i]
            for j in range(i + 1, index):
                second = self.numbers[j]
                if first != second and first + second == expected_sum:
                    return True

        return False

    def find_contiguous_range(self):
        if self.error_number is None:
            return None

        nrs = self.numbers
        expected_sum = self.error_number
        for i in range(len(nrs) - 1):
            actual_sum = nrs[i]
            for j in range(i + 1, len(nrs)):
                actual_sum += nrs[j]

                if actual_sum == expected_sum:
                    return nrs[i:j+1]
                if actual_sum > expected_sum:
                    break

        return None

    def __repr__(self):
        return f"{self.error_index} {self.error_number}"


###############################################################################
def run_a(input_data):
    test_preamble_len = 5
    real_preamble_len = 25
    numbers = [int(line) for line in input_data]
    preamble = Preamble(numbers, real_preamble_len)
    preamble.validate()
    print(preamble)
    return [preamble.error_index]


def run_b(input_data):
    test_preamble_len = 5
    real_preamble_len = 25
    numbers = [int(line) for line in input_data]
    preamble = Preamble(numbers, real_preamble_len)
    preamble.validate()
    preamble.hack()
    print(preamble.weakness)
    return [preamble.weakness]
