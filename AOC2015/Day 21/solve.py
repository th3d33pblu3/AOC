def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_inputs():
    data = read_input_file_data()
    lines = data.splitlines()
    hp = int(lines[0].split()[-1])
    damage = int(lines[1].split()[-1])
    armor = int(lines[2].split()[-1])
    return hp, damage, armor

boss_hp, boss_damage, boss_armor = parse_inputs()
player_hp = 100
player_damage = 0
player_armor = 0

# (boss_hp, player_hp, player_damage, player_armor, gold_spent, wep, armor, ring1, ring2, win_lose)
# wep, armor, ring1 and ring2 will be the index of the item, -1 if not yet purchased
# win_lose is 0 if not yet ended, 1 if player win and -1 if boss win
starting_state = (boss_hp, player_hp, player_damage, player_armor, 0, -1, -1, -1, -1, 0)

# (Cost, damage, armor)
WEAPONS = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
ARMORS = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
RINGS = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

def attack(attacker_damage: int, defender_armor: int, defender_hp: int) -> int:
    '''
    Return the hp after being attacked.
    '''
    return defender_hp - max(1, attacker_damage - defender_armor)

def quick_forward_state(state: tuple) -> tuple:
    boss_hp, player_hp, player_damage, player_armor, gold_spent, wep, armor, ring1, ring2, win_lose = state
    if win_lose == 0:
        while True:
            boss_hp = attack(player_damage, boss_armor, boss_hp)
            if boss_hp <= 0:
                return 0, player_hp, player_damage, player_armor, gold_spent, wep, armor, ring1, ring2, 1
            player_hp = attack(boss_damage, player_armor, player_hp)
            if player_hp <= 0:
                return boss_hp, 0, player_damage, player_armor, gold_spent, wep, armor, ring1, ring2, -1
    return state

def get_next_states(state: tuple):
    boss_hp, player_hp, player_damage, player_armor, gold_spent, wep, armor, ring1, ring2, win_lose = state
    next_states = set()

    # Buy weapon
    if wep == -1: # If weapon has not been bought
        for i in range(len(WEAPONS)): # Try buying every weapon
            wep_cost, wep_damage, wep_armor = WEAPONS[i]
            next_states.add((boss_hp, player_hp, player_damage + wep_damage, player_armor + wep_armor, gold_spent + wep_cost, i, armor, ring1, ring2, win_lose))
        return next_states, None # Must buy 1 weapon

    # Attack
    attacked_state = quick_forward_state(state) # Once player starts attacking, it should not buy items again

    # Buy armor
    if armor == -1: # If armor has not been bought
        for i in range(len(ARMORS)): # Try buying every armor
            armor_cost, armor_damage, armor_armor = ARMORS[i]
            next_states.add((boss_hp, player_hp, player_damage + armor_damage, player_armor + armor_armor, gold_spent + armor_cost, wep, i, ring1, ring2, win_lose))

    # Buy ring
    if ring1 == -1: # If first ring has not been bought
        for i in range(len(RINGS)): # Try buying every ring
            ring_cost, ring_damage, ring_armor = RINGS[i]
            next_states.add((boss_hp, player_hp, player_damage + ring_damage, player_armor + ring_armor, gold_spent + ring_cost, wep, armor, i, ring2, win_lose))
    elif ring2 == -1: # If second ring has not been bought
        for i in range(len(RINGS)): # Try buying every ring that is not the same as the first ring
            if (i == ring1):
                continue
            ring_cost, ring_damage, ring_armor = RINGS[i]
            next_states.add((boss_hp, player_hp, player_damage + ring_damage, player_armor + ring_armor, gold_spent + ring_cost, wep, armor, ring1, i, win_lose))
    
    return next_states, attacked_state

def solve_part_1():
    global starting_state
    states = {starting_state}
    winning_states = set()
    seen_states = set()
    while len(states) > 0:
        new_states = set()
        for state in states:
            next_states, attacked_state = get_next_states(state)
            if attacked_state != None and attacked_state[-1] == 1: # If won
                winning_states.add(attacked_state)
            new_states = new_states.union(next_states)
        seen_states = seen_states.union(states)
        states = new_states.difference(seen_states)

    won_costs = []
    for state in winning_states:
        won_costs.append(state[4])
    return min(won_costs)

def solve_part_2():
    global starting_state
    # (boss_hp, player_hp, player_damage, player_armor, gold_spent, wep, armor, ring1, ring2, win_lose)
    # wep, armor, ring1 and ring2 will be the index of the item, -1 if not yet purchased
    # win_lose is 0 if not yet ended, 1 if player win and -1 if boss win
    states = {starting_state}
    lost_states = set()
    seen_states = set()
    while len(states) > 0:
        new_states = set()
        for state in states:
            next_states, attacked_state = get_next_states(state)
            if attacked_state != None and attacked_state[-1] == -1: # If lost
                lost_states.add(attacked_state)
            new_states = new_states.union(next_states)
        seen_states = seen_states.union(states)
        states = new_states.difference(seen_states)

    lost_costs = []
    for state in lost_states:
        lost_costs.append(state[4])
    return max(lost_costs)
    
print(solve_part_2())
