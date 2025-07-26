import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    instructions = read_input_file_data().splitlines()
    memory = {}
    and_value = None
    or_value = None
    for line in instructions: 
        if line.startswith('mem'):
            address = int(re.match(r'mem\[(\d+)\]', line).group(1))
            value = int(re.findall(r'= (\d+)', line)[0])
            value &= and_value
            value |= or_value
            memory[address] = value
        else:
            mask = line.removeprefix('mask = ')
            and_value = 0
            or_value = 0
            for bit in mask:
                and_value <<= 1
                or_value <<= 1
                if bit == '1':
                    or_value += 1
                elif bit == 'X':
                    and_value += 1
    return sum(memory.values())

def solve_part_2():
    instructions = read_input_file_data().splitlines()
    memory = {}
    mask = None
    for line in instructions: 
        if line.startswith('mem'):
            address = int(re.match(r'mem\[(\d+)\]', line).group(1))
            value = int(re.findall(r'= (\d+)', line)[0])

            possible_addresses = set()
            possible_addresses.add(0)
            bit_pos = 35
            for bit in mask:
                new_addresses = set()
                if bit == '0':
                    curr_addr_bit = (address >> bit_pos) % 2
                    for addr in possible_addresses:
                        new_addresses.add((addr << 1) + curr_addr_bit)
                elif bit == '1':
                    for addr in possible_addresses:
                        new_addresses.add((addr << 1) + 1)
                else:
                    for addr in possible_addresses:
                        new_addresses.add((addr << 1))
                        new_addresses.add((addr << 1) + 1)
                possible_addresses = new_addresses
                bit_pos -= 1
            for addr in possible_addresses:
                memory[addr] = value
        else:
            mask = line.removeprefix('mask = ')
    return sum(memory.values())
    
print(solve_part_2())
