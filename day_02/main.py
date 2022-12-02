def parse_raw():
    with open('input.txt') as f:
        data = f.read().splitlines()
        data = [match.split(' ') for match in data]

    return data


data = parse_raw()


def calculate_score_part_1(opponent, you):
    shapes = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    outcomes = {
        'Loss': 0,
        'Draw': 3,
        'Win': 6

    }

    if ((opponent == 'A' and you == 'X') or (opponent == 'B' and you == 'Y') or (opponent == 'C' and you == 'Z')):
        # It was a tie
        return shapes[you] + outcomes['Draw']
    elif ((opponent == 'A' and you == 'Z') or (opponent == 'B' and you == 'X') or (opponent == 'C' and you == 'Y')):
        # You lost
        return shapes[you] + outcomes['Loss']
    elif ((opponent == 'A' and you == 'Y') or (opponent == 'B' and you == 'Z') or (opponent == 'C' and you == 'X')):
        # You won
        return shapes[you] + outcomes['Win']


def calculate_score_part_2(opponent, outcome):
    shapes = {
        'X': 1,
        'Y': 2,
        'Z': 3,
        'A': 1,
        'B': 2,
        'C': 3
    }

    if outcome == 'X':  # You need to lose
        if opponent == 'A':
            return shapes['Z']
        elif opponent == 'B':
            return shapes['X']
        elif opponent == 'C':
            return shapes['Y']
    elif outcome == 'Y':  # You need to draw
        return shapes[opponent] + 3
    elif outcome == 'Z':  # You need to win
        if opponent == 'A':
            return shapes['Y'] + 6
        elif opponent == 'B':
            return shapes['Z'] + 6
        elif opponent == 'C':
            return shapes['X'] + 6


def part_one():
    match_scores = [calculate_score_part_1(match[0], match[1]) for match in data]
    print(sum(match_scores))


def part_two():
    match_scores = [calculate_score_part_2(match[0], match[1]) for match in data]
    print(sum(match_scores))


part_one()
part_two()
