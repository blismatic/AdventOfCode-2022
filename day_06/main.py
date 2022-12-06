def parse_raw():
    with open('input.txt') as f:
        data = f.read().strip()
    return data


data = parse_raw()


def find_unique_sequence(datastream_buffer, n):
    for idx, _ in enumerate(datastream_buffer):
        next_N_characters = data[idx:idx + n]
        if len(set(next_N_characters)) == n:
            return idx + n


def part_one():
    start_of_packet = find_unique_sequence(data, n=4)
    print(start_of_packet)


def part_two():
    start_of_message = find_unique_sequence(data, n=14)
    print(start_of_message)


part_one()
part_two()
