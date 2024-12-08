def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    groups = read_input_file_data().split("\n\n")
    total_yes_counts = 0
    for group in groups:
        total_yes_counts += len(set(group.replace("\n", "")))
    return total_yes_counts

def solve_part_2():
    groups = read_input_file_data().split("\n\n")
    total_all_yes_counts = 0
    for group in groups:
        ppl_answers = group.splitlines()
        sample = ppl_answers[0]

        all_yes_count = 0
        for char in sample:
            for other_answer in ppl_answers[1:]:
                if char not in other_answer:
                    break
            else:
                all_yes_count += 1

        total_all_yes_counts += all_yes_count
    return total_all_yes_counts
    
print(solve_part_2())
