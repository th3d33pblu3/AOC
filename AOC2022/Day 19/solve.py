import math

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def read_test_file_data():
    FILE = "test_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parser():
    lines = read_input_file_data().splitlines()
    output = []
    for line in lines:
        line = line.split()
        ls = [line[1][:-1], line[6], line[12], line[18], line[21], line[27], line[30]]
        output.append(tuple(map(int, ls)))
    return output

def test_parser():
    lines = read_test_file_data().splitlines()
    output = []
    for line in lines:
        line = line.split()
        ls = [line[1][:-1], line[6], line[12], line[18], line[21], line[27], line[30]]
        output.append(tuple(map(int, ls)))
    return output

def blueprint_max_geodes(ore_bot_ore_cost, clay_bot_ore_cost, obsidian_bot_ore_cost, obsidian_bot_clay_cost, geode_bot_ore_cost, geode_bot_obsidian_cost, TIME_LIMIT):
    starting_state = (TIME_LIMIT, 1, 0, 0, 0, 0, 0, 0, 0) # time, robots, resources
    expense_limit = (max(ore_bot_ore_cost, clay_bot_ore_cost, obsidian_bot_ore_cost, geode_bot_ore_cost), obsidian_bot_clay_cost, geode_bot_obsidian_cost)

    def can_produce_ore_bot(state):
        return state[5] >= ore_bot_ore_cost
    def can_produce_clay_bot(state):
        return state[5] >= clay_bot_ore_cost
    def can_produce_obsidian_bot(state):
        return state[5] >= obsidian_bot_ore_cost and state[6] >= obsidian_bot_clay_cost
    def can_produce_geode_bot(state):
        return state[5] >= geode_bot_ore_cost and state[7] >= geode_bot_obsidian_cost
    def should_produce_ore_bot(state):
        return state[1] < expense_limit[0] and state[5] < expense_limit[0] * state[0]
    def should_produce_clay_bot(state):
        return state[2] < expense_limit[1] and state[6] < expense_limit[1] * state[0]
    def should_produce_obsidian_bot(state):
        return state[3] < expense_limit[2] and state[7] < expense_limit[2] * state[0]

    def remove_extra_resources(state):
        time, ore_bot, clay_bot, obsidian_bot, geode_bot, ores, clays, obsidians, geodes = state
        return (time, ore_bot, clay_bot, obsidian_bot, geode_bot, min(ores, expense_limit[0] * time), min(clays, expense_limit[1] * time), min(obsidians, expense_limit[2] * time), geodes)

    seen_states = set()
    states = set()
    states.add(starting_state)
    time_max_geodes = [0] * (TIME_LIMIT + 1)
    while len(states) != 0:
        state = states.pop()
        if state in seen_states:
            continue
        seen_states.add(state)

        time, ore_bot, clay_bot, obsidian_bot, geode_bot, ores, clays, obsidians, geodes = state
        time_max_geodes[time] = max(geodes, time_max_geodes[time])
        if geodes < time_max_geodes[time] or time == 0:
            continue

        states.add(remove_extra_resources((time - 1, ore_bot, clay_bot, obsidian_bot, geode_bot, ores + ore_bot, clays + clay_bot, obsidians + obsidian_bot, geodes + geode_bot)))
        if can_produce_ore_bot(state) and should_produce_ore_bot(state):
            states.add(remove_extra_resources((time - 1, ore_bot + 1, clay_bot, obsidian_bot, geode_bot, ores + ore_bot - ore_bot_ore_cost, clays + clay_bot, obsidians + obsidian_bot, geodes + geode_bot)))
        if can_produce_clay_bot(state) and should_produce_clay_bot(state):
            states.add(remove_extra_resources((time - 1, ore_bot, clay_bot + 1, obsidian_bot, geode_bot, ores + ore_bot - clay_bot_ore_cost, clays + clay_bot, obsidians + obsidian_bot, geodes + geode_bot)))
        if can_produce_obsidian_bot(state) and should_produce_obsidian_bot(state):
            states.add(remove_extra_resources((time - 1, ore_bot, clay_bot, obsidian_bot + 1, geode_bot, ores + ore_bot - obsidian_bot_ore_cost, clays + clay_bot - obsidian_bot_clay_cost, obsidians + obsidian_bot, geodes + geode_bot)))
        if can_produce_geode_bot(state):
            states.add(remove_extra_resources((time - 1, ore_bot, clay_bot, obsidian_bot, geode_bot + 1, ores + ore_bot - geode_bot_ore_cost, clays + clay_bot, obsidians + obsidian_bot - geode_bot_obsidian_cost, geodes + geode_bot)))
        
    return time_max_geodes[0]

