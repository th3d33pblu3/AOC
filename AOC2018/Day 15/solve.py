def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

GOBLIN = 'G'
ELF = 'E'
WALL = '#'
EMPTY = '.'

class Unit:
    goblins = {}
    elves = {}
    battlefield = []

    def __init__(self, type, id, pos, atk, hp):
        self.type = type
        self.id = id
        self.pos = pos # (row, col)
        self.atk = atk
        self.hp = hp
        self.enemy = ELF if type == GOBLIN else ELF
        if type == GOBLIN:
            Unit.goblins[pos] = self
        else:
            Unit.elves[pos] = self

    def perform_action(self):
        enemy_type = GOBLIN if self.type == ELF else ELF
        enemies = Unit.goblins if self.type == ELF else Unit.elves
        deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        in_range_positions = [(self.pos[0] + i, self.pos[1] + j) for (i, j) in deltas]

        # If there is enemy in range, attack
        enemy_options = []
        for (row, col) in in_range_positions:
            if Unit.battlefield[row][col] == enemy_type:
                enemy_options.append(enemies[(row, col)])
        
        if len(enemy_options) != 0:
            target_enemy = enemy_options[0]
            for possible_enemy in enemy_options[1:]:
                if possible_enemy.hp < target_enemy.hp: # already sorted in reading order, so only need to compare hp
                    target_enemy = possible_enemy
            self.attack(target_enemy)
        else: # No enemy in range, move to nearest available location
            all_flooded_pos = { self.pos: self.pos } # add self into flooded pos
            frontier = []
            for (row, col) in in_range_positions:
                all_flooded_pos[(row, col)] = self.pos # all initial in range directions to self from self position
                if Unit.battlefield[row][col] == EMPTY:
                    frontier.append((row, col))
            
            # Find the grids to go to
            nearest_reachable_enemies = {} # enemy_reachable_pos : enemy
            found_enemy = False
            while frontier and not found_enemy:
                new_frontier = []
                for (row, col) in frontier:
                    for (i, j) in deltas:
                        if (row + i, col + j) not in all_flooded_pos: # a position not seen before
                            all_flooded_pos[(row + i, col + j)] = (row, col)
                            if Unit.battlefield[row + i][col + j] == EMPTY:
                                new_frontier.append((row + i, col + j))
                            elif Unit.battlefield[row + i][col + j] == enemy_type: # current grid can reach enemy
                                found_enemy = True
                                nearest_reachable_enemies[(row, col)] = enemies[(row + i, col + j)]
                frontier = new_frontier
            
            if nearest_reachable_enemies:
                reachable_positions = list(nearest_reachable_enemies.keys())
                reachable_positions.sort()
                target_position = reachable_positions[0]
                while target_position not in in_range_positions:
                    target_position = all_flooded_pos[target_position]
                self.move(target_position)

    def attack(self, enemy):
        enemy.hp -= self.atk
        # print(f"{"Elf" if self.type == ELF else "Goblin"} {self.id} attacked {"Elf" if enemy.type == ELF else "Goblin"} {enemy.id} with {self.atk} ATK, enemy now has {enemy.hp} HP")
        if enemy.hp <= 0: # enemy dead
            # print(f"{"Elf" if enemy.type == ELF else "Goblin"} {enemy.id} died!")
            enemies = Unit.goblins if self.type == ELF else Unit.elves
            enemies.pop(enemy.pos) # remove enemy from active unit list
            Unit.battlefield[enemy.pos[0]][enemy.pos[1]] = EMPTY # remove enemy from battlefield

    def move(self, new_pos: tuple): # (row, col)
        # Update in battlefield
        Unit.battlefield[self.pos[0]][self.pos[1]] = EMPTY
        Unit.battlefield[new_pos[0]][new_pos[1]] = self.type
        # Updeate in units list
        allies = Unit.elves if self.type == ELF else Unit.goblins
        allies.pop(self.pos)
        allies[new_pos] = self
        # Update self
        self.pos = new_pos
        # print(f"{"Elf" if self.type == ELF else "Goblin"} {self.id} moved to {new_pos}")

        # If there are enemies in range after moving, attack
        enemy_type = GOBLIN if self.type == ELF else ELF
        enemies = Unit.goblins if self.type == ELF else Unit.elves
        deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        in_range_positions = [(self.pos[0] + i, self.pos[1] + j) for (i, j) in deltas]

        # If there is enemy in range, attack
        enemy_options = []
        for (row, col) in in_range_positions:
            if Unit.battlefield[row][col] == enemy_type:
                enemy_options.append(enemies[(row, col)])
        
        if len(enemy_options) != 0:
            target_enemy = enemy_options[0]
            for possible_enemy in enemy_options[1:]:
                if possible_enemy.hp < target_enemy.hp: # already sorted in reading order, so only need to compare hp
                    target_enemy = possible_enemy
            self.attack(target_enemy)

