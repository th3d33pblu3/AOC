def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def print_max(): # 209
    data = read_input_file().read()
    id = 0
    for line in data.splitlines():
        words = line.split()
        if words[0] == "bot":
            id = max(id, int(words[1]))
    print(id)

def solve_part_1():
    NUM_BOTS = 210
    NUM_OUTPUTS = 21
    VALUE1 = 17
    VALUE2 = 61
    bots = [0] * (NUM_BOTS + NUM_OUTPUTS)
    for i in range(NUM_BOTS + NUM_OUTPUTS):
        bots[i] = []
    bot_instructions = [0] * NUM_BOTS
    data = read_input_file().read()
    for line in data.splitlines():
        words = line.split()
        if words[0] == "bot":
            bot_id = int(words[1])
            low_id = int(words[6])
            high_id = int(words[-1])
            if words[5] == "output":
                low_id += NUM_BOTS
            if words[-2] == "output":
                high_id += NUM_BOTS
            bot_instructions[bot_id] = (low_id, high_id)

    def throw_min_max(bot_id):
        while (len(bots[bot_id]) >= 2):
            val1 = bots[bot_id].pop(0)
            val2 = bots[bot_id].pop(0)
            low = min(val1, val2)
            high = max(val1, val2)
            if low == VALUE1 and high == VALUE2:
                return bot_id
            low_id, high_id = bot_instructions[bot_id]
            bots[low_id].append(low)
            bots[high_id].append(high)
            result = throw_min_max(low_id)
            if result != None:
                return result
            return throw_min_max(high_id)
        return None

    for line in data.splitlines():
        words = line.split()
        if words[0] == "value":
            value = int(words[1])
            bot_id = int(words[-1])
            bots[bot_id].append(value)
            result = throw_min_max(bot_id)
            if result != None:
                return result

def solve_part_2():
    NUM_BOTS = 210
    NUM_OUTPUTS = 21
    bots = [0] * (NUM_BOTS + NUM_OUTPUTS)
    for i in range(NUM_BOTS + NUM_OUTPUTS):
        bots[i] = []
    bot_instructions = [0] * NUM_BOTS
    data = read_input_file().read()
    for line in data.splitlines():
        words = line.split()
        if words[0] == "bot":
            bot_id = int(words[1])
            low_id = int(words[6])
            high_id = int(words[-1])
            if words[5] == "output":
                low_id += NUM_BOTS
            if words[-2] == "output":
                high_id += NUM_BOTS
            bot_instructions[bot_id] = (low_id, high_id)

    def throw_min_max(bot_id):
        while (len(bots[bot_id]) >= 2):
            val1 = bots[bot_id].pop(0)
            val2 = bots[bot_id].pop(0)
            low = min(val1, val2)
            high = max(val1, val2)
            low_id, high_id = bot_instructions[bot_id]
            bots[low_id].append(low)
            bots[high_id].append(high)
            throw_min_max(low_id)
            throw_min_max(high_id)

    for line in data.splitlines():
        words = line.split()
        if words[0] == "value":
            value = int(words[1])
            bot_id = int(words[-1])
            bots[bot_id].append(value)
            throw_min_max(bot_id)

    return bots[NUM_BOTS][0] * bots[NUM_BOTS + 1][0] * bots[NUM_BOTS + 2][0]
    
print(solve_part_2())
