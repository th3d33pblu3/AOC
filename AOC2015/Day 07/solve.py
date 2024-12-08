from __future__ import annotations
from enum import Enum

MAX = 65535

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

class Component:
    components = {}

    def get_value(name):
        if (isinstance(Component.components.get(name), Component)):
            component = Component.components.get(name)
            val = component.get_value()
            Component.components[name] = val
            return val
        else:
            return Component.components.get(name)

    def put_component(name, val: Component):
        Component.components[name] = val

    def get_components():
        return Component.components

    def clear():
        Component.components = {}

class Wire(Component):
    def __init__(self, input: str):
        self.input = input
    
    def get_value(self):
        return Component.get_value(self.input)

    def __repr__(self):
        return f"Wire of input {self.input}"

class Operations(Enum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    LSHIFT = "LSHIFT"
    RSHIFT = "RSHIFT"

    def get_operation(op_str):
        if op_str == "AND":
            return Operations.AND
        elif op_str == "OR":
            return Operations.OR
        elif op_str == "NOT":
            return Operations.NOT
        elif op_str == "LSHIFT":
            return Operations.LSHIFT
        elif op_str == "RSHIFT":
            return Operations.RSHIFT
        else:
            raise Exception("Unknown operation: " + op_str)

class Gate(Component):
    def __init__(self, operation: Operations, input1: str, input2: str):
        self.operation = operation
        self.input1 = input1
        self.input2 = input2

    def apply_operation(self, value1, value2):
        if self.operation == Operations.AND:
            return value1 & value2
        elif self.operation == Operations.OR:
            return value1 | value2
        elif self.operation == Operations.NOT:
            return MAX - value1
        elif self.operation == Operations.LSHIFT:
            return value1 << value2
        elif self.operation == Operations.RSHIFT:
            return value1 >> value2
        else:
            raise Exception("Unknown operation application: " + self.operation)
    
    def get_value(self):
        value1 = Component.get_value(self.input1)
        value2 = Component.get_value(self.input2)
        return self.apply_operation(value1, value2)

    def __repr__(self):
        return f"{self.operation.value} Gate of inputs {self.input1}, {self.input2}"

class Literal(Component):
    def __init__(self, value: int):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def __repr__(self):
        return f"Literal of value {self.value}"

def setup():
    file = read_input_file()
    for line in file.read().splitlines():
        input_str, name = line.split(" -> ")
        inputs = input_str.split()
        if len(inputs) == 1:
            if inputs[0].isdigit():
                Component.put_component(inputs[0], Literal(int(inputs[0])))
            Component.put_component(name, Wire(inputs[0]))
        elif inputs[0] == Operations.NOT.value:
            if inputs[1].isdigit():
                Component.put_component(inputs[1], Literal(int(inputs[1])))
            Component.put_component(name, Gate(Operations.NOT, inputs[1], None))
        else:
            op = Operations.get_operation(inputs[1])
            if inputs[0].isdigit():
                Component.put_component(inputs[0], Literal(int(inputs[0])))
            if inputs[2].isdigit():
                Component.put_component(inputs[2], Literal(int(inputs[2])))
            Component.put_component(name, Gate(op, inputs[0], inputs[2]))

def solve_part_1():
    setup()
    return Component.get_value("a") # 16076

def solve_part_2():
    setup()
    a = Component.get_value("a")
    Component.clear()
    setup()
    Component.put_component("b", Literal(a))
    return Component.get_value("a")
    
print(solve_part_2())
