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
    return hp, damage

boss_hp, boss_damage = parse_inputs()
player_hp = 50
player_mana = 500

'''
boss_hp, player_hp, player_mana, total_mana_spent, shield_timer, poison_timer, recharge_timer, win_lose 
'''
starting_state = (boss_hp, player_hp, player_mana, 0, 0, 0, 0, 0)

'''
Magic missile: 4 dmg
Drain: do 2 dmg and heal 2 dmg
Shield: Gain 7 armor (boss do 1 dmg) for 6 turns
Poison: Do 3 dmg for 6 turns
Recharge: Gain 101 mana for 5 turns
'''
MAGIC_MISSILE_COST = 53
MAGIC_MISSILE_DAMAGE = 4
DRAIN_COST = 73
DRAIN_DAMAGE_AND_HEAL = 2
SHIELD_COST = 113
SHIELD_VALUE = 7
SHIELD_TIMER = 6
POISON_COST = 173
POISON_DAMAGE = 3
POISON_TIMER = 6
RECHARGE_COST = 229
RECHARGE_MANA_GAIN = 101
RECHARGE_TIMER = 5

MIN_MANA_TO_CAST = min(MAGIC_MISSILE_COST, DRAIN_COST, SHIELD_COST, POISON_COST, RECHARGE_COST)

HARD = False

def perform_boss_turn(boss_hp, player_hp, player_mana, total_mana_spent, shield_timer, poison_timer, recharge_timer, win_lose) -> tuple:
    player_armor = 0

    # Handling timer and effects
    if shield_timer > 0:
        player_armor = SHIELD_VALUE
        shield_timer -= 1
    if poison_timer > 0:
        boss_hp -= POISON_DAMAGE
        poison_timer -= 1
    if recharge_timer > 0:
        player_mana += RECHARGE_MANA_GAIN
        recharge_timer -= 1

    # If boss die due to magic effect
    if boss_hp <= 0:
        return (0, player_hp, player_mana, total_mana_spent, shield_timer, poison_timer, recharge_timer, 1)
    
    # Else boss attacks player
    player_hp -= max(1, boss_damage - player_armor)
    if player_hp <= 0: # If player dies from boss attack
        return (boss_hp, 0, player_mana, total_mana_spent, shield_timer, poison_timer, recharge_timer, -1)
    else: # If player still in the game
        return (boss_hp, player_hp, player_mana, total_mana_spent, shield_timer, poison_timer, recharge_timer, win_lose)

def get_next_states(state):
    global HARD
    boss_hp, player_hp, player_mana, total_mana_spent, shield_timer, poison_timer, recharge_timer, win_lose = state

    ### Note: This can be further optimized by keeping a global variable of the minimum total mana spent of a winning state.
    ###       Only continue to run if the total_mana_spent is less than that global variable.

    if HARD:
        player_hp -= 1 # Reduce player hp by 1 due to hard mode
        if player_hp <= 0: # If player dies from the hp reduction
            return set(), set()
    
    # Handling timer and effects
    if shield_timer > 0:
        shield_timer -= 1
    if poison_timer > 0:
        boss_hp -= POISON_DAMAGE
        poison_timer -= 1
    if recharge_timer > 0:
        player_mana += RECHARGE_MANA_GAIN
        recharge_timer -= 1

    # If boss die due to magic effect
    if boss_hp <= 0:
        return set(), {(0, player_hp, player_mana, total_mana_spent, shield_timer, poison_timer, recharge_timer, 1)}

    # If player does not have enough mana to cast any spells, player loses
    if player_mana < MIN_MANA_TO_CAST:
        # return {(boss_hp, player_hp, player_mana, total_mana_spent, shield_timer, poison_timer, recharge_timer, -1)}
        return set(), set()

    new_states = set()
    
    # Cast Magic Missile
    if player_mana >= MAGIC_MISSILE_COST:
        new_player_mana = player_mana - MAGIC_MISSILE_COST
        new_total_mana_spent = total_mana_spent + MAGIC_MISSILE_COST
        new_boss_hp = boss_hp - MAGIC_MISSILE_DAMAGE
        new_states.add(perform_boss_turn(new_boss_hp, player_hp, new_player_mana, new_total_mana_spent, shield_timer, poison_timer, recharge_timer, win_lose))

    # Cast Drain
    if player_mana >= DRAIN_COST:
        new_player_mana = player_mana - DRAIN_COST
        new_total_mana_spent = total_mana_spent + DRAIN_COST
        new_boss_hp = boss_hp - DRAIN_DAMAGE_AND_HEAL
        new_player_hp = player_hp + DRAIN_DAMAGE_AND_HEAL
        new_states.add(perform_boss_turn(new_boss_hp, new_player_hp, new_player_mana, new_total_mana_spent, shield_timer, poison_timer, recharge_timer, win_lose))

    # Cast Shield
    if player_mana >= SHIELD_COST and shield_timer == 0:
        new_player_mana = player_mana - SHIELD_COST
        new_total_mana_spent = total_mana_spent + SHIELD_COST
        new_states.add(perform_boss_turn(boss_hp, player_hp, new_player_mana, new_total_mana_spent, SHIELD_TIMER, poison_timer, recharge_timer, win_lose))

    # Cast Poison
    if player_mana >= POISON_COST and poison_timer == 0:
        new_player_mana = player_mana - POISON_COST
        new_total_mana_spent = total_mana_spent + POISON_COST
        new_states.add(perform_boss_turn(boss_hp, player_hp, new_player_mana, new_total_mana_spent, shield_timer, POISON_TIMER, recharge_timer, win_lose))

    # Cast Recharge
    if player_mana >= RECHARGE_COST and recharge_timer == 0:
        new_player_mana = player_mana - RECHARGE_COST
        new_total_mana_spent = total_mana_spent + RECHARGE_COST
        new_states.add(perform_boss_turn(boss_hp, player_hp, new_player_mana, new_total_mana_spent, shield_timer, poison_timer, RECHARGE_TIMER, win_lose))

    continue_states = set()
    won_states = set()
    for state in new_states:
        if state[-1] == 1: # If won
            won_states.add(state)
        elif state[-1] == 0: # If not yet ended
            continue_states.add(state)

    return continue_states, won_states

def solve_part_1():
    states = {starting_state}
    winning_states = set()
    seen_states = set()
    while len(states) > 0:
        new_states = set()
        for state in states:
            continue_states, won_states = get_next_states(state)
            if len(won_states) > 0:
                winning_states = winning_states.union(won_states)
            new_states = new_states.union(continue_states)
        seen_states = seen_states.union(states)
        states = new_states.difference(seen_states)

    won_costs = []
    for state in winning_states:
        won_costs.append(state[3])
    return min(won_costs)

def solve_part_2():
    global HARD
    HARD = True
    return solve_part_1()
    
print(solve_part_2())
