def parse_raw():
    with open('input.txt') as f:
        data = f.read().strip().split('\n')
    return data


data = parse_raw()


def prio(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


def part_one():
    halves = [[rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]] for rucksack in data]
    duplicates = [''.join(set(rucksack[0]) & set(rucksack[1])) for rucksack in halves]

    answer = sum([prio(char) for char in duplicates])
    print(answer)


def part_two():
    triplets = list(zip(*[iter(data)]*3))
    duplicates = [''.join(set(triplet[0]) & set(triplet[1]) & set(triplet[2])) for triplet in triplets]

    answer = sum([prio(char) for char in duplicates])
    print(answer)


part_one()
part_two()
