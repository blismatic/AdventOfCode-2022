from collections import Counter


def parse_raw():
    with open('input.txt') as f:
        raw_data = f.read().strip().split('\n')

    data = Counter()
    cwd = []
    command = ''
    for line in raw_data:
        if line.startswith('dir'):
            continue
        if line.startswith('$'):
            command, *args = line.split()[1:]
            if command == 'cd':
                arg = args.pop()
                if arg == '..':
                    cwd.pop()
                else:
                    cwd.append(arg)
        elif command == 'ls':
            size = int(line.split()[0])
            for i in range(len(cwd)):
                key = tuple(cwd[:i + 1])
                data[key] += size
    return data


data = parse_raw()
# print(data)


def part_one():
    sizes = data.values()
    print(sum([dir_size for dir_size in sizes if dir_size <= 100_000]))


def part_two():
    used_space = data[tuple('/')]
    available_space = 70_000_000 - used_space

    needed_space = 30_000_000 - available_space

    sizes = sorted(data.values())
    for size in sizes:
        if size >= needed_space:
            print(size)
            return


part_one()
part_two()
