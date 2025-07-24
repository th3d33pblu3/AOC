def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

# def solve_part_1():
#     NUM_CARDS = 10007
#     cards = [i for i in range(NUM_CARDS)]
#     for instruction in read_input_file_data().splitlines():
#         if instruction.startswith("deal into new stack"):
#             # Deal into new stack (reverse)
#             cards.reverse()
#         elif instruction.startswith("deal with increment"):
#             # Deal with increment (indexing)
#             n = int(instruction.removeprefix("deal with increment "))
#             new_cards = [-1] * NUM_CARDS
#             ptr = 0
#             for card in cards:
#                 new_cards[ptr] = card
#                 ptr = (ptr + n) % NUM_CARDS
#             cards = new_cards
#         elif instruction.startswith("cut"):
#             # Cut (rotate left)
#             n = int(instruction.removeprefix("cut ")) % NUM_CARDS
#             cards = cards[n:] + cards[:n]
#     return cards.index(2019)

def solve_part_1():
    NUM_CARDS = 10007
    card_pos = 2019
    for instruction in read_input_file_data().splitlines():
        if instruction.startswith("deal into new stack"):
            # Deal into new stack (reverse)
            card_pos = NUM_CARDS - 1 - card_pos
        elif instruction.startswith("deal with increment"):
            # Deal with increment (indexing)
            n = int(instruction.removeprefix("deal with increment "))
            card_pos = (card_pos * n) % NUM_CARDS
        elif instruction.startswith("cut"):
            # Cut (rotate left)
            n = int(instruction.removeprefix("cut ")) % NUM_CARDS
            card_pos = (card_pos - n) % NUM_CARDS
    return card_pos

# def solve_part_2():
#     REV, INC, CUT = 0, 1, 2
#     def process_instruction(instruction):
#         if instruction.startswith("deal into new stack"):
#             return (REV, None)
#         elif instruction.startswith("deal with increment"):
#             n = int(instruction.removeprefix("deal with increment "))
#             return (INC, n)
#         elif instruction.startswith("cut"):
#             n = int(instruction.removeprefix("cut "))
#             return (CUT, n)
        
#     NUM_CARDS = 119315717514047
#     NUM_LOOPS = 101741582076661
#     instructions = read_input_file_data().splitlines()
#     instructions.reverse()
#     instructions = list(map(process_instruction, instructions))

#     states = {}
#     card_pos = 2020
#     loops = NUM_LOOPS
#     while loops > 0:
#         # Deshuffle base on previous states
#         if card_pos in states:
#             loop_pos = card_pos
#             card_pos = states[card_pos]
#             loop_size = 1
#             remainders = { 0: loop_pos, 1: card_pos }
#             while card_pos != loop_pos:
#                 card_pos = states[card_pos]
#                 loop_size += 1
#                 remainders[loop_size] = card_pos
#             card_pos = remainders[loops % loop_size]
#             loops = 0
#             break

#         # Deshuffle manually
#         original_card_pos = card_pos
#         for ins_type, n in instructions:
#             if ins_type == REV:
#                 # Deal into new stack (reverse)
#                 card_pos = NUM_CARDS - 1 - card_pos
#             elif ins_type == INC:
#                 # Deal with increment (indexing)
#                 k = pow(n, -1, NUM_CARDS)
#                 card_pos = (card_pos * k) % NUM_CARDS
#             elif ins_type == CUT:
#                 # Cut (rotate left)
#                 card_pos = (card_pos + n) % NUM_CARDS
#         states[original_card_pos] = card_pos
#         loops -= 1
#     return card_pos
    
def solve_part_2():
    REV, INC, CUT = 0, 1, 2
    def process_instruction(instruction):
        if instruction.startswith("deal into new stack"):
            return (REV, None)
        elif instruction.startswith("deal with increment"):
            n = int(instruction.removeprefix("deal with increment "))
            return (INC, n)
        elif instruction.startswith("cut"):
            n = int(instruction.removeprefix("cut "))
            return (CUT, n)
        
    NUM_CARDS = 119315717514047
    NUM_LOOPS = 101741582076661
    instructions = read_input_file_data().splitlines()
    instructions.reverse()
    instructions = list(map(process_instruction, instructions))

    card_pos = 2020
    # Track equation for shuffle
    multiple = 1
    constant = 0
    for ins_type, n in instructions:
        if ins_type == REV:
            # Deal into new stack (reverse)
            multiple *= -1
            constant *= -1
            constant += -1
        elif ins_type == INC:
            # Deal with increment (indexing)
            k = pow(n, -1, NUM_CARDS)
            multiple *= k
            constant *= k
        elif ins_type == CUT:
            # Cut (rotate left)
            constant += n

    # Do some math
    a = multiple % NUM_CARDS
    b = constant % NUM_CARDS
    return (pow(a, NUM_LOOPS, mod=NUM_CARDS) * card_pos + b * (pow(a, NUM_LOOPS, mod=NUM_CARDS) - 1) * pow(a - 1, -1, mod=NUM_CARDS)) % NUM_CARDS
    
print(solve_part_2())
