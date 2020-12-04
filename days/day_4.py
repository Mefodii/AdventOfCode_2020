import re

from utils.Validation import is_int

BYR = "byr"
IYR = "iyr"
EYR = "eyr"
HGT = "hgt"
HCL = "hcl"
ECL = "ecl"
PID = "pid"
CID = "cid"

MANDATORY = [BYR, IYR, EYR, HGT, HCL, ECL, PID]
OPTIONAL = [CID]


class Passport:
    def __init__(self, raw_data):
        self.fields = {}
        self.is_valid = True

        self.build_fields(raw_data.strip().split(" "))
        self.validate()

    def build_fields(self, params):
        for param in params:
            field_name, field_value = param.split(":")
            self.fields[field_name] = field_value

    def validate(self):
        for mandatory_field in MANDATORY:
            if self.fields.get(mandatory_field, None) is None:
                self.is_valid = False
                return

    def values_validation(self):
        if not self.is_valid:
            return

        if self.validate_byr() and self.validate_iyr() and self.validate_eyr() and self.validate_hgt()\
                and self.validate_hcl() and self.validate_ecl() and self.validate_pid():
            pass
        else:
            self.is_valid = False

    def validate_byr(self):
        min_value = 1920
        max_value = 2002

        value = self.fields.get(BYR)
        if len(value) == 4 and is_int(value):
            return min_value <= int(value) <= max_value
        return False

    def validate_iyr(self):
        min_value = 2010
        max_value = 2020

        value = self.fields.get(IYR)
        if len(value) == 4 and is_int(value):
            return min_value <= int(value) <= max_value
        return False

    def validate_eyr(self):
        min_value = 2020
        max_value = 2030

        value = self.fields.get(EYR)
        if len(value) == 4 and is_int(value):
            return min_value <= int(value) <= max_value
        return False

    def validate_hgt(self):
        value = self.fields.get(HGT)
        if len(value) >= 4:
            if value[-2:] == "cm":
                min_value = 150
                max_value = 190
            elif value[-2:] == "in":
                min_value = 59
                max_value = 76
            else:
                return False

            if is_int(value[:-2]):
                return min_value <= int(value[:-2]) <= max_value

    def validate_hcl(self):
        regex = "^[#][a-z0-9]{6}"
        return re.search(regex, self.fields.get(HCL))

    def validate_ecl(self):
        valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.fields.get(ECL) in valid_colors

    def validate_pid(self):
        value = self.fields.get(PID)
        return len(value) == 9 and is_int(value)


def build_passports(data):
    passport_raw_data = []
    passports = []
    for line in data:
        if len(line.strip()) == 0:
            passports.append(Passport(" ".join(passport_raw_data)))
            passport_raw_data = []
        else:
            passport_raw_data.append(line)

    if len(passport_raw_data) > 0:
        passports.append(Passport(" ".join(passport_raw_data)))

    return passports


###############################################################################
def run_a(input_data):
    passports = build_passports(input_data)
    valid_passports = 0
    for passport in passports:
        if passport.is_valid:
            valid_passports += 1

    return [valid_passports]


def run_b(input_data):
    passports = build_passports(input_data)
    valid_passports = 0
    for passport in passports:
        passport.values_validation()
        if passport.is_valid:
            valid_passports += 1

    return [valid_passports]
