def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def transpose(puzzle: list[str]) -> list[str]:
    new_puzzle = []
    for c in range(len(puzzle[0])):
        temp = []
        for r in range(len(puzzle)):
            temp.append(puzzle[r][c])
        new_puzzle.append(''.join(temp))
    return new_puzzle

def horizontalReflection(puzzle: list[str]) -> int:
    row = None
    length = len(puzzle)
    for r in range(1, length):
        flag = True
        for d in range(0, min(r, length - r)):
            if puzzle[r-1 - d] != puzzle[r + d]:
                flag = False
                break
        if flag:
            row = r
            break
    return row

def solve_part_1():
    summary = 0
    for puzzle in read_input_file_data().split('\n\n'):
        puzzle = puzzle.splitlines()
        temp = horizontalReflection(puzzle)
        if temp != None:
            summary += temp * 100
        else:
            puzzle = transpose(puzzle)
            temp = horizontalReflection(puzzle)
            summary += temp
    return summary

def smudgeHorizontalReflection(puzzle: list[str]) -> int:
    length = len(puzzle)
    width = len(puzzle[0])
    count = [s.count("#") for s in puzzle]
    for r in range(1, length):
        d = min(r, length - r)
        if abs(sum(count[r-d : r]) - sum(count[r : r+d])) == 1:
            diff = 0
            c_diff = 0
            for x in range(d):
                if puzzle[r-1-x] != puzzle[r+x]:
                    p1 = puzzle[r-1-x]
                    p2 = puzzle[r+x]
                    diff += 1
                    for c in range(width):
                        if p1[c] != p2[c]:
                            c_diff += 1
            if diff == 1 and c_diff == 1:
                return r
    return None

def solve_part_2():
    summary = 0
    for puzzle in read_input_file_data().split('\n\n'):
        puzzle = puzzle.splitlines()
        temp = smudgeHorizontalReflection(puzzle)
        if temp != None:
            summary += temp * 100
        else:
            puzzle = transpose(puzzle)
            temp = smudgeHorizontalReflection(puzzle)
            summary += temp
    return summary
    
print(solve_part_2())
