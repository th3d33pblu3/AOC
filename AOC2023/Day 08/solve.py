import re
from math import lcm

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

L = 'L'
R= 'R'
LEFT = 0
RIGHT = 1
START = 'AAA'
END = 'ZZZ'

def solve_part_1():
    data = read_input_file_data().split('\n\n')
    instructions = data[0]
    length = len(instructions)
    nodes = {}
    for line in data[1].splitlines():
        input_node = re.findall(r'(\w{3})', line)
        nodes[input_node[0]] = (input_node[1], input_node[2])
    
    curr_node = START
    steps = 0
    while curr_node != END:
        i = instructions[steps % length]
        steps += 1
        if i == L:
            curr_node = nodes[curr_node][LEFT]
        else:
            curr_node = nodes[curr_node][RIGHT]

    return steps

def solve_part_2():
    data = read_input_file_data().split('\n\n')
    instructions = data[0]
    length = len(instructions)
    nodes = {}
    for line in data[1].splitlines():
        input_node = re.findall(r'(\w{3})', line)
        nodes[input_node[0]] = (input_node[1], input_node[2])

    curr_nodes = set(filter(lambda x: x[2] == 'A', nodes.keys()))
    loop_sizes = set()
    for node in curr_nodes:
        steps = 0
        while node[2] != 'Z':
            node = nodes[node][LEFT if instructions[steps % length] == L else RIGHT]
            steps += 1
        loop_sizes.add(steps)
    
    return lcm(*loop_sizes)
    
print(solve_part_2())