class Goblin(Unit):
    def __init__(self, id, pos, atk=3, hp=200):
        super().__init__(GOBLIN, id, pos, atk, hp)

    def __repr__(self):
        return f"Goblin {self.id} @ {self.pos} with {self.hp} HP"

class Elf(Unit):
    def __init__(self, id, pos, atk=3, hp=200):
        super().__init__(ELF, id, pos, atk, hp)
    
    def __repr__(self):
        return f"Elf {self.id} @ {self.pos} with {self.hp} HP"

def process_data(data, elf_atk=3):
    battlefield = data
    for i in range(len(battlefield)):
        battlefield[i] = list(data[i])
    Unit.battlefield = battlefield
    
    Unit.goblins = {}
    Unit.elves = {}

    id = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == GOBLIN:
                Goblin(id, (row, col))
                id += 1
            elif data[row][col] == ELF:
                Elf(id, (row, col), elf_atk)
                id += 1

def calculate_outcome(round):
    remaining_units = [*Unit.goblins.values(), *Unit.elves.values()]
    total_hp = sum(map(lambda u: u.hp, remaining_units))
    print(f"Completed rounds: {round}\nTotal HP remaining: {total_hp}")
    return round * total_hp

def solve_part_1():
    data = read_input_file_data()
    data = data.splitlines()
    process_data(data)

    round = 0
    while Unit.goblins and Unit.elves:
        units = [*Unit.goblins.values(), *Unit.elves.values()]
        units.sort(key=lambda u: u.pos)

        for unit in units:
            unit: Unit
            if unit.hp > 0: # Units that died in the round should not perform actions
                if not Unit.goblins or not Unit.elves: # If this unit is alive yet other group dies out, end and calculate outcome immediately
                    return calculate_outcome(round)
                unit.perform_action()
        round += 1 # count complete rounds

        # print(f"After {round} rounds")
        # for row in Unit.battlefield:
        #     print(''.join(row))
        # units.sort(key=lambda u: u.pos)
        # print(units)

    return calculate_outcome(round)

def initialize_with_elf_atk(atk):
    data = read_input_file_data()
    data = data.splitlines()
    battlefield = data
    for i in range(len(battlefield)):
        battlefield[i] = list(data[i])
    Unit.battlefield = battlefield

    Unit.goblins = {}
    Unit.elves = {}

    id = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == GOBLIN:
                Goblin(id, (row, col))
                id += 1
            elif data[row][col] == ELF:
                Elf(id, (row, col), atk)
                id += 1

def simulate_combat_result():
    initial_elves_count = len(Unit.elves)
    while Unit.goblins and len(Unit.elves) == initial_elves_count:
        units = [*Unit.goblins.values(), *Unit.elves.values()]
        units.sort(key=lambda u: u.pos)

        for unit in units:
            unit: Unit
            if unit.hp > 0: # Units that died in the round should not perform actions
                if not Unit.goblins or not Unit.elves: # If this unit is alive yet other group dies out, end and calculate outcome immediately
                    return len(Unit.elves) == initial_elves_count
                unit.perform_action()

    return len(Unit.elves) == initial_elves_count

def find_atk_required():
    low = 3
    high = 200
    while high - low > 1:
        mid = (high + low) // 2
        # print(f"Simulating with low: {low}, high: {high}, mid: {mid}")
        initialize_with_elf_atk(mid)
        is_all_elves_survive = simulate_combat_result()
        # print(f"Result: {is_all_elves_survive}")
        if is_all_elves_survive:
            high = mid
        else:
            low = mid
    print(f"Elves require an attack of {high}")
    return high

def solve_part_2():
    elf_atk_required = find_atk_required()

    data = read_input_file_data()
    data = data.splitlines()
    process_data(data, elf_atk_required)

    round = 0
    while Unit.goblins and Unit.elves:
        units = [*Unit.goblins.values(), *Unit.elves.values()]
        units.sort(key=lambda u: u.pos)

        for unit in units:
            unit: Unit
            if unit.hp > 0: # Units that died in the round should not perform actions
                if not Unit.goblins or not Unit.elves: # If this unit is alive yet other group dies out, end and calculate outcome immediately
                    return calculate_outcome(round)
                unit.perform_action()
        round += 1 # count complete rounds

        # print(f"After {round} rounds")
        # for row in Unit.battlefield:
        #     print(''.join(row))
        # units.sort(key=lambda u: u.pos)
        # print(units)

    return calculate_outcome(round)
    
print(solve_part_2())
