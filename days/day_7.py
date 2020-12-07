import re


class Bag:
    NO_OTHER_BAGS = "no other bags"

    def __init__(self, raw_rule):
        self.raw_rule = raw_rule
        self.bag_name, self.contains = self.parse_rule()
        self.parents = {}
        self.children = {}

    def parse_rule(self):
        attrs = self.raw_rule.split(" contain ")
        bag_name = re.search("(.*)\\sbag", attrs[0]).group(1)
        contains = {}
        for bag in attrs[1][:-1].split(", "):
            if not bag == self.NO_OTHER_BAGS:
                parse = re.search("(\\d+)\\s(.*)\\sbag", bag)
                count, name = parse.groups()
                contains[name] = count

        return bag_name, contains

    def __repr__(self):
        return f"{self.bag_name} {str(self.contains)} {str(self.children)}"


def connect_bags(bags):
    for parent in bags.values():
        for child_name, child_value in parent.contains.items():
            child = bags.get(child_name)
            parent.children[child_name] = {"bag": child, "cost": child_value}
            child.parents[parent.bag_name] = parent


def build_bags_dict(data):
    bags = {}
    for line in data:
        bag = Bag(line)
        bags[bag.bag_name] = bag

    connect_bags(bags)

    return bags


def get_unique_containers(bag):
    containers = set()
    for parent in bag.parents.values():
        containers.add(parent.bag_name)
        containers = containers.union(get_unique_containers(parent))

    return containers


def calculate_bags(bag):
    count = 0
    for child in bag.children.values():
        cost = int(child.get("cost"))
        count += cost + cost * calculate_bags(child.get("bag"))

    return count


###############################################################################
def run_a(input_data):
    bags = build_bags_dict(input_data)
    containers = get_unique_containers(bags.get("shiny gold"))
    print(containers)
    return [len(containers)]


def run_b(input_data):
    bags = build_bags_dict(input_data)
    count = calculate_bags(bags.get("shiny gold"))
    print(count)
    return [count]
