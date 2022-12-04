def parse_raw():
    with open('input.txt') as f:
        data = f.read().strip().split('\n')
        data = [pair.split(',') for pair in data]
        data = [[pair[0].split('-'), pair[1].split('-')] for pair in data]

        for idx, pair in enumerate(data):
            elf_1_start = int(pair[0][0])
            elf_1_stop = int(pair[0][1])
            elf_2_start = int(pair[1][0])
            elf_2_stop = int(pair[1][1])

            elf_1_range = range(elf_1_start, elf_1_stop + 1)
            elf_2_range = range(elf_2_start, elf_2_stop + 1)

            data[idx] = [set(elf_1_range), set(elf_2_range)]

    return data


data = parse_raw()


def part_one():
    count = 0
    for pair in data:
        if (pair[0].issubset(pair[1]) or pair[1].issubset(pair[0])):
            count += 1
    print(count)


def part_two():
    count = 0
    for pair in data:
        if (len(pair[0] & pair[1]) > 0):
            count += 1
    print(count)


part_one()
part_two()
