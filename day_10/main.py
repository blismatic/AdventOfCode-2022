def parse_raw():
    with open('input.txt') as f:
        data = f.read().strip().split('\n')
        data = [instruction.split() for instruction in data]
    return data


data = parse_raw()
# print(data)


def part_one():
    breakpoints = [20, 60, 100, 140, 180, 220]
    x_reg = 1
    cycle = 0
    strengths = {}

    for instruction in data:
        op = instruction[0]
        if op == 'noop':
            cycle += 1
            strengths[cycle] = x_reg * cycle
        elif op == 'addx':
            V = int(instruction[1])

            cycle += 1
            strengths[cycle] = x_reg * cycle

            cycle += 1
            strengths[cycle] = x_reg * cycle

            x_reg += V

    print(sum([strengths[val] for val in breakpoints]))


def part_two():
    width, height = (40, 6)
    pixels = list('.' * width * height)

    def update(x, cycle, pixels):
        position = (cycle - 1) % 40
        if position in [x - 1, x, x + 1]:
            pixels[cycle - 1] = '#'

    x_reg = 1
    cycle = 0

    for instruction in data:
        op = instruction[0]
        if op == 'noop':
            cycle += 1
            update(x_reg, cycle, pixels)
        elif op == 'addx':
            V = int(instruction[1])

            cycle += 1
            update(x_reg, cycle, pixels)

            cycle += 1
            update(x_reg, cycle, pixels)

            x_reg += V

    for i in range(height):
        print(''.join(pixels[i*width: i*width + width]))


part_one()
part_two()
