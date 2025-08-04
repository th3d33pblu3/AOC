from enum import Enum

class Positions(Enum):
    H1: 0
    H2: 1
    R1: 2
    H3: 3
    R2: 4
    H4: 5
    R3: 6
    H5: 7
    R4: 8
    H6: 9
    H7: 10

NUM_LOCATIONS = 11
ROOMS = (2, 4, 6, 8)
HALLWAYS = (0, 1, 3, 5, 7, 9, 10)

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

data = read_input_file_data().splitlines()
room_data = [[data[2][3], data[3][3]], [data[2][5], data[3][5]], [data[2][7], data[3][7]], [data[2][9], data[3][9]]]

def get_init():
    global room_data
    return room_data

def solve_part_1():
    multiplier = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }
    room_targets = ('A', 'B', 'C', 'D')
    rooms = get_init()
    overhead_cost = 0

    # Ignore amphipods that do not need to move
    for i in range(4):
        while rooms[i] and rooms[i][-1] == room_targets[i]:
            rooms[i].pop()

    # Initial setup by adding cost to move to hallway and adding cost to move back in
    for i in range(4):
        required_steps = 1
        for x in rooms[i]:
            overhead_cost += required_steps * multiplier[x] # Cost for amphipod to move out
            overhead_cost += required_steps * multiplier[room_targets[i]] # Cost for right amphipod to move in
            required_steps += 1
    
    # Branching function
    def get_moves(state):
        hallway_state, rooms_state = state
        moves = [] # ((hallway_state, rooms_state), cost)

        for start_loc in range(NUM_LOCATIONS):
            for end_loc in range(NUM_LOCATIONS):
                # Did not move
                if start_loc == end_loc:
                    continue
                # Nothing to move
                if ((start_loc in ROOMS and not rooms_state[ROOMS.index(start_loc)]) or
                    (start_loc in HALLWAYS and not hallway_state[start_loc])):
                    continue
                # Moving in hallway
                if start_loc in HALLWAYS and end_loc in HALLWAYS:
                    continue
                # Blocked due to uncleared room
                if end_loc in ROOMS and rooms_state[ROOMS.index(end_loc)]:
                    continue
                # Blocked due to incompatible room
                if end_loc in ROOMS and ROOMS.index(end_loc) != room_targets.index(hallway_state[start_loc] if start_loc in HALLWAYS else rooms_state[ROOMS.index(start_loc)][0]):
                    continue
                # Blocked in hallway
                is_movable = True
                direction = 1 if end_loc > start_loc else -1
                for loc in range(start_loc + 1 * direction, end_loc + 1 * direction, direction):
                    if hallway_state[loc]: # Something there
                        is_movable = False
                        break
                if not is_movable:
                    continue
                
                # Can move
                move_result = move(state, start_loc, end_loc)
                if move_result: # Ignore cases where room cannot be entered due to mismatch
                    moves.append(move_result)
        return moves

    # Moving function
    def move(state, start_loc, end_loc):
        hallway_state, rooms_state = state
        hallway_state = list(hallway_state)
        rooms_state = list(map(list, rooms_state))

        obj = hallway_state[start_loc] if start_loc in HALLWAYS else rooms_state[ROOMS.index(start_loc)].pop(0)
        if start_loc in HALLWAYS:
            hallway_state[start_loc] = None
        if end_loc in HALLWAYS:
            hallway_state[end_loc] = obj
        return ((tuple(hallway_state), tuple(map(tuple, rooms_state))), abs(end_loc - start_loc) * multiplier[obj])

    # Solving
    END_STATE = ((None,) * NUM_LOCATIONS, ((),) * 4)
    initial_hallway_state = (None,) * NUM_LOCATIONS
    initial_rooms_state = tuple(map(tuple, rooms))

    frontier = set()
    frontier.add((initial_hallway_state, initial_rooms_state))
    state_cost = { (initial_hallway_state, initial_rooms_state): 0 }
    while frontier:
        new_frontier = set()
        for state in frontier:
            if state == END_STATE:
                continue
            curr_cost = state_cost[state]
            for new_state, move_cost in get_moves(state):
                new_cost = curr_cost + move_cost
                if new_state in state_cost and new_cost >= state_cost[new_state]:
                    continue
                state_cost[new_state] = new_cost
                new_frontier.add(new_state)
        frontier = new_frontier
    return overhead_cost + state_cost[END_STATE]

def solve_part_2():
    global room_data, data
    room_data = [[data[2][3], 'D', 'D', data[3][3]], [data[2][5], 'C', 'B', data[3][5]], [data[2][7], 'B', 'A', data[3][7]], [data[2][9], 'A', 'C', data[3][9]]]
    return solve_part_1()
    
print(solve_part_2())