def solve_part_1():
    TIME_LIMIT = 24
    data = parser()
    quality_levels = 0
    for blueprint in data:
        id, ore_bot_ore_cost, clay_bot_ore_cost, obs_bot_ore_cost, obs_bot_clay_cost, g_bot_ore_cost, g_bot_clay_cost = blueprint
        print(f"Blueprint: {id}")
        max_geodes = blueprint_max_geodes(ore_bot_ore_cost, clay_bot_ore_cost, obs_bot_ore_cost, obs_bot_clay_cost, g_bot_ore_cost, g_bot_clay_cost, TIME_LIMIT)
        print(f"{id} * {max_geodes} = {id * max_geodes}")
        quality_levels += id * max_geodes
    return quality_levels

def solve_part_2():
    TIME_LIMIT = 32
    data = parser()
    max_geode_multiply = 1
    for blueprint in data[:3]:
        id, ore_bot_ore_cost, clay_bot_ore_cost, obs_bot_ore_cost, obs_bot_clay_cost, g_bot_ore_cost, g_bot_clay_cost = blueprint
        print(f"Blueprint: {id}")
        max_geodes = blueprint_max_geodes(ore_bot_ore_cost, clay_bot_ore_cost, obs_bot_ore_cost, obs_bot_clay_cost, g_bot_ore_cost, g_bot_clay_cost, TIME_LIMIT)
        print(f"Max geodes: {max_geodes}")
        max_geode_multiply *= max_geodes
    return max_geode_multiply
    
print(solve_part_2())

# def get_max_geodes(robots: list, resources: list, costs: tuple, time_left: int): # Almost done but still contain problem regarding basic ore reservation.
#     def can_produce_geode_bot():
#         return resources[ORE] >= costs[GEODE][0] and resources[OBSIDIAN] >= costs[GEODE][1]
#     def can_produce_obsidian_bot():
#         return resources[ORE] >= costs[OBSIDIAN][0] and resources[CLAY] >= costs[OBSIDIAN][1]
#     def can_produce_clay_bot():
#         return resources[ORE] >= costs[CLAY]
#     def can_produce_ore_bot():
#         return resources[ORE] >= costs[ORE]
#     def should_produce_obsidian_bot():
#         return robots[OBSIDIAN] < costs[GEODE][1]
#     def should_produce_clay_bot():
#         return robots[CLAY] < costs[OBSIDIAN][1]
#     def should_produce_ore_bot():
#         return robots[ORE] < max(costs[CLAY], costs[OBSIDIAN][0], costs[GEODE][0])
#     def will_obstruct_geode_bot_production(ore_cost, robot_produced):
#         if robots[OBSIDIAN] == 0:
#             return False
#         def time_to_enough_resources_if_no_produce():
#             obsidian_lacking = costs[GEODE][1] - resources[OBSIDIAN]
#             ore_lacking = costs[GEODE][0] - resources[ORE]
#             time_to_enough_obsidian = max(0, math.ceil(obsidian_lacking / robots[OBSIDIAN]))
#             time_to_enough_ore = max(0, math.ceil(ore_lacking / robots[ORE]))
#             return max(time_to_enough_obsidian, time_to_enough_ore)
#         def time_to_enough_resources_if_produce():
#             obsidian_lacking = costs[GEODE][1] - resources[OBSIDIAN]
#             ore_lacking_after_produce = costs[GEODE][0] - resources[ORE] + ore_cost
#             if robot_produced == ORE:
#                 time_to_enough_obsidian = max(0, math.ceil(obsidian_lacking / robots[OBSIDIAN]))
#                 if ore_lacking_after_produce <= 0:
#                     time_to_enough_ore = 0
#                 elif ore_lacking_after_produce <= robots[ORE]:
#                     time_to_enough_ore = 1
#                 else:
#                     time_to_enough_ore = math.ceil((ore_lacking_after_produce - robots[ORE]) / (robots[ORE] + 1)) + 1
#                 return max(time_to_enough_obsidian, time_to_enough_ore)
#             elif robot_produced == OBSIDIAN:
#                 if obsidian_lacking <= 0:
#                     time_to_enough_obsidian = 0
#                 elif obsidian_lacking <= robots[OBSIDIAN]:
#                     time_to_enough_obsidian = 1
#                 else:
#                     time_to_enough_obsidian = math.ceil((obsidian_lacking - robots[OBSIDIAN]) / (robots[OBSIDIAN] + 1)) + 1
#                 time_to_enough_ore = max(0, math.ceil(ore_lacking_after_produce / robots[ORE]))
#                 return max(time_to_enough_obsidian, time_to_enough_ore)
#             else:
#                 time_to_enough_obsidian = max(0, math.ceil(obsidian_lacking / robots[OBSIDIAN]))
#                 time_to_enough_ore = max(0, math.ceil(ore_lacking_after_produce / robots[ORE]))
#                 return max(time_to_enough_obsidian, time_to_enough_ore)
#         if time_to_enough_resources_if_produce() > time_to_enough_resources_if_no_produce(): # Obstructs if it cause longer waiting time
#             # print(f"Geode bot obstructed production.")
#             return True
#         else:
#             return False
#     def will_obstruct_obsidian_bot_production(ore_cost, robot_produced):
#         if robots[CLAY] == 0:
#             return False
#         def time_to_enough_resources_if_no_produce():
#             clay_lacking = costs[OBSIDIAN][1] - resources[CLAY]
#             ore_lacking = costs[OBSIDIAN][0] - resources[ORE]
#             time_to_enough_clay = max(0, math.ceil(clay_lacking / robots[CLAY]))
#             time_to_enough_ore = max(0, math.ceil(ore_lacking / robots[ORE]))
#             return max(time_to_enough_clay, time_to_enough_ore)
#         def time_to_enough_resources_if_produce():
#             clay_lacking = costs[OBSIDIAN][1] - resources[CLAY]
#             ore_lacking_after_produce = costs[OBSIDIAN][0] - resources[ORE] + ore_cost
#             if robot_produced == ORE:
#                 time_to_enough_clay = max(0, math.ceil(clay_lacking / robots[CLAY]))
#                 if ore_lacking_after_produce <= 0:
#                     time_to_enough_ore = 0
#                 elif ore_lacking_after_produce <= robots[ORE]:
#                     time_to_enough_ore = 1
#                 else:
#                     time_to_enough_ore = math.ceil((ore_lacking_after_produce - robots[ORE]) / (robots[ORE] + 1)) + 1
#                 return max(time_to_enough_clay, time_to_enough_ore)
#             elif robot_produced == CLAY:
#                 if clay_lacking <= 0:
#                     time_to_enough_clay = 0
#                 elif clay_lacking <= robots[CLAY]:
#                     time_to_enough_clay = 1
#                 else:
#                     time_to_enough_clay = math.ceil((clay_lacking - robots[CLAY]) / (robots[CLAY] + 1)) + 1
#                 time_to_enough_ore = max(0, math.ceil(ore_lacking_after_produce / robots[ORE]))
#                 return max(time_to_enough_clay, time_to_enough_ore)
#             else:
#                 time_to_enough_clay = max(0, math.ceil(clay_lacking / robots[CLAY]))
#                 time_to_enough_ore = max(0, math.ceil(ore_lacking_after_produce / robots[ORE]))
#                 return max(time_to_enough_clay, time_to_enough_ore)

