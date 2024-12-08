from __future__ import annotations
from copy import deepcopy

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def read_test_file_data():
    FILE = "test_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

class Column:

    COLUMN_WIDTH = 7
    LEFTMOST_INDEX = 0
    RIGHTMOST_INDEX = COLUMN_WIDTH - 1
    BOTTOM_LAYER_INDEX = 0

    def _combine_into_range(ranges: list, value: int):
        ranges_that_matter = []
        for range_min, range_max in ranges:
            if range_min - 1 == value or range_max + 1 == value:
                ranges_that_matter.append((range_min, range_max))
        if len(ranges_that_matter) == 0: # value not close to any range
            ranges.append((value, value))
        elif len(ranges_that_matter) == 1: # value close to 1 range
            ranges.remove(ranges_that_matter[0])
            range_min, range_max = ranges_that_matter[0]
            ranges.append((min(range_min, value), max(range_max, value)))
        elif len(ranges_that_matter) == 2: # value close to 2 ranges
            ranges.remove(ranges_that_matter[0])
            ranges.remove(ranges_that_matter[1])
            range_1_min, range_1_max = ranges_that_matter[0]
            range_2_min, range_2_max = ranges_that_matter[1]
            new_range = (min(range_1_min, range_2_min), max(range_1_max, range_2_max))
            assert new_range[0] < value < new_range[1]
            ranges.append(new_range)
        else:
            raise Exception(f"Unexpected number of touching ranges touching {value}: {ranges_that_matter}")



    def __init__(self):
        self.heights = [0] * Column.COLUMN_WIDTH
        self.column_fillings = []
        for _ in range(Column.COLUMN_WIDTH):
            self.column_fillings.append([])
        
        self.jet_directions = read_input_file_data()
        self.LEN_JET_DIRECTIONS = len(self.jet_directions)
        self.jet_dir_index = 0
        self.rock_dropper = RockDropper()

    def drop_a_rock(self):
        appear_x = Column.LEFTMOST_INDEX + 2
        appear_y = self.get_max_height() + 1 + 3
        rock = self.rock_dropper.get_next_rock(appear_x, appear_y)
        while not rock.is_resting():
            jet_dir = self.jet_directions[self.jet_dir_index]
            self.jet_dir_index = (self.jet_dir_index + 1) % self.LEN_JET_DIRECTIONS
            rock.move(jet_dir, self)
        self.update_coordinates(rock)

    def get_max_height(self):
        return max(self.heights)

    def update_coordinates(self, rock: Rocks):
        coordinates = rock.get_coordinates()
        for x, y in coordinates:
            self.heights[x] = max(self.heights[x], y)
            Column._combine_into_range(self.column_fillings[x], y)
        self._optimize_filling_ranges()
        
    def _optimize_filling_ranges(self):
        min_height = min(self.heights) - 20
        for col_num in range(Column.COLUMN_WIDTH):
            self.column_fillings[col_num] = list(filter(lambda range: range[1] >= min_height, self.column_fillings[col_num]))
    
    def is_movable_coordinate(self, coordinate):
        x, y = coordinate
        if x < Column.LEFTMOST_INDEX or x > Column.RIGHTMOST_INDEX:
            return False
        elif y <= Column.BOTTOM_LAYER_INDEX:
            return False
        else:
            for range_min, range_max in self.column_fillings[x]:
                if range_min <= y <= range_max:
                    return False
            return True

class RockDropper:

    NUM_ROCK_TYPES = 5

    def __init__(self):
        self.next_rock_type = 0

    def get_next_rock(self, appear_x, appear_y) -> Rocks:
        if self.next_rock_type == 0:
            self.next_rock_type = (self.next_rock_type + 1) % 5
            return Rock0(appear_x, appear_y)
        elif self.next_rock_type == 1:
            self.next_rock_type = (self.next_rock_type + 1) % 5
            return Rock1(appear_x, appear_y)
        elif self.next_rock_type == 2:
            self.next_rock_type = (self.next_rock_type + 1) % 5
            return Rock2(appear_x, appear_y)
        elif self.next_rock_type == 3:
            self.next_rock_type = (self.next_rock_type + 1) % 5
            return Rock3(appear_x, appear_y)
        elif self.next_rock_type == 4:
            self.next_rock_type = (self.next_rock_type + 1) % 5
            return Rock4(appear_x, appear_y)
        else:
            raise Exception(f"Wrong rock type: {self.next_rock_type}")

