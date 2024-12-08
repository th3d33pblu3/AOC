def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    range_values = tuple(map(int, read_input_file_data().split('-')))
    value = range_values[0]
    LIMIT = range_values[1] + 1

    def isNonDecreasing(i: int) -> bool:
        last = i % 10
        i //= 10
        while i != 0:
            sec_last = i % 10
            i //= 10
            if sec_last > last:
                return False
            last = sec_last
        return True
    
    def isContainDouble(i: int) -> bool:
        last = i % 10
        i //= 10
        flag = False
        while i != 0:
            sec_last = i % 10
            i //= 10
            if sec_last == last:
                flag = True
                break
            last = sec_last
        return flag

    def makeNonDecreasing(i: int) -> int:
        arr = []
        while i != 0:
            arr.insert(0, i % 10)
            i //= 10
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                for j in range(i + 1, len(arr)):
                    arr[j] = arr[i]
                break
        return int(''.join(map(str, arr)))

    def makeNonDecreasingLastDouble(i: int) -> int:
        end = i % 100
        for n in range(1, 10):
            if n * 11 > end:
                i += n * 11 - end
                break
        return i

    num_valid = 0
    while value < LIMIT:
        if not isNonDecreasing(value):
            value = makeNonDecreasing(value)
        if not isContainDouble(value):
            value = makeNonDecreasingLastDouble(value)
        if value < LIMIT:
            num_valid += 1
            value += 1
    
    return num_valid

def solve_part_2():
    range_values = tuple(map(int, read_input_file_data().split('-')))
    value = range_values[0]
    LIMIT = range_values[1] + 1

    def isNonDecreasing(i: int) -> bool:
        last = i % 10
        i //= 10
        while i != 0:
            sec_last = i % 10
            i //= 10
            if sec_last > last:
                return False
            last = sec_last
        return True
    
    def isContainGroupDouble(i: int) -> bool:
        arr = []
        while i != 0:
            arr.insert(0, i % 10)
            i //= 10
        flag = False
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                if i > 0 and arr[i - 1] == arr[i]:
                    continue
                if i + 1 < (len(arr) - 1) and arr[i + 2] == arr[i + 1]:
                    continue
                flag = True
                break
        return flag

    def makeNonDecreasing(i: int) -> int:
        arr = []
        while i != 0:
            arr.insert(0, i % 10)
            i //= 10
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                for j in range(i + 1, len(arr)):
                    arr[j] = arr[i]
                break
        return int(''.join(map(str, arr)))

    num_valid = 0
    while value < LIMIT:
        if not isNonDecreasing(value):
            value = makeNonDecreasing(value)
        while not isContainGroupDouble(value):
            value += 1
            value = makeNonDecreasing(value)
        
        if value < LIMIT:
            num_valid += 1
            value += 1
    
    return num_valid
    
print(solve_part_2())
