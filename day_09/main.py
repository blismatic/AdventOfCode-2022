def parse_raw():
    with open('input.txt') as f:
        data = f.read().strip().split('\n')
    return data


data = parse_raw()
# print(data)


class Knot:
    x = 0
    y = 0

    def move(self, direction):
        match direction:
            case 'R':
                self.x += 1
            case 'L':
                self.x -= 1
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1

    def follow(self, other):
        # ---------------------
        # Cardinal directions |
        # ---------------------
        if (other.x == self.x) and (other.y == self.y + 2):
            '''
            ......    ......
            .O....    .O....
            ...... -> .S.... (other is 2 units above self)
            .S....    ......
            ......    ......
            '''
            self.y += 1
        elif (other.x == self.x) and (other.y == self.y - 2):
            '''
            ......    ......
            .S....    ......
            ...... -> .S.... (other is 2 units below self)
            .O....    .O....
            ......    ......
            '''
            self.y -= 1
        elif (other.y == self.y) and (other.x == self.x + 2):
            '''
            ......    ......
            ......    ......
            ..S.O. -> ...SO. (other is 2 units right of self)
            ......    ......
            ......    ......
            '''
            self.x += 1
        elif (other.y == self.y) and (other.x == self.x - 2):
            '''
            ......    ......
            ......    ......
            .O.S.. -> .OS... (other is 2 units left of self)
            ......    ......
            ......    ......
            '''
            self.x -= 1
        # ---------------------
        # Diagonal directions |
        # ---------------------
        elif ((other.y == self.y + 2) and (other.x == self.x + 1)) or ((other.x == self.x + 2) and (other.y == self.y + 1)) or ((other.x == self.x + 2) and (other.y == self.y + 2)):
            '''
            ......    ......
            ..O...    ..O...
            ...O.. -> ..SO.. (other is 2 units up and 1 unit right of self)
            .S....    ......                      or
            ......    ...... (other is 2 units right and 1 unit up of self)
            '''
            self.x += 1
            self.y += 1
        elif ((other.y == self.y + 2) and (other.x == self.x - 1)) or ((other.x == self.x - 2) and (other.y == self.y + 1)) or ((other.x == self.x - 2) and (other.y == self.y + 2)):
            '''
            ......    ......
            ..O...    ..O...
            .O.... -> .OS... (other is 2 units up and 1 unit left of self)
            ...S..    ......                      or
            ......    ...... (other is 2 units left and 1 unit up of self)
            '''
            self.x -= 1
            self.y += 1
        elif ((other.y == self.y - 2) and (other.x == self.x + 1)) or ((other.x == self.x + 2) and (other.y == self.y - 1)) or ((other.x == self.x + 2) and (other.y == self.y - 2)):
            '''
            ......    ......
            ..S...    ......
            ....O. -> ...SO. (other is 2 units down and 1 unit right of self)
            ...O..    ...O..                      or
            ......    ...... (other is 2 units right and 1 unit down of self)
            '''
            self.x += 1
            self.y -= 1
        elif ((other.y == self.y - 2) and (other.x == self.x - 1)) or ((other.x == self.x - 2) and (other.y == self.y - 1)) or ((other.x == self.x - 2) and (other.y == self.y - 2)):
            '''
            ......    ......
            ...S..    ......
            .O.... -> .OS... (other is 2 units down and 1 unit left of self)
            ..O...    ..O...                      or
            ......    ...... (other is 2 units left and 1 unit down of self)
            '''
            self.x -= 1
            self.y -= 1
        # ---------------------
        #  Already touching   |
        # ---------------------
        else:
            # Already touching
            return False

    def __repr__(self):
        return f'({self.x=}, {self.y=})'


def part_one():
    head = Knot()
    tail = Knot()
    visited_positions = set()

    # Always count starting position as "visited"
    visited_positions.add((tail.x, tail.y))

    for step in data:
        direction, amount = step.split()
        for _ in range(int(amount)):
            head.move(direction)
            tail.follow(head)
            visited_positions.add((tail.x, tail.y))

    print(len(visited_positions))


def part_two():
    knots = [Knot() for _ in range(10)]
    visited_positions = set()

    # Always count starting position as "visited"
    visited_positions.add((knots[9].x, knots[9].y))

    for step in data:
        direction, amount = step.split()
        for _ in range(int(amount)):
            knots[0].move(direction)
            for idx, _ in enumerate(knots[1:], start=1):
                knots[idx].follow(knots[idx - 1])
            # knots[9] is the Tail of the rope
            visited_positions.add((knots[9].x, knots[9].y))

    print(len(visited_positions))


part_one()
part_two()
