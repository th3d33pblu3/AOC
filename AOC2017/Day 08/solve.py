def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def get_registers():
    file = read_input_file()
    registers_set = set()
    for line in file.read().splitlines():
        ins = line.split()
        name, inc_dec, val, _cond_if, cond_name, cond_cond, cond_value = ins
        registers_set.add(name)
    registers = {}
    for register in registers_set:
        registers[register] = 0
    return registers

def compare(left, right, opr_str):
    if opr_str == ">":
        return left > right
    elif opr_str == ">=":
        return left >= right
    elif opr_str == "<":
        return left < right
    elif opr_str == "<=":
        return left <= right
    elif opr_str == "==":
        return left == right
    elif opr_str == "!=":
        return left != right
    else:
        raise Exception(f"Unknown operator: {opr_str}")

def update(val, inc_dec, change_val):
    if inc_dec == "inc":
        return val + change_val
    elif inc_dec == "dec":
        return val - change_val
    else:
        raise Exception(f"Unknown update: {inc_dec}")

def solve_part_1():
    registers = get_registers()

    file = read_input_file()
    for line in file.read().splitlines():
        ins = line.split()
        name, inc_dec, val, _cond_if, cond_name, cond_cond, cond_val = ins
        cond_register_val = registers.get(cond_name)
        cond_val = int(cond_val)
        
        is_condition_met = compare(cond_register_val, cond_val, cond_cond)
        if is_condition_met:
            reg_val = registers[name]
            change_val = int(val)
            registers[name] = update(reg_val, inc_dec, change_val)
    
    return max(registers.values())

def solve_part_2():
    registers = get_registers()
    max_val = 0

    file = read_input_file()
    for line in file.read().splitlines():
        ins = line.split()
        name, inc_dec, val, _cond_if, cond_name, cond_cond, cond_val = ins
        cond_register_val = registers.get(cond_name)
        cond_val = int(cond_val)
        
        is_condition_met = compare(cond_register_val, cond_val, cond_cond)
        if is_condition_met:
            reg_val = registers[name]
            change_val = int(val)
            new_val = update(reg_val, inc_dec, change_val)

            if new_val > max_val:
                max_val = new_val

            registers[name] = new_val
    
    return max_val
    
print(solve_part_2())
