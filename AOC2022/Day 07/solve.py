from __future__ import annotations

INF = 70000000

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

class Directory:
    def __init__(self, name, parent: Directory):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0
        self.is_final_size = False
    
    def add_children(self, child: Directory):
        self.children.append(child)

    def add_file(self, file_size: int):
        self.size += file_size

    def get_size(self):
        if self.is_final_size == False:
            output = 0
            for child in self.children:
                output += child.get_size()
            self.size += output
            self.is_final_size = True
        return self.size
    
    def get_limited_size(self):
        LIMIT = 100000
        output = 0
        for child in self.children:
            output += child.get_limited_size()
        if self.get_size() > LIMIT:
            return output
        else:
            return self.get_size() + output

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise Exception("Unknown sub directory")

    def get_parent(self):
        return self.parent

    def get_smallest_size_above_limit(self, limit):
        if self.get_size() < limit:
            return INF
        else:
            smallest = self.get_size()
            for child in self.children:
                smallest_size = child.get_smallest_size_above_limit(limit)
                if smallest_size < smallest:
                    smallest = smallest_size
            return smallest

    def __repr__(self):
        return f"Directory: {self.name}"

def pre_process() -> Directory:
    root = Directory("/", None)
    current_dir = root
    file = read_input_file()
    lines = file.readlines()
    for line in lines:
        ins = line.split()
        if ins[0] == "$":
            if ins[1] == "cd":
                if ins[2] == "/":
                    current_dir = root
                elif ins[2] == "..":
                    current_dir = current_dir.get_parent()
                else:
                    current_dir = current_dir.get_child(ins[2])
            elif ins[1] == "ls":
                pass
            else:
                raise Exception(f"Unknown command {ins[1]}")
        elif ins[0] == "dir":
            current_dir.add_children(Directory(ins[1], current_dir))
        else:
            current_dir.add_file(int(ins[0]))

    return root

def solve_part_1():
    root = pre_process()
    return root.get_limited_size()

def solve_part_2():
    root = pre_process()
    required_size = root.get_size() - 40000000
    return root.get_smallest_size_above_limit(required_size)

print(solve_part_2())