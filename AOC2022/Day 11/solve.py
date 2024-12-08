import math

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

class Monkey:
    def __init__(self):
        self.items = []
        self.business = 0

    def add_item(self, item):
        self.items.append(item)

    def get_business(self):
        return self.business
    
    def inspect(self):
        output = []
        for item in self.items:
            new_item = self.operation(item)
            new_monkey = self.test(new_item)
            output.append((new_monkey, new_item))
            self.business += 1
        self.items = []
        return output

    def operation(self, item):
        pass

    def test(self, item):
        pass

class Monkey0(Monkey):
    def operation(self, item):
        return math.floor((item * 7) / 3)
    
    def test(self, item):
        if (item % 17 == 0):
            return 5
        else:
            return 3

class Monkey1(Monkey):
    def operation(self, item):
        return math.floor((item + 4) / 3)
    
    def test(self, item):
        if (item % 3 == 0):
            return 0
        else:
            return 3

class Monkey2(Monkey):
    def operation(self, item):
        return math.floor((item + 2) / 3)
    
    def test(self, item):
        if (item % 5 == 0):
            return 7
        else:
            return 4

class Monkey3(Monkey):
    def operation(self, item):
        return math.floor((item + 7) / 3)
    
    def test(self, item):
        if (item % 7 == 0):
            return 5
        else:
            return 2

class Monkey4(Monkey):
    def operation(self, item):
        return math.floor((item * 17) / 3)
    
    def test(self, item):
        if (item % 11 == 0):
            return 1
        else:
            return 6

class Monkey5(Monkey):
    def operation(self, item):
        return math.floor((item + 8) / 3)
    
    def test(self, item):
        if (item % 19 == 0):
            return 2
        else:
            return 7

class Monkey6(Monkey):
    def operation(self, item):
        return math.floor((item + 6) / 3)
    
    def test(self, item):
        if (item % 2 == 0):
            return 0
        else:
            return 1

class Monkey7(Monkey):
    def operation(self, item):
        return math.floor((item * item) / 3)
    
    def test(self, item):
        if (item % 13 == 0):
            return 6
        else:
            return 4

def get_monkeys():
    monkeys = [Monkey0(), Monkey1(), Monkey2(), Monkey3(), 
               Monkey4(), Monkey5(), Monkey6(), Monkey7()]
    
    monkey_items = []
    monkey_items.append([54, 89, 94])
    monkey_items.append([66, 71])
    monkey_items.append([76, 55, 80, 55, 55, 96, 78])
    monkey_items.append([93, 69, 76, 66, 89, 54, 59, 94])
    monkey_items.append([80, 54, 58, 75, 99])
    monkey_items.append([69, 70, 85, 83])
    monkey_items.append([89])
    monkey_items.append([62, 80, 58, 57, 93, 56])

    monkey_num = 0
    for items in monkey_items:
        for item in items:
            monkeys[monkey_num].add_item(item)
        monkey_num += 1
    
    return monkeys

def solve_part_1():
    monkeys = get_monkeys()
    round = 1
    while round <= 20:
        for monkey in monkeys:
            new_items = monkey.inspect()
            for new_monkey, new_item in new_items:
                monkeys[new_monkey].add_item(new_item)
        round += 1
    
    monkey_business = []
    for monkey in monkeys:
        monkey_business.append(monkey.get_business())

    print(monkey_business)
    monkey_business.sort()
    return monkey_business[-1] * monkey_business[-2]

class NewMonkey:
    LCM = 9699690

    def __init__(self):
        self.items = []
        self.business = 0

    def add_item(self, item):
        self.items.append(item)

    def get_business(self):
        return self.business
    
    def inspect(self):
        output = []
        for item in self.items:
            new_item = self.operation(item) % NewMonkey.LCM
            new_monkey = self.test(new_item)
            output.append((new_monkey, new_item))
            self.business += 1
        self.items = []
        return output

    def operation(self, item):
        pass

    def test(self, item):
        pass

class NewMonkey0(NewMonkey):
    def operation(self, item):
        return item * 7
    
    def test(self, item):
        if (item % 17 == 0):
            return 5
        else:
            return 3

class NewMonkey1(NewMonkey):
    def operation(self, item):
        return item + 4
    
    def test(self, item):
        if (item % 3 == 0):
            return 0
        else:
            return 3

class NewMonkey2(NewMonkey):
    def operation(self, item):
        return item + 2
    
    def test(self, item):
        if (item % 5 == 0):
            return 7
        else:
            return 4

class NewMonkey3(NewMonkey):
    def operation(self, item):
        return item + 7
    
    def test(self, item):
        if (item % 7 == 0):
            return 5
        else:
            return 2

class NewMonkey4(NewMonkey):
    def operation(self, item):
        return item * 17
    
    def test(self, item):
        if (item % 11 == 0):
            return 1
        else:
            return 6

class NewMonkey5(NewMonkey):
    def operation(self, item):
        return item + 8
    
    def test(self, item):
        if (item % 19 == 0):
            return 2
        else:
            return 7

class NewMonkey6(NewMonkey):
    def operation(self, item):
        return item + 6
    
    def test(self, item):
        if (item % 2 == 0):
            return 0
        else:
            return 1

class NewMonkey7(NewMonkey):
    def operation(self, item):
        return item * item
    
    def test(self, item):
        if (item % 13 == 0):
            return 6
        else:
            return 4

def get_new_monkeys():
    monkeys = [NewMonkey0(), NewMonkey1(), NewMonkey2(), NewMonkey3(), 
               NewMonkey4(), NewMonkey5(), NewMonkey6(), NewMonkey7()]
    
    monkey_items = []
    monkey_items.append([54, 89, 94])
    monkey_items.append([66, 71])
    monkey_items.append([76, 55, 80, 55, 55, 96, 78])
    monkey_items.append([93, 69, 76, 66, 89, 54, 59, 94])
    monkey_items.append([80, 54, 58, 75, 99])
    monkey_items.append([69, 70, 85, 83])
    monkey_items.append([89])
    monkey_items.append([62, 80, 58, 57, 93, 56])

    monkey_num = 0
    for items in monkey_items:
        for item in items:
            monkeys[monkey_num].add_item(item)
        monkey_num += 1
    
    return monkeys

def solve_part_2():
    monkeys = get_new_monkeys()
    round = 1
    while round <= 10000:
        for monkey in monkeys:
            new_items = monkey.inspect()
            for new_monkey, new_item in new_items:
                monkeys[new_monkey].add_item(new_item)
        round += 1
    
    monkey_business = []
    for monkey in monkeys:
        monkey_business.append(monkey.get_business())

    print(monkey_business)
    monkey_business.sort()
    return monkey_business[-1] * monkey_business[-2]

print(solve_part_2())
