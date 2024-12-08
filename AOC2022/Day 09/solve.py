def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    head = [0, 0]
    tail = [0, 0]
    visited = {}
    visited[(0, 0)] = True

    def move(direction):
        if direction == "L":
            head[0] -= 1
        elif direction == "R":
            head[0] += 1
        elif direction == "U":
            head[1] += 1
        elif direction == "D":
            head[1] -= 1
        else:
            raise Exception(f"Unknown direction: {direction}")

    def is_touching():
        if (abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1):
            return False
        return True

    def move_tail():
        if (head[0] == tail[0] or head[1] == tail[1]):
            tail[0] += (head[0] - tail[0]) / 2
            tail[1] += (head[1] - tail[1]) / 2
        else:
            tail[0] += (head[0] - tail[0]) / abs(head[0] - tail[0])
            tail[1] += (head[1] - tail[1]) / abs(head[1] - tail[1])

        visited[(tail[0], tail[1])] = True


    file = read_input_file()
    for line in file.read().splitlines():
        info = line.split()
        direction , dist = info[0], int(info[1])
        for _ in range(dist):
            move(direction)
            if (not is_touching()):
                move_tail()
    
    return len(visited)

def solve_part_2():
    knots = []
    for _ in range(10):
        knots.append([0, 0])
    visited = {}
    visited[(0, 0)] = True

    def move_head(direction):
        head = knots[0]
        if direction == "L":
            head[0] -= 1
        elif direction == "R":
            head[0] += 1
        elif direction == "U":
            head[1] += 1
        elif direction == "D":
            head[1] -= 1
        else:
            raise Exception(f"Unknown direction: {direction}")

    def is_touching(num1, num2):
        head = knots[num1]
        tail = knots[num2]
        if (abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1):
            return False
        return True

    def move_knot(num):
        head = knots[num - 1]
        tail = knots[num]
        if (head[0] == tail[0] or head[1] == tail[1]):
            tail[0] += (head[0] - tail[0]) / 2
            tail[1] += (head[1] - tail[1]) / 2
        else:
            tail[0] += (head[0] - tail[0]) / abs(head[0] - tail[0])
            tail[1] += (head[1] - tail[1]) / abs(head[1] - tail[1])

        if (num == 9):
            visited[(tail[0], tail[1])] = True


    file = read_input_file()
    for line in file.read().splitlines():
        info = line.split()
        direction , dist = info[0], int(info[1])
        for _ in range(dist):
            move_head(direction)
            for knot_num in range(1, 10):
                if (is_touching(knot_num - 1, knot_num)):
                    break
                move_knot(knot_num)
    
    return len(visited)
    
print(solve_part_2())
