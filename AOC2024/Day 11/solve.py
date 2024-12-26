from collections import deque

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    stones = read_input_file_data().split()

    def blink():
        nonlocal stones
        new_stones = deque()
        for stone in stones:
            if int(stone) == 0:
                new_stones.appendleft("1")
                new_stones.rotate(-1)
            elif len(stone) % 2 == 0:
                new_stones.appendleft(stone[0:len(stone)//2])
                new_stones.rotate(-1)
                new_stones.appendleft(str(int(stone[len(stone)//2:])))
                new_stones.rotate(-1)
            else:
                new_stones.appendleft(str(int(stone) * 2024))
                new_stones.rotate(-1)
        stones = list(new_stones)

    for _ in range(25):
        blink()
        
    return len(stones)

def solve_part_2():
    data = read_input_file_data().split()
    stones = {x: data.count(x) for x in data}

    def blink():
        nonlocal stones

        new_stones = {}
        for stone in stones:
            if int(stone) == 0:
                new_stones['1'] = new_stones.get('1', 0) + stones[stone]
            elif len(stone) % 2 == 0:
                left = stone[0:len(stone)//2]
                right = str(int(stone[len(stone)//2:]))
                new_stones[left] = new_stones.get(left, 0) + stones[stone]
                new_stones[right] = new_stones.get(right, 0) + stones[stone]
            else:
                new_stone = str(int(stone) * 2024)
                new_stones[new_stone] = new_stones.get(new_stone, 0) + stones[stone]
        
        stones = new_stones

    for _ in range(75):
        blink()
        
    return sum(stones.values())
    
print(solve_part_2())
