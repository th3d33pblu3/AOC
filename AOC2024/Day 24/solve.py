def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    input_data, connection_data = read_input_file_data().split('\n\n')
    partners = {}
    gates = {}
    for line in connection_data.splitlines():
        wire_and_logic, output = line.split(' -> ')
        w1, logic, w2 = wire_and_logic.split()

        if (w1, w2) not in gates: # repeatable
            gates[(w1, w2)] = set()
        gates[(w1, w2)].add((logic, output)) # Non-symmetric
        if w1 not in partners:
            partners[w1] = set()
        if w2 not in partners:
            partners[w2] = set()
        partners[w1].add(w2)
        partners[w2].add(w1)

    gates_to_operate = set()
    inputs = {}
    for line in input_data.splitlines():
        wire, val = line.split(': ')
        inputs[wire] = int(val) # No repeat and does not previously exist, also no input queueing or else will have race condition problem
        for partner in partners[wire]:
            if partner in inputs:
                gates_to_operate.add((wire, partner))
                gates_to_operate.add((partner, wire))

    while len(gates_to_operate) != 0:
        new_gates_to_operate = set()
        for wire, partner in gates_to_operate:
            if (wire, partner) not in gates:
                continue
            for logic, output in gates[(wire, partner)]:
                v1, v2 = inputs[wire], inputs[partner]
                if logic == 'XOR':
                    inputs[output] = v1 ^ v2
                elif logic == 'AND':
                    inputs[output] = v1 & v2
                elif logic == 'OR':
                    inputs[output] = v1 | v2
                if output not in partners:
                    continue
                for out_partner in partners[output]:
                    if out_partner in inputs:
                        new_gates_to_operate.add((output, out_partner))
                        new_gates_to_operate.add((out_partner, output))
        gates_to_operate = new_gates_to_operate
    
    z_wires = list(filter(lambda wire: wire[0] == 'z', inputs.keys()))
    z_wires.sort(reverse=True)
    binary = int(''.join(list(map(lambda wire: str(inputs[wire]), z_wires))), base=2)
    return binary

# def solve_part_2():
#     _, connection_data = read_input_file_data().split('\n\n')
#     partners = {}
#     gates = {}

#     X_MAX = Y_MAX = Z_MAX = 0
#     output_sources = {}

#     for line in connection_data.splitlines():
#         wire_and_logic, output = line.split(' -> ')
#         w1, logic, w2 = wire_and_logic.split()

#         if (w1, w2) not in gates: # repeatable
#             gates[(w1, w2)] = set()
#         gates[(w1, w2)].add((logic, output)) # Non-symmetric
#         if w1 not in partners:
#             partners[w1] = set()
#         if w2 not in partners:
#             partners[w2] = set()
#         partners[w1].add(w2)
#         partners[w2].add(w1)

#         if w1[0] == 'x' and int(w1[1:]) > X_MAX:
#             X_MAX = int(w1[1:])
#         elif w1[0] == 'y' and int(w1[1:]) > Y_MAX:
#             Y_MAX = int(w1[1:])
#         if w2[0] == 'x' and int(w2[1:]) > X_MAX:
#             X_MAX = int(w2[1:])
#         elif w2[0] == 'y' and int(w2[1:]) > Y_MAX:
#             Y_MAX = int(w2[1:])
#         if output[0] == 'z' and int(output[1:]) > Z_MAX:
#             Z_MAX = int(output[1:])
#         if output not in output_sources:
#             output_sources[output] = set()
#         output_sources[output].add(w1)
#         output_sources[output].add(w2)

#     assert X_MAX == Y_MAX and Z_MAX == X_MAX + 1



#     def num_to_wires(num, prefix, max_count):
#         wires = {}
#         for i in range(max_count + 1):
#             if num == 0:
#                 break
#             wires[prefix + ('0' if i < 10 else '') + str(i)] = num % 2
#             num >>= 1
#         return wires
    
#     def trace_wire_path(wire) -> set:
#         involved_wires = set()
#         frontier = set()
#         frontier.add(wire)
#         while len(frontier) != 0:
#             involved_wires.update(frontier)
#             new_frontier = set()
#             for output in frontier:
#                 if output not in output_sources:
#                     continue
#                 new_frontier.update(output_sources[output])
#             frontier = new_frontier
#         return involved_wires

