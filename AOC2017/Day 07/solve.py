from __future__ import annotations
from collections import Counter

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    names = set()
    supported = set()
    for line in file.read().splitlines():
        segments = line.split(" -> ")
        name = segments[0].split()[0]
        # weight = int(segments[0].split()[1][1:-1])
        names.add(name)
        if len(segments) == 1:
            continue
        supported_names = segments[1].split(", ")
        supported.update(supported_names)
    return names.difference(supported) # eqgvf

class Disc:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.supporting_weight = 0
        self.supporting = []
        self.is_done_get_weight = False

    def set_weight(self, weight):
        self.weight = weight
    
    def add_supporting(self, disc: Disc):
        self.supporting.append(disc)

    def get_weight(self):
        if self.is_done_get_weight:
            return self.weight + self.supporting_weight
        for disc in self.supporting:
            self.supporting_weight += disc.get_weight()
    
        self.is_done_get_weight = True
        return self.weight + self.supporting_weight

    def get_different_weight(self):
        weights = []
        for support in self.supporting:
            weights.append(support.get_weight())
        counter = Counter(weights)
        if len(counter) == 1:
            return None
        odd_weight = counter.most_common(2)[1][0]
        diff_support = None
        for support in self.supporting:
            if support.get_weight() == odd_weight:
                diff_support = support
                break
        
        is_diff_weight = diff_support.get_different_weight()
        if is_diff_weight == None:
            diff = counter.most_common(1)[0][0] - odd_weight
            disc_weight = diff_support.weight
            return disc_weight + diff
        else:
            return is_diff_weight


def solve_part_2():
    file = read_input_file()
    names = {}
    for line in file.read().splitlines():
        segments = line.split(" -> ")
        name = segments[0].split()[0]
        weight = int(segments[0].split()[1][1:-1])
        if names.get(name) == None:
            names[name] = Disc(name, weight)
        elif names.get(name).weight == None:
            names.get(name).set_weight(weight)
        if len(segments) == 1:
            continue
        disc = names.get(name)
        supported_names = segments[1].split(", ")
        for supported_name in supported_names:
            if names.get(supported_name) == None:
                names[supported_name] = Disc(supported_name, None)
            disc.add_supporting(names.get(supported_name))
    root = names.get("eqgvf")
    return root.get_different_weight()
    
print(solve_part_2())
