def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

class Dir:
    UP    = 0
    DOWN  = 1
    LEFT  = 2
    RIGHT = 3

def solve_part_1():
    layout = read_input_file_data().splitlines()
    HEIGHT = len(layout)
    WIDTH = len(layout[0])

    collected = []
    loc = (0, layout[0].index('|'), Dir.DOWN)
    while True:
        r, c, dir = loc
        sym = layout[r][c]
        # print(f"{r} {c}: {sym}")

        match dir:
            case Dir.UP:
                match sym:
                    case '-':
                        loc = (r-1, c, Dir.UP)
                    case '|':
                        loc = (r-1, c, Dir.UP)
                    case '+':
                        if c - 1 < 0 or layout[r][c-1] == ' ': # turn right
                            loc = (r, c+1, Dir.RIGHT)
                            continue
                        if c + 1 >= WIDTH or layout[r][c+1] == ' ': # turn left
                            loc = (r, c-1, Dir.LEFT)
                            continue
                        raise Exception(f"No turning at '+' at location ({r}, {c})")
                    case ' ':
                        break
                    case _:
                        collected.append(sym)
                        loc = (r-1, c, Dir.UP)
            case Dir.DOWN:
                match sym:
                    case '-':
                        loc = (r+1, c, Dir.DOWN)
                    case '|':
                        loc = (r+1, c, Dir.DOWN)
                    case '+':
                        if c - 1 < 0 or layout[r][c-1] == ' ': # turn right
                            loc = (r, c+1, Dir.RIGHT)
                            continue
                        if c + 1 >= WIDTH or layout[r][c+1] == ' ': # turn left
                            loc = (r, c-1, Dir.LEFT)
                            continue
                        raise Exception(f"No turning at '+' at location ({r}, {c})")
                    case ' ':
                        break
                    case _:
                        collected.append(sym)
                        loc = (r+1, c, Dir.DOWN)
            case Dir.LEFT:
                match sym:
                    case '-':
                        loc = (r, c-1, Dir.LEFT)
                    case '|':
                        loc = (r, c-1, Dir.LEFT)
                    case '+':
                        if r - 1 < 0 or layout[r-1][c] == ' ': # turn down
                            loc = (r+1, c, Dir.DOWN)
                            continue
                        if r + 1 >= HEIGHT or layout[r+1][c] == ' ': # turn up
                            loc = (r-1, c, Dir.UP)
                            continue
                        raise Exception(f"No turning at '+' at location ({r}, {c})")
                    case ' ':
                        break
                    case _:
                        collected.append(sym)
                        loc = (r, c-1, Dir.LEFT)
            case Dir.RIGHT:
                match sym:
                    case '-':
                        loc = (r, c+1, Dir.RIGHT)
                    case '|':
                        loc = (r, c+1, Dir.RIGHT)
                    case '+':
                        if r - 1 < 0 or layout[r-1][c] == ' ': # turn down
                            loc = (r+1, c, Dir.DOWN)
                            continue
                        if r + 1 >= HEIGHT or layout[r+1][c] == ' ': # turn up
                            loc = (r-1, c, Dir.UP)
                            continue
                        raise Exception(f"No turning at '+' at location ({r}, {c})")
                    case ' ':
                        break
                    case _:
                        collected.append(sym)
                        loc = (r, c+1, Dir.RIGHT)
            case _:
                raise Exception(f"Unknown direction {dir}")

    return ''.join(collected)

def solve_part_2():
    layout = read_input_file_data().splitlines()
    HEIGHT = len(layout)
    WIDTH = len(layout[0])

    loc = (0, layout[0].index('|'), Dir.DOWN)
    steps = 0
    while True:
        r, c, dir = loc
        sym = layout[r][c]
        # print(f"{r} {c}: {sym}")

        match dir:
            case Dir.UP:
                match sym:
                    case '-':
                        loc = (r-1, c, Dir.UP)
                    case '|':
                        loc = (r-1, c, Dir.UP)
                    case '+':
                        if c - 1 < 0 or layout[r][c-1] == ' ': # turn right
                            loc = (r, c+1, Dir.RIGHT)
                        elif c + 1 >= WIDTH or layout[r][c+1] == ' ': # turn left
                            loc = (r, c-1, Dir.LEFT)
                        else:
                            raise Exception(f"No turning at '+' at location ({r}, {c})")
                    case ' ':
                        break
                    case _:
                        loc = (r-1, c, Dir.UP)
            case Dir.DOWN:
                match sym:
                    case '-':
                        loc = (r+1, c, Dir.DOWN)
                    case '|':
                        loc = (r+1, c, Dir.DOWN)
                    case '+':
                        if c - 1 < 0 or layout[r][c-1] == ' ': # turn right
                            loc = (r, c+1, Dir.RIGHT)
                        elif c + 1 >= WIDTH or layout[r][c+1] == ' ': # turn left
                            loc = (r, c-1, Dir.LEFT)
                        else:
                            raise Exception(f"No turning at '+' at location ({r}, {c})")
                    case ' ':
                        break
                    case _:
                        loc = (r+1, c, Dir.DOWN)
            case Dir.LEFT:
                match sym:
                    case '-':
                        loc = (r, c-1, Dir.LEFT)
                    case '|':
                        loc = (r, c-1, Dir.LEFT)
                    case '+':
                        if r - 1 < 0 or layout[r-1][c] == ' ': # turn down
                            loc = (r+1, c, Dir.DOWN)
                        elif r + 1 >= HEIGHT or layout[r+1][c] == ' ': # turn up
                            loc = (r-1, c, Dir.UP)
                        else:
                            raise Exception(f"No turning at '+' at location ({r}, {c})")
                    case ' ':
                        break
                    case _:
                        loc = (r, c-1, Dir.LEFT)
            case Dir.RIGHT:
                match sym:
                    case '-':
                        loc = (r, c+1, Dir.RIGHT)
                    case '|':
                        loc = (r, c+1, Dir.RIGHT)
                    case '+':
                        if r - 1 < 0 or layout[r-1][c] == ' ': # turn down
                            loc = (r+1, c, Dir.DOWN)
                        elif r + 1 >= HEIGHT or layout[r+1][c] == ' ': # turn up
                            loc = (r-1, c, Dir.UP)
                        else:
                            raise Exception(f"No turning at '+' at location ({r}, {c})")
                    case ' ':
                        break
                    case _:
                        loc = (r, c+1, Dir.RIGHT)
            case _:
                raise Exception(f"Unknown direction {dir}")
        steps += 1

    return steps
    
print(solve_part_2())
