def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def get_instruction_list():
    return read_input_file_data().splitlines()

def is_jump_instruction(instruction: str) -> bool:
    return instruction.startswith("jmp") or instruction.startswith("jie") or instruction.startswith("jio")

def jump(index: int, instruction: str, a: int, b: int) -> int:
    if instruction.startswith("jmp"):
        words = instruction.split()
        offset = int(words[1])
        return index + offset
    elif instruction.startswith("jie"):
        words = instruction.split(",")
        register = a if words[0].split()[1] == "a" else b
        offset = int(words[1])
        if register % 2 == 0:
            return index + offset
        else:
            return index + 1
    elif instruction.startswith("jio"):
        words = instruction.split(",")
        register = a if words[0].split()[1] == "a" else b
        offset = int(words[1])
        if register == 1:
            return index + offset
        else:
            return index + 1
    else:
        raise Exception

def execute_instruction(ins: str, r: int):
    if ins == "hlf":
        return r // 2
    elif ins == "tpl":
        return r * 3
    elif ins == "inc":
        return r + 1
    else:
        raise Exception

def solve_part_1():
    instructions_list = get_instruction_list()
    a = 0
    b = 0
    index = 0
    while index < len(instructions_list):
        instruction = instructions_list[index]
        if is_jump_instruction(instruction):
            index = jump(index, instruction, a, b)
        else:
            words = instruction.split()
            ins = words[0]
            if words[1] == "a":
                a = execute_instruction(ins, a)
            elif words[1] == "b":
                b = execute_instruction(ins, b)
            else:
                raise Exception
            index += 1
    return b

def solve_part_2():
    instructions_list = get_instruction_list()
    a = 1
    b = 0
    index = 0
    while index < len(instructions_list):
        instruction = instructions_list[index]
        if is_jump_instruction(instruction):
            index = jump(index, instruction, a, b)
        else:
            words = instruction.split()
            ins = words[0]
            if words[1] == "a":
                a = execute_instruction(ins, a)
            elif words[1] == "b":
                b = execute_instruction(ins, b)
            else:
                raise Exception
            index += 1
    return b
    
print(solve_part_2())
