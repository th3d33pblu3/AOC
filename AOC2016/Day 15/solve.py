GATES = [(17, 5), (19, 8), (7, 1), (13, 7), (5, 1), (3, 0)]
NUM_GATES = len(GATES)

def can_pass_gate_n(gate_num, n):
    gate = GATES[gate_num - 1]
    return (n + gate_num + gate[1]) % gate[0] == 0

def solve_part_1():
    gate1 = GATES[0]
    time = gate1[0] - gate1[1] - 1
    loop_time = gate1[0]
    while True:
        for gate_num in range(1, NUM_GATES + 1):
            if not can_pass_gate_n(gate_num, time):
                time += loop_time
                break
        else:
            return time

def solve_part_2():
    global GATES, NUM_GATES
    GATES.append((11, 0))
    NUM_GATES = len(GATES)

    gate1 = GATES[0]
    time = gate1[0] - gate1[1] - 1
    loop_time = gate1[0]
    while True:
        for gate_num in range(1, NUM_GATES + 1):
            if not can_pass_gate_n(gate_num, time):
                time += loop_time
                break
        else:
            return time
    
print(solve_part_2())
