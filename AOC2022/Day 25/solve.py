def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

TWO = "2"
ONE = "1"
ZERO = "0"
MINUS_ONE = "-"
MINUS_TWO = "="

def val_to_char(val):
    if val == 2:
        return TWO
    elif val == 1:
        return ONE
    elif val == 0:
        return ZERO
    elif val == -1:
        return MINUS_ONE
    elif val == -2:
        return MINUS_TWO
    else:
        raise Exception(f"Unknown val: {val}")

def char_to_val(char):
    if char == TWO:
        return 2
    elif char == ONE:
        return 1
    elif char == ZERO:
        return 0
    elif char == MINUS_ONE:
        return -1
    elif char == MINUS_TWO:
        return -2
    else:
        raise Exception(f"Unknown char: {char}")

def snafu_to_dec(num):
    value = 0
    for char in num:
        value *= 5
        value += char_to_val(char)
    return value

def dec_to_snafu(dec):
    fake_snafu = ""
    while dec != 0:
        remainder = dec % 5
        dec = (dec - remainder) // 5
        fake_snafu = str(remainder) + fake_snafu

    true_snafu = ""
    carry = 0
    for char in fake_snafu[::-1]:
        value = int(char) + carry
        carry = value // 5
        value = value % 5
        if value > 2:
            value -= 5
            carry += 1
        true_char = val_to_char(value)
        true_snafu = true_char + true_snafu
    if carry != 0:
        true_snafu = val_to_char(carry) + true_snafu

    return true_snafu

def solve_part_1():
    total_sum = 0
    for line in read_input_file_data().splitlines():
        total_sum += snafu_to_dec(line)
    return dec_to_snafu(total_sum)

def solve_part_2():
    pass
    
print(solve_part_1())
