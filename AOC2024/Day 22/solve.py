from collections import deque
from tqdm import tqdm
import time

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    def mix(a, b):
        return a ^ b
    def prune(a):
        return a % 16777216
    def evolve(a):
        a = prune(mix(a * 64, a))
        a = prune(mix(a // 32, a))
        a = prune(mix(a * 2048, a))
        return a
    def evolve_str_2000(a):
        a = int(a)
        for _ in range(2000):
            a = evolve(a)
        return a
    return sum(list(map(evolve_str_2000, read_input_file_data().splitlines())))

# def solve_part_2():
#     NUM_LIMIT = 2000
#     def evolve(a):
#         a = ((a * 64) ^ a) % 16777216
#         a = ((a // 32) ^ a) % 16777216
#         a = ((a * 2048) ^ a) % 16777216
#         return a
#     def predict_str(a):
#         a = int(a)
#         nums = deque((a % 10,))
#         for _ in range(NUM_LIMIT):
#             a = evolve(a)
#             nums.appendleft(a % 10)
#         nums = list(nums)
#         nums.reverse()
#         return nums
#     def get_diffs(nums):
#         return [nums[i+1] - nums[i] for i in range(NUM_LIMIT)]
#     def get_diff_indices(diffs):
#         indices = {}
#         for n in range(-9, 10):
#             indices[n] = set()
#         for i in range(NUM_LIMIT):
#             indices[diffs[i]].add(i)
#         return indices
    
#     # def get_valid_changes(): # 21000 (excluding decreasing sequences)
#     #     valid_changes = set()
#     #     for a in range(-9, 10):
#     #         for b in range(-9, 10):
#     #             if a + b < -9 or a + b > 9:
#     #                 continue
#     #             for c in range(-9, 10):
#     #                 if a + b + c < -9 or a + b + c > 9:
#     #                     continue
#     #                 for d in range(1, 10):
#     #                     if a + b + c + d < 0 or a + b + c + d > 9:
#     #                         continue
#     #                     valid_changes.add((a, b, c, d))
#     #     return valid_changes
    
#     # def get_valid_changes(): # 3033 (with possible missing)
#     #     valid_changes = set()
#     #     for a in range(-3, 5):
#     #         for b in range(-3, 5):
#     #             if a + b < -9 or a + b > 9:
#     #                 continue
#     #             for c in range(-3, 5):
#     #                 if a + b + c < -9 or a + b + c > 9:
#     #                     continue
#     #                 for d in range(1, 10):
#     #                     if a + b + c + d < 0 or a + b + c + d > 9:
#     #                         continue
#     #                     valid_changes.add((a, b, c, d))
#     #     return valid_changes
    
#     def get_valid_changes(): # 40951
#         valid_changes = set()
#         for monkey_diff in monkey_diffs:
#             for i in range(NUM_LIMIT-3):
#                 valid_changes.add(tuple(monkey_diff[i:i+4]))
#         return valid_changes
    
#     # def get_monkey_bananas(m, changes):
#     #     nums, diffs = monkey_nums[m], monkey_diffs[m]
#     #     for i in range(NUM_LIMIT-3):
#     #         if changes == diffs[i:i+4]:
#     #             return nums[i]
#     #     return 0
    
#     # def get_monkey_bananas(m, changes): # Better optimized
#     #     nums, diffs, diff_indices = monkey_nums[m], monkey_diffs[m], monkey_diff_indices[m]
#     #     min_i = NUM_LIMIT
#     #     for i in diff_indices[changes[0]]:
#     #         if i > NUM_LIMIT-4:
#     #             continue
#     #         if diffs[i:i+4] == changes:
#     #             if i < min_i:
#     #                 min_i = i
#     #     return 0 if min_i == NUM_LIMIT else nums[min_i]
    
#     def get_monkey_bananas(m, changes): # Even better optimized
#         nums, diffs, diff_indices = monkey_nums[m], monkey_diffs[m], monkey_diff_indices[m]
#         min_i = NUM_LIMIT
#         for i in diff_indices[changes[0]]:
#             if i > NUM_LIMIT-4:
#                 continue
#             if diffs[i:i+4] == changes:
#                 if i < min_i:
#                     min_i = i
#         return 0 if min_i == NUM_LIMIT else nums[min_i]
    
#     monkey_nums = list(map(predict_str, read_input_file_data().splitlines()))
#     monkey_diffs = [get_diffs(num) for num in monkey_nums]
#     monkey_diff_indices = [get_diff_indices(diff) for diff in monkey_diffs]
#     valid_changes = get_valid_changes()

#     NUM_MONKEYS = len(monkey_nums)
#     max_bananas = 0
#     for change in tqdm(valid_changes):
#         change = list(change)
#         bananas = 0
#         for m in range(NUM_MONKEYS):
#             bananas += get_monkey_bananas(m, change)
#         if bananas > max_bananas:
#             max_bananas = bananas
    
#     return max_bananas

def solve_part_2():
    NUM_LIMIT = 2000
    def evolve(a):
        a = ((a * 64) ^ a) % 16777216
        a = ((a // 32) ^ a) % 16777216
        a = ((a * 2048) ^ a) % 16777216
        return a
    def predict_str(a):
        a = int(a)
        nums = deque((a % 10,))
        for _ in range(NUM_LIMIT):
            a = evolve(a)
            nums.appendleft(a % 10)
        nums = list(nums)
        nums.reverse()
        return nums
    def get_diffs(nums):
        return [nums[i+1] - nums[i] for i in range(NUM_LIMIT)]
    
    # def get_valid_changes():
    #     valid_changes = set()
    #     for m in range(NUM_MONKEYS):
    #         valid_changes.update(set(monkey_change_bananas[m].keys()))
    #     return valid_changes

    def get_valid_changes(): # 21000 (excluding decreasing sequences) (use the commented method above for more accurate answer)
        valid_changes = set()
        for a in range(-9, 10):
            for b in range(-9, 10):
                if a + b < -9 or a + b > 9:
                    continue
                for c in range(-9, 10):
                    if a + b + c < -9 or a + b + c > 9:
                        continue
                    for d in range(1, 10):
                        if a + b + c + d < 0 or a + b + c + d > 9:
                            continue
                        valid_changes.add((a, b, c, d))
        return valid_changes
    
    def get_monkey_change_bananas(m):
        nums, diffs = monkey_nums[m], monkey_diffs[m]
        change_bananas = {}
        for i in range(4, NUM_LIMIT):
            change = tuple(diffs[i-4:i])
            if change not in change_bananas:
                change_bananas[change] = nums[i]
        return change_bananas

    
    monkey_nums = list(map(predict_str, read_input_file_data().splitlines()))
    NUM_MONKEYS = len(monkey_nums)
    monkey_diffs = [get_diffs(num) for num in monkey_nums]
    monkey_change_bananas = [get_monkey_change_bananas(m) for m in range(NUM_MONKEYS)]
    valid_changes = get_valid_changes()
    
    max_bananas = 0
    best_change = None
    for change in tqdm(valid_changes):
        bananas = 0
        for m in range(NUM_MONKEYS):
            if change in monkey_change_bananas[m]:
                bananas += monkey_change_bananas[m][change]
        if bananas > max_bananas:
            max_bananas = bananas
            best_change = change
    
    print(best_change)
    return max_bananas

print(solve_part_2())
