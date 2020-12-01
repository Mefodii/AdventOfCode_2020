def find_checksum(data, checksum):
    last_index = len(data) - 1

    end_index = last_index

    for i in range(0, end_index):
        start_value = data[i]
        for j in range(end_index, i, -1):
            end_value = data[j]

            added = start_value + end_value

            if added < checksum:
                end_index = min(j + 1, last_index)
                break
            elif added == checksum:
                return start_value * end_value


def find_checksum_b(data, checksum):
    last_index = len(data) - 1

    end_index = last_index

    for i in range(0, end_index):
        start_value = data[i]
        for k in range(i+1, end_index):
            mid_value = data[k]
            for j in range(end_index, k, -1):
                end_value = data[j]

                added = start_value + end_value + mid_value

                if added < checksum:
                    end_index = min(j + 1, last_index)
                    break
                elif added == checksum:
                    return start_value * end_value * mid_value


def sort_as_int(data):
    int_data = [int(value) for value in data]
    int_data.sort()
    return int_data


###############################################################################
def run_a(input_data):
    checksum = 2020
    sorted_data = sort_as_int(input_data)
    result = find_checksum(sorted_data, checksum)
    return [str(result)]


def run_b(input_data):
    checksum = 2020
    sorted_data = sort_as_int(input_data)
    result = find_checksum_b(sorted_data, checksum)
    return [str(result)]
