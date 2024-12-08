def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

data = read_input_file_data().splitlines()
HEIGHT = len(data)
WIDTH = len(data[0])

def is_symbol(c: str):
    return not (c.isdigit() or c == '.')

def check(i: int, j: int):
    if i < 0 or j < 0 or i >= HEIGHT or j >= WIDTH:
        return False
    return is_symbol(data[i][j])

def solve_part_1():
    total = 0
    for i, line in enumerate(data):
        temp = ''
        should_add = False
        j = 0
        while j < WIDTH:
            char = line[j]
            if char.isdigit():
                if temp == '':
                    should_add |= check(i - 1, j - 1) or check(i, j - 1) or check(i + 1, j - 1)
                temp += char
                if not should_add:
                    should_add |= check(i - 1, j) or check(i + 1, j)
            elif temp != '':
                should_add |= check(i - 1, j) or check(i, j) or check(i + 1, j)
                if should_add:
                    total += int(temp)
                temp = ''
                should_add = False
            j += 1
        if temp != '':
            if should_add:
                total += int(temp)
            temp = ''
            should_add = False
    return total

def find_adjacent_nums(i: int, j: int) -> list[int]:
    nums = []
    # Top
    if i > 0 and data[i - 1][j].isdigit(): # Only 1 number right on top
        temp_j = j
        while temp_j > 0 and data[i - 1][temp_j - 1].isdigit():
            temp_j -= 1
        temp = ''
        while temp_j < WIDTH and data[i - 1][temp_j].isdigit():
            temp += data[i - 1][temp_j]
            temp_j += 1
        nums.append(int(temp))
    else:
        if i > 0 and j > 0 and data[i - 1][j - 1].isdigit(): # Top left has number
            temp_j = j - 1
            temp = ''
            while temp_j >= 0 and data[i - 1][temp_j].isdigit():
                temp = data[i - 1][temp_j] + temp
                temp_j -= 1
            nums.append(int(temp))
        if i > 0 and j < WIDTH - 1 and data[i - 1][j + 1].isdigit(): # Top right has number
            temp_j = j + 1
            temp = ''
            while temp_j < WIDTH and data[i - 1][temp_j].isdigit():
                temp += data[i - 1][temp_j]
                temp_j += 1
            nums.append(int(temp))
    
    # Curr row
    if j > 0 and data[i][j - 1].isdigit(): # Left has number
        temp_j = j - 1
        temp = ''
        while temp_j >= 0 and data[i][temp_j].isdigit():
            temp = data[i][temp_j] + temp
            temp_j -= 1
        nums.append(int(temp))
    if j < WIDTH - 1 and data[i][j + 1].isdigit(): # Right has number
        temp_j = j + 1
        temp = ''
        while temp_j < WIDTH and data[i][temp_j].isdigit():
            temp += data[i][temp_j]
            temp_j += 1
        nums.append(int(temp))

    # Bottom
    if i < HEIGHT - 1 and data[i + 1][j].isdigit(): # Only 1 number right below
        temp_j = j
        while temp_j >= 0 and data[i + 1][temp_j - 1].isdigit():
            temp_j -= 1
        temp = ''
        while temp_j < WIDTH and data[i + 1][temp_j].isdigit():
            temp += data[i + 1][temp_j]
            temp_j += 1
        nums.append(int(temp))
    else:
        if i < HEIGHT - 1 and j > 0 and data[i + 1][j - 1].isdigit(): # Bottom left has number
            temp_j = j - 1
            temp = ''
            while temp_j >= 0 and data[i + 1][temp_j].isdigit():
                temp = data[i + 1][temp_j] + temp
                temp_j -= 1
            nums.append(int(temp))
        if i < HEIGHT - 1 and j < WIDTH - 1 and data[i + 1][j + 1].isdigit(): # Bottom right has number
            temp_j = j + 1
            temp = ''
            while temp_j < WIDTH and data[i + 1][temp_j].isdigit():
                temp += data[i + 1][temp_j]
                temp_j += 1
            nums.append(int(temp))
    
    return nums

def solve_part_2():
    gear_coordinates = []
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if data[i][j] == '*':
                gear_coordinates.append((i, j))

    total = 0
    for gear in gear_coordinates:
        i, j = gear
        nums = find_adjacent_nums(i, j)
        if len(nums) == 2:
            total += nums[0] * nums[1]
    return total
    
print(solve_part_2())
