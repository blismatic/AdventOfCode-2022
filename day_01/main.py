with open('input.txt') as f:
    input = [[int(calorie) for calorie in elf.split('\n')]
             for elf in f.read().strip().split('\n\n')]

    elves = sorted([sum(elf) for elf in input], reverse=True)


def puzzle_1():
    print(elves[0])


def puzzle_2():
    print(sum(elves[:3]))


puzzle_1()
puzzle_2()