class Rocks:
    def __init__(self, appear_x, appear_y):
        self.is_rest = False
        self.coordinates = []

    def move(self, dir, column: Column):
        if dir == "<":
            self._move_left(column)
        elif dir == ">":
            self._move_right(column)
        else:
            raise Exception(f"Unexpected move direction: {dir}")
        self._move_down(column)

    def _move_right(self, column: Column):
        for coordinate in self.coordinates:
            x, y = coordinate
            if not column.is_movable_coordinate((x + 1, y)):
                return
        for coordinate in self.coordinates:
            coordinate[0] += 1

    def _move_left(self, column: Column):
        for coordinate in self.coordinates:
            x, y = coordinate
            if not column.is_movable_coordinate((x - 1, y)):
                return
        for coordinate in self.coordinates:
            coordinate[0] -= 1

    def _move_down(self, column: Column):
        for coordinate in self.coordinates:
            x, y = coordinate
            if not column.is_movable_coordinate((x, y - 1)):
                self.is_rest = True
                return
        for coordinate in self.coordinates:
            coordinate[1] -= 1

    def is_resting(self):
        return self.is_rest

    def get_coordinates(self):
        return self.coordinates
    
class Rock0(Rocks):
    """
    [#]# # #
    """
    def __init__(self, appear_x, appear_y):
        self.is_rest = False
        self.coordinates = []
        for x in range(4):
            self.coordinates.append([appear_x + x, appear_y])

class Rock1(Rocks):
    """
       #
     # # #
    [ ]#
    """
    def __init__(self, appear_x, appear_y):
        self.is_rest = False
        self.coordinates = []
        center = [appear_x + 1, appear_y + 1]
        self.coordinates.append(center)
        for x_change in (-1, 1):
            self.coordinates.append([center[0] + x_change, center[1]           ])
        for y_change in (-1, 1):
            self.coordinates.append([center[0],            center[1] + y_change])

class Rock2(Rocks):
    """
         #
         #
    [#]# #
    """
    def __init__(self, appear_x, appear_y):
        self.is_rest = False
        self.coordinates = []
        corner = [appear_x + 2, appear_y]
        self.coordinates.append(corner)
        for x_change in (-2, -1):
            self.coordinates.append([corner[0] + x_change, corner[1]           ])
        for y_change in (1, 2):
            self.coordinates.append([corner[0],            corner[1] + y_change])

class Rock3(Rocks):
    """
     #
     #
     #
    [#]
    """
    def __init__(self, appear_x, appear_y):
        self.is_rest = False
        self.coordinates = []
        for y in range(4):
            self.coordinates.append([appear_x, appear_y + y])

class Rock4(Rocks):
    """
     # #
    [#]#
    """
    def __init__(self, appear_x, appear_y):
        self.is_rest = False
        self.coordinates = []
        for x in range(2):
            for y in range(2):
                self.coordinates.append([appear_x + x, appear_y + y])

def solve_part_1():
    ROCK_RESTING_LIMIT = 2022
    rocks_resting = 0
    column = Column()

    while rocks_resting < ROCK_RESTING_LIMIT:
        column.drop_a_rock()
        rocks_resting += 1
    
    return column.get_max_height()

def get_indices(seen, element): # Time complexity: O(n)
    indices = []
    for i in range(len(seen)):
        if seen[i] == element:
            indices.append(i)
    return indices

