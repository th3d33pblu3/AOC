def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def seat_to_id(seat):
    row = seat[:7]
    col = seat[7:]
    row = row.replace("F", "0")
    row = row.replace("B", "1")
    col = col.replace("L", "0")
    col = col.replace("R", "1")
    row = int(row, 2)
    col = int(col, 2)
    return row * 8 + col

def solve_part_1():
    highest_id = 0
    for line in read_input_file_data().splitlines():
        id = seat_to_id(line)
        highest_id = max(highest_id, id)
    return highest_id

def solve_part_2():
    ids = set()
    for line in read_input_file_data().splitlines():
        id = seat_to_id(line)
        ids.add(id)
    for my_id in range(935):
        if my_id not in ids and my_id - 1 in ids and my_id + 1 in ids:
            return my_id
    
print(solve_part_2())
