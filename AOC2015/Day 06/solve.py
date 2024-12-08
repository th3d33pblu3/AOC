def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()

    OFF = 0
    ON = 1
    TOGGLE = 2

    def parse_instruction(instruction):
        string = instruction.split()
        if string[0] == "toggle":
            x1, y1 = string[1].split(",")
            x2, y2 = string[3].split(",")
            return TOGGLE, int(x1), int(y1), int(x2), int(y2)
        elif string[1] == "off":
            x1, y1 = string[2].split(",")
            x2, y2 = string[4].split(",")
            return OFF, int(x1), int(y1), int(x2), int(y2)
        elif string[1] == "on":
            x1, y1 = string[2].split(",")
            x2, y2 = string[4].split(",")
            return ON, int(x1), int(y1), int(x2), int(y2)
        else:
            raise Exception("Unknown instruction")

    lights = []
    size = (1000, 1000)
    for _ in range(size[1]):
        lights.append([False] * size[0])

    for instruction in file.readlines():
        action, start_x, start_y, end_x, end_y = parse_instruction(instruction)
        if action == OFF:
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    lights[x][y] = False
        elif action == ON:
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    lights[x][y] = True
        elif action == TOGGLE:
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    lights[x][y] = not lights[x][y]
        else:
            raise Exception("Unknown action")

    count = 0
    for row in lights:
        for light in row:
            if light:
                count += 1
    
    return count

def solve_part_2():
    file = read_input_file()

    OFF = 0
    ON = 1
    TOGGLE = 2

    def parse_instruction(instruction):
        string = instruction.split()
        if string[0] == "toggle":
            x1, y1 = string[1].split(",")
            x2, y2 = string[3].split(",")
            return TOGGLE, int(x1), int(y1), int(x2), int(y2)
        elif string[1] == "off":
            x1, y1 = string[2].split(",")
            x2, y2 = string[4].split(",")
            return OFF, int(x1), int(y1), int(x2), int(y2)
        elif string[1] == "on":
            x1, y1 = string[2].split(",")
            x2, y2 = string[4].split(",")
            return ON, int(x1), int(y1), int(x2), int(y2)
        else:
            raise Exception("Unknown instruction")

    lights = []
    size = (1000, 1000)
    for _ in range(size[1]):
        lights.append([0] * size[0])

    for instruction in file.readlines():
        action, start_x, start_y, end_x, end_y = parse_instruction(instruction)
        if action == OFF:
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    lights[x][y] = max(0, lights[x][y] - 1)
        elif action == ON:
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    lights[x][y] += 1
        elif action == TOGGLE:
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    lights[x][y] += 2
        else:
            raise Exception("Unknown action")

    brightness = 0
    for row in lights:
        for light in row:
            brightness += light
    
    return brightness
    
print(solve_part_2())
