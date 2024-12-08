import re
from math import prod
from queue import Queue

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

part = tuple[int, int, int, int] # x, m, a, s
ranges = list[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int], str]
START = 'in'
REJECT = 'R'
ACCEPT = 'A'

class Condition():
    def __init__(self, condition: tuple):
        self.condition = condition

    def apply(self, p: part) -> str:
        if len(self.condition) == 1: # Directly send to R or A
            return self.condition[0]
        # part index 0-3, < or >, condition value, next_directory
        if self.condition[1] == '<':
            if p[self.condition[0]] < self.condition[2]:
                return self.condition[3]
            return None
        else:
            if p[self.condition[0]] > self.condition[2]:
                return self.condition[3]
            return None
        
    def apply_range(self, r: ranges) -> tuple[ranges, ranges]: # True ranges, False ranges
        if len(self.condition) == 1: # Directly send to R or A
            r[4] = self.condition[0]
            return (r, None)
        i, c, v, n = self.condition
        x1, x2 = r[i]
        if c == '<':
            # [---)
            # <
            # All True
            if v <= x1:
                r1 = None
                r2 = r
            # [---)
            #   <
            elif v > x1 and v < x2:
                r1 = r
                r2 = r.copy()
                r1[i] = (x1, v)
                r1[4] = n
                r2[i] = (v, x2)
            # [---)
            #     <
            # All False
            elif v >= x2:
                r1 = r
                r1[4] = n
                r2 = None
        else:
            # [---)
            #    >
            # All False
            if v >= x2 - 1:
                r1 = None
                r2 = r
            # [---)
            #   >
            elif v >= x1 and v < x2 - 1:
                r1 = r
                r2 = r.copy()
                r1[i] = (v + 1, x2)
                r1[4] = n
                r2[i] = (x1, v + 1)
            #  [---)
            # >
            # All True
            elif v < x1:
                r1 = r
                r1[4] = n
                r2 = None
        return (r1, r2)
        
    def __str__(self) -> str:
        return str(self.condition)
        
class Workflow():
    def __init__(self, conditions: list[Condition]):
        self.conditions = conditions
    
    def apply_conditions(self, p: part) -> str:
        for condition in self.conditions:
            r = condition.apply(p)
            if r != None:
                return r
        raise Exception("Full reject condition in workflow")
    
    def apply_range_conditions(self, r: ranges) -> list[ranges]:
        output = []
        for condition in self.conditions:
            t, f = condition.apply_range(r)
            if t != None:
                output.append(t)
            if f != None:
                r = f
            else:
                break
        return output
    
    def __str__(self) -> str:
        return ' '.join(map(str, self.conditions))

def parse_data():
    CATS = {'x':0, 'm':1, 'a':2, 's':3}
    workflow_str, parts_str = read_input_file_data().split('\n\n')

    workflows = {}
    for workflow in workflow_str.splitlines():
        name = re.search(r'.*(?=\{)', workflow).group()
        flows: list[str] = re.findall(r'\{(.*?)\}', workflow)[0].split(',')
        conditions = []
        for flow in flows:
            if ':' not in flow:
                conditions.append(Condition((flow,)))
                continue
            condition, next_workflow = flow.split(':')
            cat = CATS[condition[0]]
            comp = condition[1]
            value = int(condition[2:])
            conditions.append(Condition((cat, comp, value, next_workflow)))
        workflows[name] = Workflow(conditions)
            
    parts = []
    for part in parts_str.splitlines():
        parts.append(tuple(map(int, re.findall(r'=([0-9]*)', part))))
    
    return workflows, parts

def solve_part_1():
    workflows, parts = parse_data()
    
    total = 0
    for p in parts:
        workflow: Workflow = workflows[START]
        r = workflow.apply_conditions(p)
        while r not in (ACCEPT, REJECT):
            workflow = workflows[r]
            r = workflow.apply_conditions(p)
        if r == ACCEPT:
            total += sum(p)
    return total

def solve_part_2():
    workflows, _ = parse_data()
    q = Queue()
    q.put([(1, 4001), (1, 4001), (1, 4001), (1, 4001), START])
    accepted = 0
    while not q.empty():
        r = q.get()
        name = r[4]
        if name == REJECT:
            continue
        if name == ACCEPT:
            accepted += prod([y - x for x, y in r[:-1]])
            continue
        workflow = workflows[name]
        new_rs = workflow.apply_range_conditions(r)
        for r in new_rs:
            q.put(r)
    return accepted
    
print(solve_part_2())
