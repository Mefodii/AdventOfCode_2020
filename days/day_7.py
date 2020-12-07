import re


class Bag:
    NO_OTHER_BAGS = "no other bags"

    def __init__(self, raw_rule):
        self.raw_rule = raw_rule
        self.bag_name, self.contains = self.parse_rule()

    def parse_rule(self):
        attrs = self.raw_rule.split(" contain ")
        bag_name = re.search("(.*)\\sbag", attrs[0]).group(1)
        contains = {}
        for bag in attrs[1][:-1].split(", "):
            if not bag == self.NO_OTHER_BAGS:
                parse = re.search("(\\d+)\\s(.*)\\sbag", attrs[0])
                print(parse)
                count, name = parse.groups()
                contains[name] = count

        return bag_name, contains

    def __repr__(self):
        return f"{self.raw_rule} {self.bag_name} {str(self.contains)}"


###############################################################################
def run_a(input_data):
    bags = [Bag(line) for line in input_data]
    return ""


def run_b(input_data):
    return ""
