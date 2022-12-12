def parse_raw():
    monkeys = {}
    with open('input.txt') as f:
        data = f.read().strip().split('\n\n')
        data = [line.strip().split('\n') for line in data]
        for idx_1, monkey in enumerate(data):
            for idx_2, _ in enumerate(monkey):
                data[idx_1][idx_2] = data[idx_1][idx_2].strip()

    for monkey in data:
        num = int(monkey[0].split()[1][:-1])
        starting_items = [int(item) for item in monkey[1][16:].split(', ')]
        operation = monkey[2][20:].split()
        test = int(monkey[3][19:])
        if_true = int(monkey[4].split()[-1])
        if_false = int(monkey[5].split()[-1])

        monkeys[num] = {
            'starting items': starting_items,
            'operation': operation,
            'test': test,
            'if true': if_true,
            'if false': if_false,
            'inspected': 0
        }
    return monkeys


monkeys = parse_raw()
# print(monkeys['3'])


def turn(m, part):
    monkey = monkeys[m]
    # print(f'Monkey {m}:')
    for item in monkey['starting items']:
        amt = ''
        worry_level = item
        monkey['inspected'] += 1
        if monkey['operation'][1] == 'old':
            worry_level = (
                worry_level * worry_level) if monkey['operation'][0] == '*' else (worry_level + worry_level)
        else:
            amt = int(monkey['operation'][1])
            worry_level = (
                worry_level * amt) if monkey['operation'][0] == '*' else (worry_level + amt)
        if part == 1:
            worry_level = worry_level // 3
        if (worry_level % monkey['test'] == 0):
            monkeys[monkey['if true']]['starting items'].append(worry_level)
        else:
            monkeys[monkey['if false']]['starting items'].append(worry_level)

    monkey['starting items'] = []


def part_one():
    for _ in range(20):
        for monkey in monkeys:
            turn(monkey, 1)

    test = []
    for m in monkeys:
        monkey = monkeys[m]
        test.append(monkey['inspected'])
    most_active = sorted(test, reverse=True)

    print(most_active[0] * most_active[1])


def part_two():
    for _ in range(10000):
        for monkey in monkeys:
            turn(monkey, 2)

    test = []
    for m in monkeys:
        monkey = monkeys[m]
        test.append(monkey['inspected'])
    most_active = sorted(test, reverse=True)

    print(most_active[0] * most_active[1])


part_one()
part_two()
