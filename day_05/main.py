def parse_raw():
    with open('input.txt') as f:
        data = f.read().split('\n')
        instructions = data[10:-1]

        horizontal_stacks = [stack[1::4] for stack in data[:8]]
        stacks = [[] for _ in range(9)]

        for row in reversed(horizontal_stacks):
            for position, crate in enumerate(row):
                if crate != ' ':
                    stacks[position].append(crate)

    return stacks, instructions


stacks, instructions = parse_raw()


def move_crates(amount, source, dest, part):
    if part == 1:
        for _ in range(amount):
            dest.append(source.pop())
    elif part == 2:
        dest.extend(source[-amount:])
        del source[-amount:]


def part_one():
    stacks = parse_raw()[0]

    for instruction in instructions:
        amount, source, dest = instruction.split()[1::2]
        move_crates(int(amount), stacks[int(source) - 1], stacks[int(dest) - 1], part=1)

    result = ''.join([stack.pop() for stack in stacks])
    print(result)


def part_two():
    stacks = parse_raw()[0]

    for instruction in instructions:
        amount, source, dest = instruction.split()[1::2]
        move_crates(int(amount), stacks[int(source) - 1], stacks[int(dest) - 1], part=2)

    result = ''.join([stack.pop() for stack in stacks])
    print(result)


part_one()
part_two()
