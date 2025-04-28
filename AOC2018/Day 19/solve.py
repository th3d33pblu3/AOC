import math

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def process_data():
    data = read_input_file_data()
    IP, instructions = data.split('\n', 1)
    IP = int(IP.split(' ')[1])
    instructions = [(line.split(' ')[0], *list(map(int, line.split(' ')[1:]))) for line in instructions.splitlines()]
    return IP, instructions

def solve_part_1():
    IP, instructions = process_data()
    reg = [0, 0, 0, 0, 0, 0]
    INS_LEN = len(instructions)

    while reg[IP] >= 0 and reg[IP] < INS_LEN:
        op, A, B, C = instructions[reg[IP]]
        if op == 'addr':
            reg[C] = reg[A] + reg[B]
        elif op == 'addi':
            reg[C] = reg[A] + B
        elif op == 'mulr':
            reg[C] = reg[A] * reg[B]
        elif op == 'muli':
            reg[C] = reg[A] * B
        elif op == 'banr':
            reg[C] = reg[A] & reg[B]
        elif op == 'bani':
            reg[C] = reg[A] & B
        elif op == 'borr':
            reg[C] = reg[A] | reg[B]
        elif op == 'bori':
            reg[C] = reg[A] | B
        elif op == 'setr':
            reg[C] = reg[A]
        elif op == 'seti':
            reg[C] = A
        elif op == 'gtir':
            reg[C] = 1 if A > reg[B] else 0
        elif op == 'gtri':
            reg[C] = 1 if reg[A] > B else 0
        elif op == 'gtrr':
            reg[C] = 1 if reg[A] > reg[B] else 0
        elif op == 'eqir':
            reg[C] = 1 if A == reg[B] else 0
        elif op == 'eqri':
            reg[C] = 1 if reg[A] == B else 0
        elif op == 'eqrr':
            reg[C] = 1 if reg[A] == reg[B] else 0

        reg[IP] += 1
    return reg[0]

# addi 4 16 4   # IP=0 start at (17): if [0]=0, set [2]=94, [3]=930 else set [2]=10550400, [3]=10551330, [0]=0; goto (1)
# seti 1 2 5    # IP=1 set [5]=1
# seti 1 1 1    # IP=2 set [1]=1
# mulr 5 1 2    # IP=3: if [5]*[1]=[3], then [0]+=[5]; goto(8)
# eqrr 2 3 2
# addr 2 4 4
# addi 4 1 4    
# addr 5 0 0
# addi 1 1 1    # IP=8 [1]+=1
# gtrr 1 3 2    # IP=9 if [1]>[3], goto (12) else goto (3)
# addr 4 2 4
# seti 2 4 4
# addi 5 1 5    # IP=12 [5]+=1
# gtrr 5 3 2    # IP=13 if [5]>[3], goto (EXIT) else goto (2)
# addr 2 4 4
# seti 1 8 4
# mulr 4 4 4
# addi 3 2 3    # IP=17 start here: set [2]=94, [3]=930, goto (25)
# mulr 3 3 3
# mulr 4 3 3
# muli 3 11 3
# addi 2 4 2
# mulr 2 4 2
# addi 2 6 2
# addr 3 2 3
# addr 4 0 4    # IP=25 if [0] is 1, goto (27) else goto (26): 
# seti 0 8 4    # IP=26 goto (1)
# setr 4 1 2    # IP=27: set [2]=10550400, [3]=10551330, [0]=0, goto (1)
# mulr 2 4 2
# addr 4 2 2
# mulr 4 2 2
# muli 2 14 2
# mulr 2 4 2
# addr 3 2 3
# seti 0 0 0
# seti 0 0 4

'''
[3] = 930 if [0]==0 else 10551330

for [5] in range(1, [3]+1):
    for [1] in range(1, [3]+1):
        if [5]*[1]==[3]:
            [0]+=[5]
return [0]

Basically get the sum of factors of [3]
'''

def solve_part_2():
    # N = 930 # part 1
    N = 10551330 # part 2
    sum_factors = 0
    for i in range(1, math.floor(math.sqrt(N)) + 1):
        if N % i == 0:
            sum_factors += i
            sum_factors += N // i
    return sum_factors

print(solve_part_2())