def solve_part_2():
    ROCK_RESTING_LIMIT = 1000000000000
    rocks_resting = 0
    column = Column()

    # Loop: When directions of the jets of air and next rock dropped are back to initial state
    # LOOP_SIZE = column.LEN_JET_DIRECTIONS * RockDropper.NUM_ROCK_TYPES
    LOOP_SIZE = RockDropper.NUM_ROCK_TYPES

    # Complete loop: Loop until height increments are the same again.
    heights_inc_in_loops = []
    heights_inc_in_loops_counter = dict()

    is_complete_loop_found = False
    complete_loop_size = None
    complete_loop_heights_inc = None

    # Finding max height after required number of rocks are resting
    while rocks_resting < ROCK_RESTING_LIMIT:
        # Do a loop
        prev_heights = deepcopy(column.heights)
        for _ in range(LOOP_SIZE):
            column.drop_a_rock()
        rocks_resting += LOOP_SIZE
        # print(f"Current rocks resting: {rocks_resting}")

        ### Debugging ==========================
        # heights = deepcopy(column.heights)
        # min_h = min(heights)
        # for i in range(column.COLUMN_WIDTH):
        #     heights[i] -= min_h
        # print(heights)
        ### ====================================

        # Keep track of loop increments
        h_inc = tuple(column.heights[i] - prev_heights[i] for i in range(column.COLUMN_WIDTH))
        heights_inc_in_loops.append(h_inc)
        if heights_inc_in_loops_counter.get(h_inc) != None:
            heights_inc_in_loops_counter[h_inc] += 1
        else:
            heights_inc_in_loops_counter[h_inc] = 1
        prev_heights = deepcopy(column.heights)

        # Check if complete loop occurs
        if heights_inc_in_loops_counter.get(h_inc) >= 3: # Ignore first occurrence, we need 2 more occurrences to compare with.
            indices_of_h_inc = get_indices(heights_inc_in_loops, h_inc)
            #  0: First occurrence (ignore)
            #  x: End of loop 1
            # -1: End of loop 2
            for x in indices_of_h_inc[1: -1]:
                loop1_end_index = x
                loop2_end_index = indices_of_h_inc[-1]
                loop_length = loop2_end_index - loop1_end_index
                loop1_start_index = loop1_end_index + 1 - loop_length
                loop2_start_index = loop1_end_index + 1

                is_same_loop = True
                for i in range(loop_length):
                    if heights_inc_in_loops[loop1_start_index + i] != heights_inc_in_loops[loop2_start_index + i]:
                        is_same_loop = False
                        break
                if is_same_loop:
                    is_complete_loop_found = True
                    complete_loop_size = LOOP_SIZE * loop_length

                    total_heights_increase = [0] * column.COLUMN_WIDTH
                    for i in range(loop_length):
                        heights_increase = heights_inc_in_loops[loop1_start_index + i]
                        for col in range(column.COLUMN_WIDTH):
                            total_heights_increase[col] += heights_increase[col]
                    complete_loop_heights_inc = tuple(total_heights_increase)
                    break

        if is_complete_loop_found: # At this stage, we just completed a complete loop.
            # print("Complete loop found.")
            remaining_rocks = ROCK_RESTING_LIMIT - rocks_resting
            num_complete_loops_remaining = remaining_rocks // complete_loop_size
            num_rocks_to_rest_after_complete_loops = remaining_rocks % complete_loop_size

            # Finish dropping rocks that remain after complete loops
            for _ in range(num_rocks_to_rest_after_complete_loops):
                column.drop_a_rock()
            rocks_resting += num_rocks_to_rest_after_complete_loops

            # Find the heights to increase by the remaining complete loops
            complete_loops_heights_to_increase = []
            for col in range(column.COLUMN_WIDTH):
                complete_loops_heights_to_increase.append(complete_loop_heights_inc[col] * num_complete_loops_remaining)

            final_heights = []
            for col in range(column.COLUMN_WIDTH):
                final_heights.append(complete_loops_heights_to_increase[col] + column.heights[col])

            return max(final_heights)
    
    return max(column.heights)
    
print(solve_part_2())

# def test():
#     x = [1, 2, 3, 4, 5 ,6]
#     print(x[1 : -1])

# test()
