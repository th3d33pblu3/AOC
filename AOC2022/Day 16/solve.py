from queue import Queue
import re

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

STARTING_ROOM = "AA"

def parse_data():
    data = read_input_file_data()
    line_data = []
    for line in data.splitlines():
        valve_info, connection_info = line.split("; ")
        valve_words = valve_info.split()
        room_name = valve_words[1]
        valve_flow_rate = int(valve_words[4].split("=")[1])
        connected_rooms = list(re.split(r"valves? ", connection_info)[1].split(", "))

        line_data.append((room_name, valve_flow_rate, connected_rooms))
    return line_data

def get_room_info():
    all_room_names = []
    connections = {}
    valve_room_names = []
    valve_room_flows = {}

    line_data = parse_data()
    for room_name, valve_flow_rate, connected_rooms in line_data:
        all_room_names.append(room_name)
        connections[room_name] = connected_rooms
        if valve_flow_rate != 0:
            valve_room_names.append(room_name) 
            valve_room_flows[room_name] = valve_flow_rate
    
    return all_room_names, connections, valve_room_names, valve_room_flows

def get_all_rooms_min_steps_from_room(starting_room, all_room_names: list, connections: dict):
    steps_from_starting_room = {}
    for room in all_room_names:
        steps_from_starting_room[room] = -1

    frontier = Queue()
    frontier.put(starting_room)
    steps_from_starting_room[starting_room] = 0

    while frontier.qsize() != 0:
        curr_room = frontier.get()
        curr_room_steps = steps_from_starting_room.get(curr_room)
        for next_room in connections.get(curr_room):
            if steps_from_starting_room.get(next_room) == -1:
                steps_from_starting_room[next_room] = curr_room_steps + 1
                frontier.put(next_room)

    return steps_from_starting_room

def get_valve_rooms_min_steps(all_room_names: list, connections: dict, valve_room_names: list):
    valve_room_min_steps = {}
    for starting_room in valve_room_names:
        all_rooms_min_steps_from_starting_room = get_all_rooms_min_steps_from_room(starting_room, all_room_names, connections)

        valve_room_steps_from_starting_room = {}
        for room in valve_room_names:
            valve_room_steps_from_starting_room[room] = all_rooms_min_steps_from_starting_room[room]
        
        valve_room_min_steps[starting_room] = valve_room_steps_from_starting_room

    return valve_room_min_steps

def get_starting_rooms_min_steps(all_room_names: list, connections: dict):
    return get_all_rooms_min_steps_from_room(STARTING_ROOM, all_room_names, connections)

def get_initial_data():
    all_room_names, connections, valve_room_names, valve_room_flows = get_room_info()
    valve_room_min_steps = get_valve_rooms_min_steps(all_room_names, connections, valve_room_names)
    starting_room_min_steps = get_starting_rooms_min_steps(all_room_names, connections)
    return valve_room_names, valve_room_flows, valve_room_min_steps, starting_room_min_steps




def solve_part_1():
    valve_room_names, valve_room_flows, valve_room_min_steps, starting_room_min_steps = get_initial_data()
    STARTING_TIME_LEFT = 30

    def get_max_release(curr_room, opened_valves: set, time_left: int):
        if time_left <= 0:
            return 0, ""
        time_left -= 1
        curr_room_total_release = valve_room_flows[curr_room] * time_left
        opened_valves.add(curr_room)
        seq = f", ({curr_room}, {time_left})"

        max_release = 0
        final_seq = seq
        for room in valve_room_names:
            if room not in opened_valves:
                room_max_release, output_seq = get_max_release(room, opened_valves, time_left - valve_room_min_steps.get(curr_room).get(room))
                if room_max_release > max_release:
                    max_release = room_max_release
                    final_seq = seq + output_seq

        opened_valves.remove(curr_room)
        return curr_room_total_release + max_release, final_seq

    final_max_release = 0
    final_max_seq = None
    for room in valve_room_names:
        max_release, seq_out = get_max_release(room, set(), STARTING_TIME_LEFT - starting_room_min_steps[room])
        if max_release > final_max_release:
            final_max_release = max_release
            final_max_seq = seq_out
    print(STARTING_ROOM + final_max_seq)
    return final_max_release

