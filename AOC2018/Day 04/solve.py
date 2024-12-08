def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

SLEEP = -1
WAKE = -2

def parse(data: str) -> list[list, set]:
    output = []
    guards = set()
    for line in data.splitlines():
        year = int(line[1:5])
        month = int(line[6:8])
        day = int(line[9:11])
        hour = int(line[12:14])
        minute = int(line[15:17])

        command_character = line[19]
        if command_character == 'G': # Change shift
            guard_number = int(line.split()[3][1:])
            output.append((year, month, day, hour, minute, guard_number))
            guards.add(guard_number)
        elif command_character == 'f': # falls asleep
            output.append((year, month, day, hour, minute, SLEEP))
        elif command_character == 'w': # wakes up
            output.append((year, month, day, hour, minute, WAKE))
        else:
            raise Exception(f'Unknown {command_character=}')
    output.sort()
    return output, list(guards)

def solve_part_1():
    parsed_data, guards = parse(read_input_file_data())
    sleep_duration = {}
    sleep_time: dict[int, list] = {}
    wake_time: dict[int, list] = {}
    for guard in guards:
        sleep_duration[guard] = 0
        sleep_time[guard] = []
        wake_time[guard] = []

    current_guard = 0
    for year, month, day, hour, minute, command in parsed_data:
        if command == SLEEP:
            sleep_time[current_guard].append((year, month, day, hour, minute))
        elif command == WAKE:
            l_year, l_month, l_day, l_hour, l_minute = sleep_time[current_guard][-1]
            sleep_duration[current_guard] += (hour - l_hour) * 60 + minute - l_minute
            wake_time[current_guard].append((year, month, day, hour, minute))
        else:
            current_guard = command
    
    max_sleeper = 0
    max_sleep = 0
    for guard in guards:
        if sleep_duration[guard] > max_sleep:
            max_sleeper = guard
            max_sleep = sleep_duration[guard]

    ms_sleep_times = sleep_time[max_sleeper]
    ms_wake_times = wake_time[max_sleeper]
    sleep_counter = [0 for i in range(60)]
    for i in range(len(ms_sleep_times)):
        s_year, s_month, s_day, s_hour, s_minute = ms_sleep_times[i]
        w_year, w_month, w_day, w_hour, w_minute = ms_wake_times[i]
        for x in range(s_minute, w_minute):
            sleep_counter[x] += 1

    max_sleep_min = 0
    max_count = 0
    for i in range(60):
        if sleep_counter[i] > max_count:
            max_count = sleep_counter[i]
            max_sleep_min = i

    return max_sleeper * max_sleep_min

def solve_part_2():
    parsed_data, guards = parse(read_input_file_data())
    num_guards = len(guards)

    guard_id = {}
    for i in range(num_guards):
        guard_id[guards[i]] = i

    sleep_minutes = []
    for i in range(num_guards):
        sleep_minutes.append([0 for _ in range(60)])

    current_guard_id = 0
    cache_sleep_min = 0
    for year, month, day, hour, minute, command in parsed_data:
        if command == SLEEP:
            cache_sleep_min = minute
        elif command == WAKE:
            for i in range(cache_sleep_min, minute):
                sleep_minutes[current_guard_id][i] += 1
        else: # New guard takes shift
            current_guard_id = guard_id[command]
    
    sleeper_id = 0
    sleeper_count = 0
    sleeper_min = 0
    for id in range(num_guards):
        sleep_array = sleep_minutes[id]
        for minute in range(60):
            if sleep_array[minute] > sleeper_count:
                sleeper_count = sleep_array[minute]
                sleeper_id = id
                sleeper_min = minute

    return guards[sleeper_id] * sleeper_min
    
print(solve_part_2())
