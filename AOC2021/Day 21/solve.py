from collections import defaultdict

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    p1, p2 = [int(line.split(': ')[1]) for line in read_input_file_data().splitlines()]
    p1_score, p2_score = 0, 0
    scores = {i: i for i in range(10)}
    scores[0] = 10
    
    d = 1
    rolls = 0
    def roll():
        nonlocal d, rolls
        rolls += 1
        v = d
        d += 1
        if d > 100:
            d -= 100
        return v
    
    while p1_score < 1000 or p2_score < 1000:
        # Player 1's turn
        for _ in range(3):
            p1 += roll()
        p1 %= 10
        p1_score += scores[p1]
        if p1_score >= 1000:
            return rolls * p2_score
        
        # Player 2's turn
        for _ in range(3):
            p2 += roll()
        p2 %= 10
        p2_score += scores[p2]
        if p2_score >= 1000:
            return rolls * p1_score

def solve_part_2():
    p1, p2 = [int(line.split(': ')[1]) for line in read_input_file_data().splitlines()]
    splits = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1
    }
    p1_win, p2_win = 0, 0
    universes = { (p1 % 10, 0, p2 % 10, 0): 1 }
    is_p1_turn = True
    while universes:
        new_universes = defaultdict(int)
        if is_p1_turn:
            for (p1_pos, p1_score, p2_pos, p2_score), u_count in universes.items():
                for steps, s_count in splits.items():
                    new_pos = (p1_pos + steps) % 10
                    new_score = p1_score + (10 if new_pos == 0 else new_pos)
                    new_count = u_count * s_count
                    if new_score >= 21:
                        p1_win += new_count
                    else:
                        new_universes[(new_pos, new_score, p2_pos, p2_score)] += new_count
        else:
            for (p1_pos, p1_score, p2_pos, p2_score), u_count in universes.items():
                for steps, s_count in splits.items():
                    new_pos = (p2_pos + steps) % 10
                    new_score = p2_score + (10 if new_pos == 0 else new_pos)
                    new_count = u_count * s_count
                    if new_score >= 21:
                        p2_win += new_count
                    else:
                        new_universes[(p1_pos, p1_score, new_pos, new_score)] += new_count

        universes = new_universes
        is_p1_turn = not is_p1_turn
    return max(p1_win, p2_win)
    
print(solve_part_2())