#         if time_to_enough_resources_if_produce() > time_to_enough_resources_if_no_produce(): # Obstructs if it cause longer waiting time
#             # print(f"Obsidian bot obstructed production.")
#             return True
#         else:
#             return False
#     def will_obstruct_clay_bot_production(ore_cost=costs[ORE], robot_produced=ORE):
#         def time_to_enough_resources_if_no_produce():
#             ore_lacking = costs[CLAY] - resources[ORE]
#             time_to_enough_ore = max(0, math.ceil(ore_lacking / robots[ORE]))
#             return time_to_enough_ore
#         def time_to_enough_resources_if_produce():
#             ore_lacking_after_produce = costs[CLAY] - resources[ORE] + ore_cost
#             if ore_lacking_after_produce <= 0:
#                 time_to_enough_ore = 0
#             elif ore_lacking_after_produce <= robots[ORE]:
#                 time_to_enough_ore = 1
#             else:
#                 time_to_enough_ore = math.ceil((ore_lacking_after_produce - robots[ORE]) / (robots[ORE] + 1)) + 1
#             return time_to_enough_ore
#         return time_to_enough_resources_if_produce() > time_to_enough_resources_if_no_produce()
#     def produce_geode_bot():
#         # print(f"Create geode bot with cost {costs[GEODE]}.")
#         resources[ORE] -= costs[GEODE][0]
#         resources[OBSIDIAN] -= costs[GEODE][1]
#         robots[GEODE] += 1
#     def produce_obsidian_bot():
#         # print(f"Create obsidian bot with cost {costs[OBSIDIAN]}.")
#         resources[ORE] -= costs[OBSIDIAN][0]
#         resources[CLAY] -= costs[OBSIDIAN][1]
#         robots[OBSIDIAN] += 1
#     def produce_clay_bot():
#         # print(f"Create clay bot with cost {costs[CLAY]}.")
#         resources[ORE] -= costs[CLAY]
#         robots[CLAY] += 1
#     def produce_ore_bot():
#         # print(f"Create ore bot with cost {costs[ORE]}.")
#         resources[ORE] -= costs[ORE]
#         robots[ORE] += 1
#     def mine():
#         nonlocal time_left
#         time_left -= 1
#         # print(f"Your robots: {robots}")
#         for i in range(4):
#             resources[i] += robots[i]
#         # print(f"Resources after mining: {resources}")

