from string import ascii_lowercase

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def get_next_pass(password):
    FORBIDDEN_INDICES = {ascii_lowercase.index('i'), ascii_lowercase.index('o'), ascii_lowercase.index('l')}

    def increment_password(password):
        index = -1
        password = list(map(lambda x: ascii_lowercase.index(x), list(password)))
        password[index] += 1
        while password[index] > 25:
            password[index] = 0
            index -= 1
            password[index] += 1

        for index in range(len(password)):
            if password[index] in FORBIDDEN_INDICES:
                password[index] += 1 # always < 25

        password = list(map(lambda i: ascii_lowercase[i], password))
        password = "".join(password)
        return password

    def is_valid_password(password: str):
        if any(x in password for x in {'i', 'o', 'l'}):
            return False
        
        password_copy = password
        count = 0
        for x in ascii_lowercase:
            pair = x + x
            if pair in password_copy:
                count += 1
                password_copy = password_copy.replace(pair, "_", 1)
                if pair in password_copy:
                    count += 1
                if count >= 2:
                    break
        if count < 2:
            return False

        password_copy = list(map(lambda x: ascii_lowercase.index(x), list(password)))
        index = 2
        while index < len(password_copy):
            val = password_copy[index]
            if (password_copy[index - 2] == val - 2 and password_copy[index - 1] == val - 1):
                return True
            index += 1

        return False

    password = increment_password(password)
    while (not is_valid_password(password)):
        password = increment_password(password)

    return password

def solve_part_1():
    password = read_input_file_data()
    return get_next_pass(password)

def solve_part_2():
    first_pass = read_input_file_data()
    second_pass = get_next_pass(first_pass)
    third_pass = get_next_pass(second_pass)
    return third_pass
    
print(solve_part_2())
