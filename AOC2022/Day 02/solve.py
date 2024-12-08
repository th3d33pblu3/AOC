def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LOSE = 0
    DRAW = 3
    WIN = 6

    def get_score(opp, you):
        """
        A: Rock
        B: Paper
        C: Scissors
        X: Rock
        Y: Paper
        Z: Scissors
        """
        if opp == "A":
            if you == "X":
                return DRAW + ROCK
            if you == "Y":
                return WIN + PAPER
            if you == "Z":
                return LOSE + SCISSORS
        elif opp == "B":
            if you == "X":
                return LOSE + ROCK
            if you == "Y":
                return DRAW + PAPER
            if you == "Z":
                return WIN + SCISSORS
        elif opp == "C":
            if you == "X":
                return WIN + ROCK
            if you == "Y":
                return LOSE + PAPER
            if you == "Z":
                return DRAW + SCISSORS
    
    total_score = 0
    for ln in file.readlines():
        total_score += get_score(ln[0], ln[2])
    
    return total_score

def solve_part_2():
    file = read_input_file()
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LOSE = 0
    DRAW = 3
    WIN = 6

    def get_score(opp, you):
        """
        A: Rock
        B: Paper
        C: Scissors
        X: Lose
        Y: Draw
        Z: Win
        """
        if opp == "A":
            if you == "X":
                return LOSE + SCISSORS
            if you == "Y":
                return DRAW + ROCK
            if you == "Z":
                return WIN + PAPER
        elif opp == "B":
            if you == "X":
                return LOSE + ROCK
            if you == "Y":
                return DRAW + PAPER
            if you == "Z":
                return WIN + SCISSORS
        elif opp == "C":
            if you == "X":
                return LOSE + PAPER
            if you == "Y":
                return DRAW + SCISSORS
            if you == "Z":
                return WIN + ROCK
    
    total_score = 0
    for ln in file.readlines():
        total_score += get_score(ln[0], ln[2])
    
    return total_score
            
print(solve_part_2())
