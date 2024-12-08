from collections import deque

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

PLAYERS = 439
LAST_MARBLE = 71307
SPECIAL_VALUE = 23
BACKTRACK = 7

def solve_part_1():
    # Note: appendleft and popleft from deque runs in O(1), while pop and append runs in O(n)
    player_scores = {}
    curr_player = 1
    curr_marble_value = 1

    marbles = deque([0])
    while curr_marble_value <= LAST_MARBLE:
        if curr_marble_value % SPECIAL_VALUE == 0:
            marbles.rotate(7)
            popped_marble_value = marbles.popleft()
            player_scores[curr_player] = player_scores.get(curr_player, 0) + curr_marble_value + popped_marble_value
        else:
            marbles.rotate(-2)
            marbles.appendleft(curr_marble_value)
        curr_marble_value += 1
        curr_player = (curr_player + 1) % PLAYERS
    
    return max(player_scores.values())

def solve_part_2():
    global LAST_MARBLE
    LAST_MARBLE *= 100
    return solve_part_1()
    
print(solve_part_2())
