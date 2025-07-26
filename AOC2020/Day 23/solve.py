from collections import deque

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    cups = deque([int(char) for char in read_input_file_data()])
    for _ in range(100):
        # Remove 3 cups clockwise
        cups.rotate(-1)
        cut = []
        cut.append(cups.popleft())
        cut.append(cups.popleft())
        cut.append(cups.popleft())
        cups.rotate(1)
        # Find destination cup
        dest = (cups[0] - 1) % 10
        while dest not in cups:
            dest = (dest - 1) % 10
        # Insert cups
        index = cups.index(dest) + 1
        cups.insert(index, cut[2])
        cups.insert(index, cut[1])
        cups.insert(index, cut[0])
        # Selects new current cup
        cups.rotate(-1)
    
    # Remove cup 1 and pick up cups in order
    while cups[0] != 1:
        cups.rotate(-1)
    cups.popleft()
    return ''.join([str(i) for i in cups])

def solve_part_2():
    class Node():
        def __init__(self, n):
            self.n = n
        
        def set_next(self, next):
            self.next = next

        def get_next(self):
            return self.next
        
        def pick_up_next_three(self):
            one = self.next
            two = one.get_next()
            three = two.get_next()
            self.set_next(three.get_next())
            return [one, two, three]
        
        def insert_picked(self, picked):
            end = self.next
            self.set_next(picked[0])
            picked[2].set_next(end)

    # Setup
    nodes = [Node(n) for n in range(1_000_000 + 1)]
    nodes[0] = None # So that index match number
    init_seq = [int(char) for char in read_input_file_data()]
    for i in range(8):
        nodes[init_seq[i]].set_next(nodes[init_seq[i+1]])
    nodes[init_seq[8]].set_next(nodes[10])
    for i in range(10, 1_000_000):
        nodes[i].set_next(nodes[i+1])
    nodes[1_000_000].set_next(nodes[init_seq[0]])

    # Run
    current = nodes[init_seq[0]]
    for _ in range(10_000_000):
        picked = current.pick_up_next_three()
        picked_vals = [picked[0].n, picked[1].n, picked[2].n]
        target_val = 1_000_000 if current.n == 1 else current.n - 1
        while target_val in picked_vals:
            target_val = 1_000_000 if target_val == 1 else target_val - 1
        target = nodes[target_val]
        target.insert_picked(picked)
        current = current.get_next()

    v1 = nodes[1].get_next().n
    v2 = nodes[1].get_next().get_next().n
    return v1 * v2
    
print(solve_part_2())
