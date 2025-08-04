def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    bits = read_input_file_data().splitlines()
    gamma_rate = ''
    for i in range(len(bits[0])):
        count_one = 0
        count_zero = 0
        for line in bits:
            if line[i] == '1':
                count_one += 1
            else:
                count_zero += 1
        if count_one > count_zero:
            gamma_rate += '1'
        else:
            gamma_rate += '0'
    
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int('1' * len(bits[0]), 2) - gamma_rate
    return gamma_rate * epsilon_rate

def solve_part_2():
    # Find oxygen generator rating
    bits = read_input_file_data().splitlines()
    for i in range(len(bits[0])):
        if len(bits) == 1:
            break
        count_one = 0
        count_zero = 0
        for line in bits:
            if line[i] == '1':
                count_one += 1
            else:
                count_zero += 1
        if count_one >= count_zero:
            more_common = '1'
        else:
            more_common = '0'
        bits = list(filter(lambda n: n[i] == more_common, bits))
    oxygen_generator_rating = int(bits[0], 2)
    
    # Find oxygen generator rating
    bits = read_input_file_data().splitlines()
    for i in range(len(bits[0])):
        if len(bits) == 1:
            break
        count_one = 0
        count_zero = 0
        for line in bits:
            if line[i] == '1':
                count_one += 1
            else:
                count_zero += 1
        if count_zero <= count_one:
            least_common = '0'
        else:
            least_common = '1'
        bits = list(filter(lambda n: n[i] == least_common, bits))
    co2_scrubber_rating = int(bits[0], 2)

    return oxygen_generator_rating * co2_scrubber_rating
    
print(solve_part_2())
