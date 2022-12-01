def puzzle_1():
    with open('input.txt') as f:
        input = f.read().split('\n\n')
        input = [line.split('\n') for line in input]

        # Convert strings to ints
        for idx, elf in enumerate(input):
            input[idx] = [int(calorie) for calorie in elf if calorie != '']

    print(max([sum(elf) for elf in input]))


def puzzle_2():
    with open('input.txt') as f:
        input = f.read().split('\n\n')
        input = [line.split('\n') for line in input]

        # Convert strings to ints
        for idx, elf in enumerate(input):
            input[idx] = [int(calorie) for calorie in elf if calorie != '']

    calories = sorted([sum(elf) for elf in input])
    print(sum(calories[-3:]))


puzzle_1()
puzzle_2()
