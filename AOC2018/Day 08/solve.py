def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    ls = list(map(int, read_input_file_data().split()))
    pointer = 0
    def pick():
        nonlocal pointer, ls
        num = ls[pointer]
        pointer += 1
        return num
    
    arr_children = []
    arr_meta = []
    sum_meta = 0

    def read_children():
        nonlocal arr_children, arr_meta, sum_meta
        arr_children.append(pick())
        arr_meta.append(pick())
        while arr_children[-1] != 0:
            read_children()
            arr_children[-1] -= 1
        arr_children.pop(-1)
        num_meta = arr_meta.pop(-1)
        for _ in range(num_meta):
            sum_meta += pick()
    
    read_children()
    return sum_meta

def solve_part_2():
    ls = list(map(int, read_input_file_data().split()))
    pointer = 0
    def pick():
        nonlocal pointer, ls
        num = ls[pointer]
        pointer += 1
        return num
    
    def read_children():
        num_children = pick()
        num_meta = pick()

        if num_children == 0: # No children, value = sum meta
            sum_meta = 0
            for _ in range(num_meta):
                sum_meta += pick()
            return sum_meta
        else: # Have children, value = sum of child values by meta index
            child_values = []
            while num_children != 0:
                child_values.append(read_children())
                num_children -= 1
            num_children = len(child_values)
            t_value = 0
            for _ in range(num_meta):
                meta = pick()
                if meta == 0 or meta > num_children:
                    continue
                t_value += child_values[meta - 1]
            return t_value
    
    return read_children()
    
print(solve_part_2())
