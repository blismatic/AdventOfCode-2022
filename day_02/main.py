def parse_raw():
    with open('input.txt') as f:
        data = f.read().splitlines()

    return data


data = parse_raw()


def calculate_score(match, part):
    possible_matches = {
        'A X': [4, 3],
        'A Y': [8, 4],
        'A Z': [3, 8],
        'B X': [1, 1],
        'B Y': [5, 5],
        'B Z': [9, 9],
        'C X': [7, 2],
        'C Y': [2, 6],
        'C Z': [6, 7]
    }

    if part == 1:
        return possible_matches[match][0]
    if part == 2:
        return possible_matches[match][1]


def part_one():
    match_scores = [calculate_score(match, part=1) for match in data]
    print(sum(match_scores))


def part_two():
    match_scores = [calculate_score(match, part=2) for match in data]
    print(sum(match_scores))


part_one()
part_two()
