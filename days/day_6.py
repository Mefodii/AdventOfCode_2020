class Group:
    def __init__(self, data, part_b=False):
        self.user_answers = data
        self.unique_answers = set("".join(self.user_answers))
        self.answers = len(self.unique_answers)
        self.same_answers = self.count_same_answers()
        self.part_b = part_b

    def count_same_answers(self):
        def has_all(answer):
            return all(answer in user_answer for user_answer in self.user_answers)

        return sum(has_all(answer) for answer in self.unique_answers)

    def __repr__(self):
        return f"{str(self.user_answers)} {str(self.unique_answers)} {str(self.answers)} {self.same_answers}"

    def __radd__(self, other):
        if self.part_b:
            return other + self.same_answers

        return other + self.answers


def build_groups(data, part_b=False):
    groups = []
    group_data = []
    for line in data:
        if len(line.strip()) == 0:
            groups.append(Group(group_data, part_b))
            group_data = []
        else:
            group_data.append(line)

    if len(group_data) > 0:
        groups.append(Group(group_data, part_b))

    return groups


###############################################################################
def run_a(input_data):
    groups = build_groups(input_data)
    return [sum(groups)]


def run_b(input_data):
    groups = build_groups(input_data, True)
    return [sum(groups)]
