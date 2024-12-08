from collections import Counter

# E, SG, SM, PG, PM, TG, TM, RG, RM, CG, CM
# STARTING_STATE = (1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2)
# TARGET_STATE   = (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
STARTING_STATE = (1, 1, 1, 1, 1, 1, 1, 1, 1)
TARGET_STATE   = (4, 4, 4, 4, 4, 4, 4, 4, 4)

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
SAVED_ENCODING = {}

def encode_state(state: tuple) -> tuple[int, int]:
    if state == None:
        return None
    result = 1
    for i in range(1, len(state), 2):
        j = i + 1
        result *= PRIMES[((state[i] - 1) * 4) + (state[j] - 1)]
    if result not in SAVED_ENCODING:
        SAVED_ENCODING[result] = state[1:]
    return (state[0], result)

def decode_state(state: tuple[int, int]) -> tuple:
    return (state[0],) + SAVED_ENCODING[state[1]]



def solve_part_1():
    def expand_state(encoded_state: tuple) -> set:
        state = decode_state(encoded_state)
        items_count = len(state) - 1
        assert items_count >= 1

        E_pos = state[0]
        new_states = set()
        for item1 in range(1, items_count + 1):
            # Move 1 item
            if state[item1] != E_pos:
                continue
            new_states.add(encode_state(move(state, E_pos - 1, item1)))
            new_states.add(encode_state(move(state, E_pos + 1, item1)))

            for item2 in range(item1 + 1, items_count + 1):
                # Move 2 items
                if state[item2] != E_pos:
                    continue
                new_states.add(encode_state(move(state, E_pos - 1, item1, item2)))
                new_states.add(encode_state(move(state, E_pos + 1, item1, item2)))

        new_states.discard(None)
        return new_states
    
    def move(state: tuple, new_E_pos: int, item1: int, item2: int = -1) -> tuple | None:
        E_pos = state[0]
        if abs(new_E_pos - E_pos) != 1 or new_E_pos > 4 or new_E_pos <= 0:
            return None
        if state[item1] != E_pos or (item2 != -1 and state[item2] != E_pos):
            return None
        ls = list(state)
        ls[0] = new_E_pos
        ls[item1] = new_E_pos
        if item2 != -1:
            ls[item2] = new_E_pos

        new_state = tuple(ls)
        if item1 % 2 == 0:
            # Chip is moved to new floor
            gen1 = item1 - 1
            chip1 = item1
            # Generator not on same floor as generator and there are other generators in same floor
            if new_state[gen1] != new_state[chip1]:
                for gen in range(1, len(state), 2):
                    if new_state[gen] == new_state[chip1]:
                        return None
        else:
            # Generator is moved to new floor
            gen1 = item1
            chip1 = item1 + 1
            # Chip just got disconnected and there are other generators on the old floor
            if new_state[gen1] != new_state[chip1] and new_state[chip1] == E_pos:
                for gen in range(1, len(state), 2):
                    if new_state[gen] == E_pos:
                        return None

        if item2 != -1:
            if item2 % 2 == 0:
                # Chip is moved to new floor
                gen2 = item2 - 1
                chip2 = item2
                # Generator not on same floor and there are other generators in same floor
                if new_state[gen2] != new_state[chip2]:
                    for gen in range(1, len(state), 2):
                        if new_state[gen] == new_state[chip2]:
                            return None
            else:
                # Generator is moved to new floor
                gen2 = item2
                chip2 = item2 + 1
                # Chip just got disconnected and there are other generators on the old floor
                if new_state[gen2] != new_state[chip2] and new_state[chip2] == E_pos:
                    for gen in range(1, len(state), 2):
                        if new_state[gen] == E_pos:
                            return None
                        
        return new_state

    starting_state = encode_state(STARTING_STATE)
    target_state = encode_state(TARGET_STATE)

    saved_states = { starting_state }
    frontier = { starting_state }
    steps = 0
    while (not target_state in saved_states) and (frontier != set()):
        steps += 1
        new_frontier = set()
        for state in frontier:
            new_frontier = new_frontier.union(expand_state(state))
        frontier = new_frontier.difference(saved_states)
        saved_states.update(frontier)
    
    return steps if target_state in saved_states else -1


def solve_part_2():
    # # E, SG, SM, PG, PM, TG, TM, RG, RM, CG, CM, EG, EM, DG, DM
    STARTING_STATE = (1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1)
    TARGET_STATE   = (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
    
    # Solve manually
    # Each new pair of 1s on floor 1 increase steps by 12
    # Each level increase decrease steps by 2
    assert STARTING_STATE[0] == 1
    assert len(STARTING_STATE) % 2 == 1

    count = dict(Counter(STARTING_STATE[1:]))
    twos = count[2]
    threes = count[3]
    
    num_pairs = (len(STARTING_STATE) - 1) // 2
    if num_pairs == 1:
        return 3
    
    return (3 + (num_pairs - 1) * 12) - (2 * twos) - (4 * threes)
    
print(solve_part_2())
