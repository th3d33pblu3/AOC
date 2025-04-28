def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    layout = read_input_file_data().splitlines()
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    TURN_LEFT, GO_STRAIGHT, TURN_RIGHT = 0, 1, 2

    carts = []
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            cart = layout[i][j]
            if cart == '^':
                carts.append((i, j, UP, TURN_LEFT))
            elif cart == 'v':
                    carts.append((i, j, DOWN, TURN_LEFT))
            elif cart == '<':
                carts.append((i, j, LEFT, TURN_LEFT))
            elif cart == '>':
                carts.append((i, j, RIGHT, TURN_LEFT))
    
    def move_cart(cart):
        i, j, dir, turn = cart
        if dir == UP:
            ni, nj = i-1, j
            if layout[ni][nj] == '\\':
                return (ni, nj, LEFT, turn)
            elif layout[ni][nj] == '/':
                return (ni, nj, RIGHT, turn)
            elif layout[ni][nj] == '+':
                if turn == TURN_LEFT:
                    return (ni, nj, LEFT, GO_STRAIGHT)
                elif turn == GO_STRAIGHT:
                    return (ni, nj, UP, TURN_RIGHT)
                elif turn == TURN_RIGHT:
                    return (ni, nj, RIGHT, TURN_LEFT)
            else:
                return (ni, nj, UP, turn)
        elif dir == DOWN:
            ni, nj = i+1, j
            if layout[ni][nj] == '/':
                return (ni, nj, LEFT, turn)
            elif layout[ni][nj] == '\\':
                return (ni, nj, RIGHT, turn)
            elif layout[ni][nj] == '+':
                if turn == TURN_LEFT:
                    return (ni, nj, RIGHT, GO_STRAIGHT)
                elif turn == GO_STRAIGHT:
                    return (ni, nj, DOWN, TURN_RIGHT)
                elif turn == TURN_RIGHT:
                    return (ni, nj, LEFT, TURN_LEFT)
            else:
                return (ni, nj, DOWN, turn)
        elif dir == LEFT:
            ni, nj = i, j-1
            if layout[ni][nj] == '\\':
                return (ni, nj, UP, turn)
            elif layout[ni][nj] == '/':
                return (ni, nj, DOWN, turn)
            elif layout[ni][nj] == '+':
                if turn == TURN_LEFT:
                    return (ni, nj, DOWN, GO_STRAIGHT)
                elif turn == GO_STRAIGHT:
                    return (ni, nj, LEFT, TURN_RIGHT)
                elif turn == TURN_RIGHT:
                    return (ni, nj, UP, TURN_LEFT)
            else:
                return (ni, nj, LEFT, turn)
        elif dir == RIGHT:
            ni, nj = i, j+1
            if layout[ni][nj] == '/':
                return (ni, nj, UP, turn)
            elif layout[ni][nj] == '\\':
                return (ni, nj, DOWN, turn)
            elif layout[ni][nj] == '+':
                if turn == TURN_LEFT:
                    return (ni, nj, UP, GO_STRAIGHT)
                elif turn == GO_STRAIGHT:
                    return (ni, nj, RIGHT, TURN_RIGHT)
                elif turn == TURN_RIGHT:
                    return (ni, nj, DOWN, TURN_LEFT)
            else:
                return (ni, nj, RIGHT, turn)

    carts_pos = set(map(lambda c: c[:2], carts))
    while True:
        next_carts = []
        for cart in carts:
            new_cart = move_cart(cart)
            ni, nj, _, _ = new_cart
            if (ni, nj) in carts_pos: # Crash
                return f"{nj},{ni}"
            next_carts.append(new_cart)
            carts_pos.remove(cart[:2])
            carts_pos.add(new_cart[:2])
        carts = next_carts