#     def find_involved_wrong_wires(x, y):
#         gates_to_operate = set()
#         inputs = {}
#         x_wires = num_to_wires(x, 'x', X_MAX)
#         y_wires = num_to_wires(y, 'y', Y_MAX)
#         for wire, val in x_wires.items():
#             inputs[wire] = val
#             for partner in partners[wire]:
#                 if partner in inputs:
#                     gates_to_operate.add((wire, partner))
#                     gates_to_operate.add((partner, wire))
#         for wire, val in y_wires.items():
#             inputs[wire] = val
#             for partner in partners[wire]:
#                 if partner in inputs:
#                     gates_to_operate.add((wire, partner))
#                     gates_to_operate.add((partner, wire))

#         while len(gates_to_operate) != 0:
#             new_gates_to_operate = set()
#             for wire, partner in gates_to_operate:
#                 if (wire, partner) not in gates:
#                     continue
#                 for logic, output in gates[(wire, partner)]:
#                     v1, v2 = inputs[wire], inputs[partner]
#                     if logic == 'XOR':
#                         inputs[output] = v1 ^ v2
#                     elif logic == 'AND':
#                         inputs[output] = v1 & v2
#                     elif logic == 'OR':
#                         inputs[output] = v1 | v2
#                     if output not in partners:
#                         continue
#                     for out_partner in partners[output]:
#                         if out_partner in inputs:
#                             new_gates_to_operate.add((output, out_partner))
#                             new_gates_to_operate.add((out_partner, output))
#             gates_to_operate = new_gates_to_operate
        
#         z = x + y
#         expected_z_wires = num_to_wires(z, 'z', Z_MAX)
#         involved_wrong_wires = set()
#         for wire, val in expected_z_wires.items():
#             if wire not in inputs or inputs[wire] != val:
#                 involved_wrong_wires.update(trace_wire_path(wire))
#         return involved_wrong_wires
    
#     zeros = 2 ** X_MAX
#     ones = 2 ** (X_MAX + 1) - 1
#     wrong_wires = []
#     wrong_wires.append(find_involved_wrong_wires(zeros, zeros))
#     wrong_wires.append(find_involved_wrong_wires(ones, zeros))
#     wrong_wires.append(find_involved_wrong_wires(zeros, ones))
#     wrong_wires.append(find_involved_wrong_wires(ones, ones))
#     intersection = set()
#     for i in range(4):
#         if len(wrong_wires[i]) == 0:
#             continue
#         intersection.update(wrong_wires[i])
#     # while len(intersection) > 8:
#     sources = set()
#     for output in intersection:
#         if output not in output_sources:
#             continue
#         sources.update(output_sources[output])
#     intersection.difference_update(sources)
#     print(intersection)
    
#     assert len(intersection) == 8
#     wrong_outputs = list(intersection)
#     wrong_outputs.sort()
#     return ''.join(wrong_outputs)

