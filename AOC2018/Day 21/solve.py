def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

# #ip 2
# seti 123 0 5       # IP=0: if 123 & 456 == 72, goto (5) else goto (1)
# bani 5 456 5
# eqri 5 72 5
# addr 5 2 2
# seti 0 0 2
# seti 0 4 5         # IP=5  set [5]=0
# bori 5 65536 4     # IP=6  set [4]=0b000000010000000000000000 | [5]
# seti 15466939 9 5  # IP=7  set [5]=0b111011000000000110111011
# bani 4 255 3       # IP=8: add last 8 bits of [4] to [5], then *=65899 and truncate to 24 bits
# addr 5 3 5
# bani 5 16777215 5
# muli 5 65899 5
# bani 5 16777215 5
# gtir 256 4 3       # IP=13: if [4] has less than 8 bits, goto (28) else goto (17)
# addr 3 2 2
# addi 2 1 2
# seti 27 8 2
# seti 0 7 3         # IP=17 set [3]=0
# addi 3 1 1         # IP=18 set [1]=[3]+1
# muli 1 256 1       # IP=19 [1]<<8
# gtrr 1 4 1         # IP=20: if [1]>[4] goto (26) else [3]+=1, goto (18) 
# addr 1 2 2
# addi 2 1 2
# seti 25 2 2
# addi 3 1 3
# seti 17 7 2
# setr 3 7 4         # IP=26 set [4]=[3]
# seti 7 3 2         # IP=27 goto (8)
# eqrr 5 0 3         # IP=28: if [5]==[0] goto (EXIT) else goto (6)
# addr 3 2 2
# seti 5 9 2

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
            # reg[C] = 1 if reg[A] == reg[B] else 0
            return reg[5]

        reg[IP] += 1
    return None

def solve_part_2():
    last_seen = None
    seen_nums = set()

    four = 65536
    five = 15466939
    while True:
        five += four & 255
        five *= 65899
        five &= 16777215
        if 256 > four: # IP=28
            if five in seen_nums:
                return last_seen
            else:
                last_seen = five
                seen_nums.add(five)
            four = five | 65536
            five = 15466939
        else:
            four >>= 8
    
print(solve_part_2())