def solve_part_2():
    layout = read_input_file_data().splitlines()
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    TURN_LEFT, GO_STRAIGHT, TURN_RIGHT = 0, 1, 2

    carts = []
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            cart = layout[i][j]
            if cart == '^':
                carts.append((i, j, UP, TURN_LEFT))
            elif cart == 'v':
                    carts.append((i, j, DOWN, TURN_LEFT))
            elif cart == '<':
                carts.append((i, j, LEFT, TURN_LEFT))
            elif cart == '>':
                carts.append((i, j, RIGHT, TURN_LEFT))
    
    def move_cart(cart):
        i, j, dir, turn = cart
        if dir == UP:
            ni, nj = i-1, j
            if layout[ni][nj] == '\\':
                return (ni, nj, LEFT, turn)
            elif layout[ni][nj] == '/':
                return (ni, nj, RIGHT, turn)
            elif layout[ni][nj] == '+':
                if turn == TURN_LEFT:
                    return (ni, nj, LEFT, GO_STRAIGHT)
                elif turn == GO_STRAIGHT:
                    return (ni, nj, UP, TURN_RIGHT)
                elif turn == TURN_RIGHT:
                    return (ni, nj, RIGHT, TURN_LEFT)
            else:
                return (ni, nj, UP, turn)
        elif dir == DOWN:
            ni, nj = i+1, j
            if layout[ni][nj] == '/':
                return (ni, nj, LEFT, turn)
            elif layout[ni][nj] == '\\':
                return (ni, nj, RIGHT, turn)
            elif layout[ni][nj] == '+':
                if turn == TURN_LEFT:
                    return (ni, nj, RIGHT, GO_STRAIGHT)
                elif turn == GO_STRAIGHT:
                    return (ni, nj, DOWN, TURN_RIGHT)
                elif turn == TURN_RIGHT:
                    return (ni, nj, LEFT, TURN_LEFT)
            else:
                return (ni, nj, DOWN, turn)
        elif dir == LEFT:
            ni, nj = i, j-1
            if layout[ni][nj] == '\\':
                return (ni, nj, UP, turn)
            elif layout[ni][nj] == '/':
                return (ni, nj, DOWN, turn)
            elif layout[ni][nj] == '+':
                if turn == TURN_LEFT:
                    return (ni, nj, DOWN, GO_STRAIGHT)
                elif turn == GO_STRAIGHT:
                    return (ni, nj, LEFT, TURN_RIGHT)
                elif turn == TURN_RIGHT:
                    return (ni, nj, UP, TURN_LEFT)
            else:
                return (ni, nj, LEFT, turn)
        elif dir == RIGHT:
            ni, nj = i, j+1
            if layout[ni][nj] == '/':
                return (ni, nj, UP, turn)
            elif layout[ni][nj] == '\\':
                return (ni, nj, DOWN, turn)
            elif layout[ni][nj] == '+':
                if turn == TURN_LEFT:
                    return (ni, nj, UP, GO_STRAIGHT)
                elif turn == GO_STRAIGHT:
                    return (ni, nj, RIGHT, TURN_RIGHT)
                elif turn == TURN_RIGHT:
                    return (ni, nj, DOWN, TURN_LEFT)
            else:
                return (ni, nj, RIGHT, turn)

    carts_pos = dict((c[:2], c[2:]) for c in carts)
    while len(carts_pos) > 1:
        i = 0
        while i < len(carts):
            cart = carts[i]
            new_cart = move_cart(cart)
            new_pos, new_dir = new_cart[:2], new_cart[2:]
            
            if new_pos in carts_pos:
                # Crash
                crashed_cart = (*new_pos, *carts_pos[new_pos])
                i2 = carts.index(crashed_cart)

                # Remove both carts
                carts_pos.__delitem__(cart[:2]) # Remove self
                carts_pos.__delitem__(new_pos) # Remove crashed cart
                if i < i2:
                    carts.pop(i2)
                    carts.pop(i)
                    i %= len(carts)
                else:
                    carts.pop(i)
                    carts.pop(i2)
                    i -= 1 # Account for shifting of i
                    i %= len(carts)
            else:
                # No crash
                carts[i] = new_cart
                carts_pos.__delitem__(cart[:2])
                carts_pos[new_pos] = new_dir
                i = (i + 1)
        carts.sort()
    y, x, _, _ = carts.pop()
    return f"{x},{y}"
'''
(53+133j) 118
(138+76j) 147
(63+0j) 220
(112+122j) 500
(107+121j) 1196

(17+1j)
(27+3j)
(97+41j)
(2+44j)
(31+91j)
(97+110j)
(107+138j)

(45+43j) 3145
(96+25j) 4434
(61+2j) 31341
'''
    
print(solve_part_2())
