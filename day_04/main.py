def parse_raw():
    with open('input.txt') as f:
        data = f.read().strip().split('\n')
        data = [pair.split(',') for pair in data]
    return data


data = parse_raw()


def part_one():
    count = 0

    for pairs in data:
        elf_1 = pairs[0].split('-')
        elf_2 = pairs[1].split('-')

        range1 = set(range(int(elf_1[0]), int(elf_1[1]) + 1))
        range2 = set(range(int(elf_2[0]), int(elf_2[1]) + 1))

        if (range1.issubset(range2) or range2.issubset(range1)):
            count += 1

    print(count)


def part_two():
    count = 0

    for pairs in data:
        elf_1 = pairs[0].split('-')
        elf_2 = pairs[1].split('-')

        range1 = set(range(int(elf_1[0]), int(elf_1[1]) + 1))
        range2 = set(range(int(elf_2[0]), int(elf_2[1]) + 1))

        if (len(range1 & range2) > 0):
            count += 1

    print(count)


part_one()
part_two()
