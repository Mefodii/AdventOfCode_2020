import re


class Rule:
    def __init__(self, raw_data):
        regex = "^(.*)[:]\\s(\\d+)[-](\\d+).*\\s(\\d+)[-](\\d+)"
        args = re.search(regex, raw_data)
        self.name = args.group(1)
        self.min1, self.max1 = int(args.group(2)), int(args.group(3))
        self.min2, self.max2 = int(args.group(4)), int(args.group(5))

    def in_range(self, value):
        return value in range(self.min1, self.max1 + 1) or value in range(self.min2, self.max2 + 1)

    def __repr__(self):
        return f"{self.name} {self.min1} {self.max1} {self.min2} {self.max2}"


class Ticket:
    def __init__(self, raw_data):
        self.fields = [int(n) for n in raw_data.split(",")]

    def __repr__(self):
        return f"{str(self.fields)}"

    def find_invalid(self, rules):
        return [field for field in self.fields if not any([rule.in_range(field) for rule in rules])]


def build_objects(data):
    rules_data, my_ticket_data, nearby_tickets_data = "\n".join(data).split("\n\n")

    rules = [Rule(line) for line in rules_data.split("\n")]
    my_ticket = Ticket(my_ticket_data.split("\n")[1])
    nearby_tickets = [Ticket(line) for line in nearby_tickets_data.split("\n")[1:]]

    return rules, my_ticket, nearby_tickets


def get_invalid_fields(rules, tickets):
    invalid_fields = []

    for ticket in tickets:
        invalid_fields += ticket.find_invalid(rules)

    return invalid_fields


###############################################################################
def run_a(input_data):
    rules, my_ticket, nearby_tickets = build_objects(input_data)
    invalid_fields = get_invalid_fields(rules, nearby_tickets)
    result = sum(invalid_fields)
    return [result]


def run_b(input_data):
    return ""
