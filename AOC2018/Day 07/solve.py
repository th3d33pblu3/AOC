from queue import PriorityQueue

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    steps = []
    for line in read_input_file_data().splitlines():
        line = line.split()
        pre = line[1]
        post = line[7]
        steps.append((pre, post))

    pres = set()
    posts = set()
    locks: dict[str, set] = {}
    for pre, post in steps:
        pres.add(pre)
        posts.add(post)
        if post in locks:
            locks[post].add(pre)
        else:
            locks[post] = set(pre)
    
    sequence = []
    pq = PriorityQueue()
    for task in pres.difference(posts):
        pq.put(task)
    while not pq.empty():
        task = pq.get()
        sequence.append(task)
        keys = set(locks.keys())
        for post in keys:
            if task in locks[post]:
                locks[post].remove(task)
                if len(locks[post]) == 0:
                    locks.pop(post)
                    pq.put(post)
    return ''.join(sequence)

OFFSET = ord('A') - 1
BASE = 60
NUM_WORKERS = 5

def get_task_time(c: str) -> int:
    return BASE + ord(c) - OFFSET

def solve_part_2():
    steps = []
    for line in read_input_file_data().splitlines():
        line = line.split()
        pre = line[1]
        post = line[7]
        steps.append((pre, post))

    pres = set()
    posts = set()
    locks: dict[str, set] = {}
    for pre, post in steps:
        pres.add(pre)
        posts.add(post)
        if post in locks:
            locks[post].add(pre)
        else:
            locks[post] = set(pre)
    
    pq = PriorityQueue()
    for task in pres.difference(posts):
        pq.put(task)
    workers = [0] * NUM_WORKERS
    working_tasks = [''] * NUM_WORKERS

    time = 0
    while (not pq.empty()) or max(workers) != 0:
        # Do work
        if min(workers) != 0 or pq.empty(): # All busy or no more tasks
            speedup = float('inf')
            for i in range(NUM_WORKERS):
                if workers[i] != 0 and workers[i] < speedup:
                    speedup = workers[i]
            time += speedup
            for i in range(NUM_WORKERS):
                workers[i] = max(workers[i] - speedup, 0)
                if workers[i] == 0: # If finish task
                    finished_task = working_tasks[i]
                    keys = set(locks.keys())
                    for key in keys:
                        if finished_task in locks[key]:
                            locks[key].remove(finished_task)
                            if len(locks[key]) == 0:
                                locks.pop(key)
                                pq.put(key)

        # Assign task
        if pq.empty():
            continue
        task = pq.get()
        for i in range(NUM_WORKERS):
            if workers[i] == 0:
                workers[i] = get_task_time(task)
                working_tasks[i] = task
                break
    return time
    
print(solve_part_2())
