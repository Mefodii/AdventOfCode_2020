class Password:
    def __init__(self, raw_data):
        params = raw_data.split(" ")
        occurs = params[0].split("-")
        self.min_occur = int(occurs[0])
        self.max_occur = int(occurs[1])
        self.char_occur = params[1].replace(":", "")
        self.password = params[2]
        self.is_valid = False

        self.check_validity()

    def check_validity(self):
        occurs = self.password.count(self.char_occur)
        if self.min_occur <= occurs <= self.max_occur:
            self.is_valid = True
        else:
            self.is_valid = False

    def __str__(self):
        return f'{self.min_occur} {self.max_occur}, {self.char_occur}, {self.password} - {self.is_valid}'
###############################################################################


class PasswordB:
    def __init__(self, raw_data):
        params = raw_data.split(" ")
        occurs = params[0].split("-")
        self.first_occur = int(occurs[0])
        self.second_occur = int(occurs[1])
        self.char_occur = params[1].replace(":", "")
        self.password = params[2]
        self.is_valid = False

        self.check_validity()

    def check_validity(self):
        has_first_occur = self.password[self.first_occur - 1] == self.char_occur
        has_second_occur = self.password[self.second_occur - 1] == self.char_occur

        if (has_first_occur and has_second_occur) or (not has_first_occur and not has_second_occur):
            self.is_valid = False
        else:
            self.is_valid = True

    def __str__(self):
        return f'{self.min_occur} {self.max_occur}, {self.char_occur}, {self.password} - {self.is_valid}'


###############################################################################
def run_a(input_data):
    objects = [Password(line) for line in input_data]
    valid_passwords_count = 0
    for obj in objects:
        if obj.is_valid:
            valid_passwords_count += 1
    return [str(valid_passwords_count)]


def run_b(input_data):
    objects = [PasswordB(line) for line in input_data]
    valid_passwords_count = 0
    for obj in objects:
        if obj.is_valid:
            valid_passwords_count += 1
    return [str(valid_passwords_count)]