def solver(starting_time_left, valve_room_names, valve_room_flows, valve_room_min_steps, starting_room_min_steps):
    def get_max_release(curr_room, opened_valves: set, time_left: int):
        if time_left <= 0:
            return 0, []
        time_left -= 1
        curr_room_total_release = valve_room_flows[curr_room] * time_left
        opened_valves.add(curr_room)
        rooms_visited = [curr_room]

        max_release = 0
        final_rooms_visited = []
        for room in valve_room_names:
            if room not in opened_valves:
                room_max_release, output_seq = get_max_release(room, opened_valves, time_left - valve_room_min_steps.get(curr_room).get(room))
                if room_max_release > max_release:
                    max_release = room_max_release
                    final_rooms_visited = output_seq

        opened_valves.remove(curr_room)
        return curr_room_total_release + max_release, rooms_visited + final_rooms_visited

    final_max_release = 0
    final_max_rooms_visited = None
    for room in valve_room_names:
        max_release, max_rooms_visited = get_max_release(room, set(), starting_time_left - starting_room_min_steps[room])
        if max_release > final_max_release:
            final_max_release = max_release
            final_max_rooms_visited = max_rooms_visited
    return final_max_release, final_max_rooms_visited

def solve_part_2():
    valve_room_names, valve_room_flows, valve_room_min_steps, starting_room_min_steps = get_initial_data()
    STARTING_TIME_LEFT = 26

    you_final_max_release, you_rooms_visited = solver(STARTING_TIME_LEFT, valve_room_names, valve_room_flows, valve_room_min_steps, starting_room_min_steps)
    valve_rooms_for_ele = valve_room_names.copy()
    for room in you_rooms_visited:
        valve_rooms_for_ele.remove(room)
    ele_final_max_release, ele_rooms_visited = solver(STARTING_TIME_LEFT, valve_rooms_for_ele, valve_room_flows, valve_room_min_steps, starting_room_min_steps)

    return you_final_max_release + ele_final_max_release

    # def get_max_release(room_you, room_ele, time_hold_you, time_hold_ele, time_left: int, closed_valves: list):
    #     if time_left <= 0:
    #         return 0, ""
        
    #     time_left -= 1
    #     closed_valves = closed_valves.copy()

    #     if time_hold_you == 0 and time_hold_ele != 0:
    #         curr_room_total_release = None
    #         if room_you not in closed_valves:
    #             curr_room_total_release = 0
    #             seq = f", (You: {room_you}(visited), {time_left})"
    #         else:
    #             curr_room_total_release = valve_room_flows[room_you] * time_left
    #             closed_valves.remove(room_you)
    #             seq = f", (You: {room_you}, {time_left})"
    #         assert curr_room_total_release != None
    #         time_hold_ele -= 1

    #         max_release = 0
    #         final_seq = seq
    #         for next_room in closed_valves:
    #             next_time_hold_you = valve_room_min_steps[room_you][next_room]
    #             time_skip = min(next_time_hold_you, time_hold_ele)
    #             room_max_release, ouptut_seq = get_max_release(next_room, room_ele, next_time_hold_you - time_skip, time_hold_ele - time_skip, time_left - time_skip, closed_valves)
    #             if room_max_release > max_release:
    #                 max_release = room_max_release
    #                 final_seq = seq + ouptut_seq
    #         return curr_room_total_release + max_release, final_seq
    #     elif time_hold_you != 0 and time_hold_ele == 0:
    #         curr_room_total_release = None
    #         if room_ele not in closed_valves:
    #             curr_room_total_release = 0
    #             seq = f", (Ele: {room_ele}(visited), {time_left})"
    #         else:
    #             curr_room_total_release = valve_room_flows[room_ele] * time_left
    #             closed_valves.remove(room_ele)
    #             seq = f", (Ele: {room_ele}, {time_left})"
    #         assert curr_room_total_release != None
    #         time_hold_you -= 1

    #         max_release = 0
    #         final_seq = seq
    #         for next_room in closed_valves:
    #             next_time_hold_ele = valve_room_min_steps[room_ele][next_room]
    #             time_skip = min(time_hold_you, next_time_hold_ele)
    #             room_max_release, ouptut_seq = get_max_release(room_you, next_room, time_hold_you - time_skip, next_time_hold_ele - time_skip, time_left - time_skip, closed_valves)
    #             if room_max_release > max_release:
    #                 max_release = room_max_release
    #                 final_seq = seq + ouptut_seq
    #         return curr_room_total_release + max_release, final_seq
    #     elif time_hold_you == 0 and time_hold_ele == 0:
    #         curr_room_total_release = None
    #         if room_you not in closed_valves:
    #             curr_room_total_release = 0
    #             seq = f", (You: {room_you}(visited), {time_left})"
    #         else:
    #             curr_room_total_release = valve_room_flows[room_you] * time_left
    #             closed_valves.remove(room_you)
    #             seq = f", (You: {room_you}, {time_left})"
    #         assert curr_room_total_release != None
    #         if room_you != room_ele:
    #             if room_ele not in closed_valves:
    #                 curr_room_total_release += 0
    #                 seq += f", (Ele: {room_ele}(visited), {time_left})"
    #             else:
    #                 curr_room_total_release += valve_room_flows[room_ele] * time_left
    #                 closed_valves.remove(room_ele)
    #                 seq += f", (Ele: {room_ele}, {time_left})"
    #         else:
    #             seq += f", (Ele: {room_ele}(same as you), {time_left})"

    #         max_release = 0
    #         final_seq = seq
    #         for i in range(len(closed_valves)):
    #             next_room_you = closed_valves[i]
    #             next_rooms_for_ele = closed_valves[i:] # Must include duplicate room in case only 1 room left
    #             for next_room_ele in next_rooms_for_ele:
    #                 next_time_hold_you = valve_room_min_steps[room_you][next_room_you]
    #                 next_time_hold_ele = valve_room_min_steps[room_ele][next_room_ele]
    #                 time_skip = min(next_time_hold_you, next_time_hold_ele)
    #                 room_max_release, output_seq = get_max_release(next_room_you, next_room_ele, next_time_hold_you - time_skip, next_time_hold_ele - time_skip, time_left - time_skip, closed_valves)
    #                 if room_max_release > max_release:
    #                     max_release = room_max_release
    #                     final_seq = output_seq
    #         return curr_room_total_release + max_release, final_seq
    #     else:
    #         raise Exception(f"Unexpected time holds: You={time_hold_you}, Ele={time_hold_ele}")

    # final_max_releas = 0
    # final_max_seq = None
    # for i in range(len(valve_room_names) - 1): # Assumption: more than 1 room with flow rate > 0
    #     room_you = valve_room_names[i]
    #     rooms_for_ele = valve_room_names[i + 1:]
    #     for room_ele in rooms_for_ele:
    #         time_hold_you = starting_room_min_steps[room_you]
    #         time_hold_ele = starting_room_min_steps[room_ele]
    #         time_skip = min(time_hold_you, time_hold_ele)
    #         max_release, output_seq = get_max_release(room_you, room_ele, time_hold_you - time_skip, time_hold_ele - time_skip, STARTING_TIME_LEFT - time_skip, valve_room_names)
    #         print("Done 1")
    #         if max_release > final_max_releas:
    #             final_max_release = max_release
    #             final_max_seq = output_seq
    # print(STARTING_ROOM + final_max_seq)
    # return final_max_release
    
print(solve_part_2())
