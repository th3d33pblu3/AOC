def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

ADDITION = 0
MULTIPLICATION = 1

def solve(expression):
    # print(f"{expression=}")
    LENGTH = len(expression)
    ptr = 0
    curr_value = 0
    curr_operation = ADDITION
    while ptr < LENGTH:
        char = expression[ptr]
        ptr += 1
        if char == '(':
            l_count = 1
            end_ptr = ptr
            while l_count > 0:
                char = expression[end_ptr]
                end_ptr += 1
                if char == '(':
                    l_count += 1
                elif char == ')':
                    l_count -= 1
            value = solve(expression[ptr: end_ptr-1])
            ptr = end_ptr
            if curr_operation == ADDITION:
                curr_value += value
            else:
                curr_value *= value
        elif char == '+':
            curr_operation = ADDITION
        elif char == '*':
            curr_operation = MULTIPLICATION
        elif char == ' ' or char == ')':
            # continue
            pass
        else:
            t = int(char)
            while ptr < LENGTH and expression[ptr] not in (' ', ')'):
                t *= 10
                t += int(expression[ptr])
                ptr += 1
            if curr_operation == ADDITION:
                curr_value += t
            else:
                curr_value *= t
    #     print(char, curr_value, curr_operation)
    # print(f"return value: {curr_value}")
    return curr_value

def solve_part_1():
    return sum(list(map(solve, read_input_file_data().splitlines())))

def advanced_solve(expression: str):
    # Solve parantheses
    LENGTH = len(expression)
    ptr = 0
    parantheses = []
    while ptr < LENGTH:
        char = expression[ptr]
        ptr += 1
        if char == '(':
            l_count = 1
            end_ptr = ptr
            while l_count > 0:
                char = expression[end_ptr]
                end_ptr += 1
                if char == '(':
                    l_count += 1
                elif char == ')':
                    l_count -= 1
            parantheses.append((ptr, end_ptr-1))
            ptr = end_ptr
    
    replace_vals = []
    for (ptr, end_ptr) in parantheses:
        expr = expression[ptr: end_ptr]
        val = advanced_solve(expr)
        replace_vals.append((ptr-1, end_ptr+1, val))
    
    replace_vals.reverse()
    for ptr, end_ptr, val in replace_vals:
        expression = expression[:ptr] + str(val) + expression[end_ptr:]

    # Solve addition
    expression = expression.split()
    values = list(map(int, expression[::2]))
    operations = expression[1::2]
    offset = 0
    for i, op in enumerate(operations):
        if op == '+':
            v1 = values.pop(i + offset)
            v2 = values.pop(i + offset)
            values.insert(i + offset, v1 + v2)
            offset -= 1
    # for i, op in enumerate(operations):
    #     if op == '+':
    #         v1 = values.pop(i)
    #         v2 = values.pop(i)
    #         values.insert(i, v1 + v2)
    #         operations.pop(i)
    
    # Solve multiplication
    result = values.pop(0)
    for val in values:
        result *= val
    return result

def solve_part_2():
    return sum(list(map(advanced_solve, read_input_file_data().splitlines())))
    
print(solve_part_2())