def solve_part_2():
    ''' Base case
    CO_01    z_00
    (AND)  (XOR)
     |\\   //|
     | \\ // |
     |   X   |
     | // \\ |
     |//   \\|
    x_00    y_00
    '''
    ''' General case
    CO_n+1 (Z_last for last case)
    (OR)
     |\\
     |  \\
     |    \\
     |      c_n     z_n
     |     (AND)   (XOR)
     |      |\\   //|
     |      | \\ // |
     |      |   X   |
     |      | // \\ |
     |      |//   \\|
     a_n    b_n    CO_n
    (AND)  (XOR)
     |\\   //|
     | \\ // |
     |   X   |
     | // \\ |
     |//   \\|
    x_n    y_n
    '''
    inputs, connection_data = read_input_file_data().split('\n\n')
    Z_MAX = len(inputs.splitlines()) // 2
    connections = {}
    partners = {}
    reverse_connections = {}
    for line in connection_data.splitlines():
        w1, logic, w2, _, output = line.split()
        connections[(w1, logic, w2)] = output
        connections[(w2, logic, w1)] = output
        if w1 not in partners:
            partners[w1] = set()
        partners[w1].add((w2, logic))
        if w2 not in partners:
            partners[w2] = set()
        partners[w2].add((w1, logic))
        reverse_connections[(output, logic)] = (w1, w2)

    def perform_logic(wire_val, logic, partner_val):
        if logic == 'OR':
            return wire_val | partner_val
        elif logic == 'AND':
            return wire_val & partner_val
        elif logic == 'XOR':
            return wire_val ^ partner_val
        else:
            raise Exception(f"Unknown logic {logic}")

    def swap_connections(conn1, conn2):
        nonlocal connections, reverse_connections
        w1, l1, p1, o1 = conn1
        w2, l2, p2, o2 = conn2

        assert connections[(w1, l1, p1)] == o1 and connections[(w2, l2, p2)] == o2 and set(reverse_connections[(o1, l1)]) == set((w1, p1)) and set(reverse_connections[(o2, l2)]) == set((w2, p2))
        connections[(w1, l1, p1)] = o2
        connections[(p1, l1, w1)] = o2
        connections[(w2, l2, p2)] = o1
        connections[(p2, l2, w2)] = o1
        reverse_connections[(o1, l1)] = (w2, p2)
        reverse_connections[(o2, l2)] = (w1, p1)
    
    def binary_add(x, y):
        wire_values = {}
        pending_calculations = set()
        for i in range(Z_MAX):
            i_str = str(i).zfill(2)
            wire_values['x' + i_str] = x & 1
            wire_values['y' + i_str] = y & 1
            x >>= 1
            y >>= 1
            pending_calculations.add(('x' + i_str, 'AND', 'y' + i_str))
            pending_calculations.add(('x' + i_str, 'XOR', 'y' + i_str))

        while len(pending_calculations) != 0:
            new_pending_calculations = set()
            for wire, logic, partner in pending_calculations:
                output = connections[(wire, logic, partner)]
                wire_values[output] = perform_logic(wire_values.get(wire, 0), logic, wire_values.get(partner, 0))
                if output not in partners:
                    continue
                for output_partner, output_logic in partners[output]:
                    if output_partner in wire_values:
                        new_pending_calculations.add((output, output_logic, output_partner))
            pending_calculations = new_pending_calculations

        actual_z = int(''.join([str(wire_values['z' + str(i).zfill(2)]) for i in range(Z_MAX, -1, -1)]), 2)
        return actual_z
    
    def debug(z):
        output = []
        for i in range(Z_MAX):
            if z == 0:
                break
            output.append(f"z{str(i).zfill(2)}: {z & 1}")
            z >>= 1
        return output

    wrong_wires = []
    '''
    Wrong addition when i=5
    Expected: 62 Actual: 94
    Expect: ['z00: 0', 'z01: 1', 'z02: 1', 'z03: 1', 'z04: 1', 'z05: 1']
    Actual: ['z00: 0', 'z01: 1', 'z02: 1', 'z03: 1', 'z04: 1', 'z05: 0', 'z06: 1']

    z05(x)
    (OR)
     |\\
     |  \\
     |    \\
     |      bhb     jst(x)
     |     (AND)   (XOR)
     |      |\\   //|
     |      | \\ // |
     |      |   X   |
     |      | // \\ |
     |      |//   \\|
     sgt    tvp    ggh
    (AND)  (XOR)
     |\\   //|
     | \\ // |
     |   X   |
     | // \\ |
     |//   \\|
    x05    y05
    '''
    swap_connections(('tvp', 'XOR', 'ggh', 'jst'), ('sgt', 'OR', 'bhb', 'z05'))
    wrong_wires.append('jst')
    wrong_wires.append('z05')
    '''
    Wrong addition when i=11
    Expected: 4094 Actual: 3070
    Expect: ['z00: 0', 'z01: 1', 'z02: 1', 'z03: 1', 'z04: 1', 'z05: 1', 'z06: 1', 'z07: 1', 'z08: 1', 'z09: 1', 'z10: 1', 'z11: 1']
    Actual: ['z00: 0', 'z01: 1', 'z02: 1', 'z03: 1', 'z04: 1', 'z05: 1', 'z06: 1', 'z07: 1', 'z08: 1', 'z09: 1', 'z10: 0', 'z11: 1']

    gvj
    (OR)
     |\\
     |  \\
     |    \\
     |      pqq     z10
     |     (AND)   (XOR)
     |      |\\   //|
     |      | \\ // |
     |      |   X   |
     |      | // \\ |
     |      |//   \\|
     gdf    mcm tdw
     mcm(x) gdf(x)
    (AND)  (XOR)
     |\\   //|
     | \\ // |
     |   X   |
     | // \\ |
     |//   \\|
    x10    y10
    '''
    swap_connections(('x10', 'AND', 'y10', 'mcm'), ('x10', 'XOR', 'y10', 'gdf'))
    wrong_wires.append('mcm')
    wrong_wires.append('gdf')
    '''
    Wrong addition when i=15
    Expected: 65534 Actual: 98302
    Expect: ['z00: 0', 'z01: 1', 'z02: 1', 'z03: 1', 'z04: 1', 'z05: 1', 'z06: 1', 'z07: 1', 'z08: 1', 'z09: 1', 'z10: 1', 'z11: 1', 'z12: 1', 'z13: 1', 'z14: 1', 'z15: 1']
    Actual: ['z00: 0', 'z01: 1', 'z02: 1', 'z03: 1', 'z04: 1', 'z05: 1', 'z06: 1', 'z07: 1', 'z08: 1', 'z09: 1', 'z10: 1', 'z11: 1', 'z12: 1', 'z13: 1', 'z14: 1', 'z15: 0', 'z16: 1']
    
    jpj
    (OR)
     |\\
     |  \\
     |    \\
     |      ckf     dnt(x)
     |     (AND)   (XOR)
     |      |\\   //|
     |      | \\ // |
     |      |   X   |
     |      | // \\ |
     |      |//   \\|
     dnt    dvj    vhr
     z15(x)
    (AND)  (XOR)
     |\\   //|
     | \\ // |
     |   X   |
     | // \\ |
     |//   \\|
    x15    y15
    '''
    swap_connections(('x15', 'AND', 'y15', 'z15'), ('dvj', 'XOR', 'vhr', 'dnt'))
    wrong_wires.append('z15')
    wrong_wires.append('dnt')
    '''
    Wrong addition when i=30
    Expected: 2147483646 Actual: 3221225470
    Expect: ['z00: 0', 'z01: 1', 'z02: 1', 'z03: 1', 'z04: 1', 'z05: 1', 'z06: 1', 'z07: 1', 'z08: 1', 'z09: 1', 'z10: 1', 'z11: 1', 'z12: 1', 'z13: 1', 'z14: 1', 'z15: 1', 'z16: 1', 'z17: 1', 'z18: 1', 'z19: 1', 'z20: 1', 'z21: 1', 'z22: 1', 'z23: 1', 'z24: 1', 'z25: 1', 'z26: 1', 'z27: 1', 'z28: 1', 'z29: 1', 'z30: 1']
    Actual: ['z00: 0', 'z01: 1', 'z02: 1', 'z03: 1', 'z04: 1', 'z05: 1', 'z06: 1', 'z07: 1', 'z08: 1', 'z09: 1', 'z10: 1', 'z11: 1', 'z12: 1', 'z13: 1', 'z14: 1', 'z15: 1', 'z16: 1', 'z17: 1', 'z18: 1', 'z19: 1', 'z20: 1', 'z21: 1', 'z22: 1', 'z23: 1', 'z24: 1', 'z25: 1', 'z26: 1', 'z27: 1', 'z28: 1', 'z29: 1', 'z30: 0', 'z31: 1']
    
    ngc
    (OR)
     |\\
     |  \\
     |    \\
     |      gwc
     |      z30(x)  gwc(x)
     |     (AND)   (XOR)
     |      |\\   //|
     |      | \\ // |
     |      |   X   |
     |      | // \\ |
     |      |//   \\|
     fhg    vrg    kgr
    (AND)  (XOR)
     |\\   //|
     | \\ // |
     |   X   |
     | // \\ |
     |//   \\|
    x30    y30
    '''
    swap_connections(('vrg', 'AND', 'kgr', 'z30'), ('vrg', 'XOR', 'kgr', 'gwc'))
    wrong_wires.append('z30')
    wrong_wires.append('gwc')
    for i in range(1, Z_MAX+1):
        x = 2 ** i - 1
        y = 2 ** i - 1
        actual_z = binary_add(x, y)
        if actual_z != x + y:
            return f"Wrong addition when {i=}\nExpected: {x + y} Actual: {actual_z}\nExpect: {debug(x + y)}\nActual: {debug(actual_z)}"
    
    assert len(wrong_wires) == 8
    wrong_wires.sort()
    return ','.join(wrong_wires)
    
print(solve_part_2())