#     while time_left > 0:
#         # print()
#         # print(f"Time: {TIME_LIMIT - time_left + 1}")
#         if can_produce_geode_bot():
#             mine()
#             produce_geode_bot()
#             continue
#         if can_produce_obsidian_bot() and should_produce_obsidian_bot():
#             if not will_obstruct_geode_bot_production(costs[OBSIDIAN][0], OBSIDIAN):
#                 mine()
#                 produce_obsidian_bot()
#                 continue
#             # else:
#                 # print("Obsidian bot production blocked.")
#         if can_produce_clay_bot() and should_produce_clay_bot():
#             if not will_obstruct_geode_bot_production(costs[CLAY], CLAY) and not will_obstruct_obsidian_bot_production(costs[CLAY], CLAY):
#                 mine()
#                 produce_clay_bot()
#                 continue
#             # else:
#                 # print("Clay bot production blocked.")
#         if can_produce_ore_bot() and should_produce_ore_bot():
#             if not will_obstruct_geode_bot_production(costs[ORE], ORE) and not will_obstruct_obsidian_bot_production(costs[ORE], ORE) and not will_obstruct_clay_bot_production(costs[ORE], ORE):
#                 mine()
#                 produce_ore_bot()
#                 continue
#             # else:
#                 # print("Ore bot production blocked.")
#         mine()
#     return resources[GEODE]

# def recursion_helper(ore_bots, clay_bots, obsidian_bots, geode_bots, ores, clays, obsidians, geodes, costs, time_left): # Still too sloww
#     def can_produce_geode_bot():
#         return ores >= costs[GEODE][0] and obsidians >= costs[GEODE][1]
#     def can_produce_obsidian_bot():
#         return ores >= costs[OBSIDIAN][0] and clays >= costs[OBSIDIAN][1]
#     def can_produce_clay_bot():
#         return ores >= costs[CLAY]
#     def can_produce_ore_bot():
#         return ores >= costs[ORE]
#     def should_produce_obsidian_bot():
#         return obsidian_bots < costs[GEODE][1]
#     def should_produce_clay_bot():
#         return clay_bots < costs[OBSIDIAN][1]
#     def should_produce_ore_bot():
#         return ore_bots < max(costs[CLAY], costs[OBSIDIAN][0], costs[GEODE][0])
    
#     if time_left < 0:
#         raise Exception("Unexpected time skip.")
#     if time_left == 0:
#         return geodes
#     maxes = set()
#     if can_produce_geode_bot():
#         maxes.add(recursion_helper(ore_bots, clay_bots, obsidian_bots, geode_bots + 1, 
#                                    ores - costs[GEODE][0] + ore_bots, clays + clay_bots, obsidians - costs[GEODE][1] + obsidian_bots, geodes + geode_bots,
#                                    costs, time_left - 1))
#     if can_produce_obsidian_bot() and should_produce_obsidian_bot():
#         maxes.add(recursion_helper(ore_bots, clay_bots, obsidian_bots + 1, geode_bots,
#                                    ores - costs[OBSIDIAN][0] + ore_bots, clays - costs[OBSIDIAN][1] + clay_bots, obsidians + obsidian_bots, geodes + geode_bots,
#                                    costs, time_left - 1))
#     if can_produce_clay_bot() and should_produce_clay_bot():
#         maxes.add(recursion_helper(ore_bots, clay_bots + 1, obsidian_bots, geode_bots,
#                                    ores - costs[CLAY] + ore_bots, clays + clay_bots, obsidians + obsidian_bots, geodes + geode_bots,
#                                    costs, time_left - 1))
#     if can_produce_ore_bot() and should_produce_ore_bot():
#         maxes.add(recursion_helper(ore_bots + 1, clay_bots, obsidian_bots, geode_bots,
#                                    ores - costs[ORE] + ore_bots, clays + clay_bots, obsidians + obsidian_bots, geodes + geode_bots,
#                                    costs, time_left - 1))
#     maxes.add(recursion_helper(ore_bots, clay_bots, obsidian_bots, geode_bots,
#                                ores + ore_bots, clays + clay_bots, obsidians + obsidian_bots, geodes + geode_bots,
#                                costs, time_left - 1))
#     return max(maxes)