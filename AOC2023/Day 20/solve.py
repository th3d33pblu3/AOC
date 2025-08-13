from abc import ABC, abstractmethod
from queue import Queue

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

LOW = False
HIGH = True
signal_command = tuple[str, bool, str]

class Module(ABC):
    low_count = 0
    high_count = 0

    def count_pulse(pulse: bool):
        if pulse: # HIGH
            Module.high_count += 1
        else:
            Module.low_count += 1

    @abstractmethod
    def process_signal(self, signal: signal_command) -> list[signal_command]:
        return

class FlipFlop(Module): # %
    def __init__(self, name: str, outputs: list[str]):
        self.name = name
        self.outputs = outputs
        self.state = False
    
    def process_signal(self, signal: signal_command) -> list[signal_command]:
        pulse = signal[1]
        if pulse: # HIGH pulse
            return []
        else: # LOW pulse
            # OFF -> ON sends HIGH (ON)
            # ON -> OFF sends LOW (OFF)
            self.state = not self.state
            return [(self.name, self.state, output_name) for output_name in self.outputs]

class Conjunction(Module): # &
    def __init__(self, name: str, inputs: list[str], outputs: list[str]):
        self.name = name
        self.outputs = outputs
        self.remembered = {key: False for key in inputs}

    def process_signal(self, signal: signal_command) -> list[signal_command]:
        pulse = signal[1]

        # Remember pulse
        from_input = signal[0]
        self.remembered[from_input] = pulse

        # Output HIGH if everything remembered is HIGH
        all_high = True
        for p in self.remembered.values():
            all_high &= p
        if all_high:
            return [(self.name, LOW, output_name) for output_name in self.outputs]
        else:
            return [(self.name, HIGH, output_name) for output_name in self.outputs]

class Broadcaster(Module): # broadcaster
    def __init__(self, name: str, outputs: list[str]):
        self.name = name
        self.outputs = outputs

    def process_signal(self, signal: signal_command) -> list[signal_command]:
        # Broadcast received pulse
        pulse = signal[1]
        return [(self.name, pulse, output_name) for output_name in self.outputs]

class Button():
    def press() -> signal_command:
        # Sends LOW pulse to broadcast
        return ('button', LOW, BROADCASTER)

FLIPFLOP = '%'
CONJUNCTION = '&'
BROADCASTER = 'broadcaster'
BUTTON = Button

def parse_modules() -> dict[str, Module]:
    types: dict[str, str] = {}
    inputs: dict[str, list[str]] = {}
    outputs: dict[str, list[str]] = {}
    for line in read_input_file_data().splitlines():
        type_name, output_names = line.split(' -> ')

        # Type handling
        t = type_name[0]
        if t == FLIPFLOP:
            name = type_name[1:]
            types[name] = FLIPFLOP
        elif t == CONJUNCTION:
            name = type_name[1:]
            types[name] = CONJUNCTION
        elif type_name == BROADCASTER:
            name = type_name
            types[name] = BROADCASTER
        else:
            raise Exception(f"Unknown module type name: {type_name}")

        # Input and Output handling
        output_names = output_names.split(', ')
        outputs[name] = output_names
        for output_name in output_names:
            if output_name not in inputs:
                inputs[output_name] = [name]
            else:
                inputs[output_name].append(name)
        
    # Module creation
    modules: dict[str, Module] = {}
    for name, t in types.items():
        if t == FLIPFLOP:
            modules[name] = FlipFlop(name, outputs[name])
        elif t == CONJUNCTION:
            modules[name] = Conjunction(name, inputs[name], outputs[name])
        elif t == BROADCASTER:
            modules[name] = Broadcaster(name, outputs[name])
        else:
            raise Exception(f"Unknown module type: {t}")
    return modules

# def print_signal(signal: signal_command):
#     if signal[1]: # HIGH
#         print(signal[0] + ' -high-> ' + signal[2])
#     else:
#         print(signal[0] + ' -low-> ' + signal[2])

def solve_part_1():
    modules = parse_modules()
    for _ in range(1000):
        # print(f"==============\nButton press: {_ + 1}\n==============")
        signals: Queue[signal_command] = Queue()
        signals.put(BUTTON.press())
        while not signals.empty():
            signal = signals.get()
            Module.count_pulse(signal[1])
            # print_signal(signal)
            module_name = signal[2]
            if module_name not in modules:
                continue
            module = modules[module_name]
            new_signals = module.process_signal(signal)
            for signal in new_signals:
                signals.put(signal)
    # print(Module.high_count, Module.low_count)
    return Module.high_count * Module.low_count

import math

def solve_part_2():
    modules = parse_modules()
    ft_dependency = ['vz', 'bq', 'qh', 'lt']
    frequencies = []
    presses = 0
    while ft_dependency:
        signals: Queue[signal_command] = Queue()
        signals.put(BUTTON.press())
        presses += 1
        while not signals.empty():
            signal = signals.get()
            pulse, module_name = signal[1], signal[2]
            if module_name in ft_dependency and pulse == LOW:
                frequencies.append(presses)
                ft_dependency.remove(module_name)
            if module_name not in modules:
                continue
            module = modules[module_name]
            new_signals = module.process_signal(signal)
            for signal in new_signals:
                signals.put(signal)
    
    return math.lcm(*frequencies)
    
print(solve_part_2())
