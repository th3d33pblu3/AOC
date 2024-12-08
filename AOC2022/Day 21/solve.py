def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

IS_VALUE = True
IS_JOB = False
ROOT_MONKEY = "root"
YOU = "humn"

def parse_monkeys():
    monkeys = {}
    for line in read_input_file_data().splitlines():
        monkey, job = line.split(": ")
        if job.isdigit():
            monkeys[monkey] = (IS_VALUE, int(job))
        else:
            left, op, right = job.split()
            monkeys[monkey] = (IS_JOB, (left, op, right))
    return monkeys

def solve_part_1():
    monkeys = parse_monkeys()
    def get_monkey_value(monkey):
        if monkeys[monkey][0] == IS_VALUE:
            return monkeys[monkey][1]
        else:
            left, op, right = monkeys[monkey][1]
            val_left = get_monkey_value(left)
            val_right = get_monkey_value(right)
            if op == "+":
                return val_left + val_right
            elif op == "-":
                return val_left - val_right
            elif op == "*":
                return val_left * val_right
            elif op == "/":
                return val_left // val_right
            else:
                raise Exception(f"Unknown operation {op}")    
    return get_monkey_value(ROOT_MONKEY)

def perform_op(val_left, op, val_right):
    if op == "+":
        return val_left + val_right
    elif op == "-":
        return val_left - val_right
    elif op == "*":
        return val_left * val_right
    elif op == "/":
        return val_left // val_right
    else:
        raise Exception(f"Unknown operation {op}")

def reverse_op(op):
    if op == "+":
        return "-"
    elif op == "-":
        return "+"
    elif op == "*":
        return "/"
    elif op == "/":
        return "*"
    else:
        raise Exception(f"Unknown operation {op}")

def solve_part_2():
    monkeys = parse_monkeys()
    monkeys[ROOT_MONKEY] = (IS_JOB, (monkeys[ROOT_MONKEY][1][0], "==", monkeys[ROOT_MONKEY][1][2]))
    monkeys[YOU] = (None, "x")
    def get_monkey_value(monkey):
        if monkey == YOU:
            return None, "x"
        if monkeys[monkey][0] == IS_VALUE:
            return monkeys[monkey][1], None
        left, op, right = monkeys[monkey][1]
        val_left, hold_ops_left = get_monkey_value(left)
        val_right, hold_ops_right = get_monkey_value(right)
        if op == "==":
            if val_left == None and val_right == None:
                raise Exception("Too many hold operations")
            if val_left != None and val_right != None:
                return val_left == val_right
            if val_left == None and val_right != None:
                x = hold_ops_left
                result = val_right
            elif val_left != None and val_right == None:
                x = hold_ops_right
                result = val_left
            else:
                raise Exception("Unexpected compare result.")

            delayed_ops = x.split()
            for i in range(len(delayed_ops) - 1, 0, -2):
                num = int(delayed_ops[i])
                x_side = delayed_ops[i - 1][0]
                delayed_op = delayed_ops[i - 1][1]
                if x_side == "L":
                    result = perform_op(result, delayed_op, num)
                else:
                    result = perform_op(num, delayed_op, result)
            return result
        else:
            if hold_ops_left == None and hold_ops_right == None: # Just values
                return perform_op(val_left, op, val_right), None
            elif hold_ops_left != None and hold_ops_right == None: # x on Left
                return None, hold_ops_left + f" L{reverse_op(op)} " + str(val_right)
            elif hold_ops_left == None and hold_ops_right != None: # x on Right
                if op == "+" or op == "*":
                    return None, hold_ops_right + f" L{reverse_op(op)} " + str(val_left)
                else:
                    return None, hold_ops_right + f" R{op} " + str(val_left)
            else:
                raise Exception("Too many hold operations")
    return get_monkey_value(ROOT_MONKEY)
    
print(solve_part_2())
