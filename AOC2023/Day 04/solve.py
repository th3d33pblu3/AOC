import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse(line: str):
    left, right = re.search(r': (.*)', line).group(1).split('|')
    winning_numbers = set(map(lambda x: int(x), left.split()))
    current_numbers = list(map(lambda x: int(x), right.split()))
    return winning_numbers, current_numbers

def solve_part_1():
    total_points = 0
    for line in read_input_file_data().splitlines():
        winning_numbers, current_numbers = parse(line)
        points = 0
        for num in current_numbers:
            if num in winning_numbers:
                if points == 0:
                    points += 1
                else:
                    points *= 2
        total_points += points
    return total_points

def solve_part_2():
    wins = []
    for line in read_input_file_data().splitlines():
        winning_numbers, current_numbers = parse(line)
        num_win = 0
        for num in current_numbers:
            if num in winning_numbers:
                num_win += 1
        wins.append(num_win)
    
    SIZE = len(wins)
    cards = [1] * SIZE
    for card_no, win in enumerate(wins):
        for i in range(1, win + 1):
            if card_no + i >= SIZE:
                break
            cards[card_no + i] += cards[card_no]
    return sum(cards)

print(solve_part_2())
