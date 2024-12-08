import json

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_input_file_data():
    data = json.loads(read_input_file_data())
    return data

def solve_part_1():
    def summer(data):
        if data == None:
            return 0
        if type(data) == list:
            sums = list(map(lambda x: summer(x), data))
            return sum(sums)
        if type(data) == dict:
            sums = list(map(lambda x: summer(x), data.values()))
            return sum(sums)
        if type(data) == str:
            return 0
        if type(data) == int:
            return data

    data = parse_input_file_data()
    return summer(data)

def solve_part_2():
    def summer(data):
        if data == None:
            return 0
        if type(data) == list:
            sums = list(map(lambda x: summer(x), data))
            return sum(sums)
        if type(data) == dict:
            if "red" in data.values():
                return 0
            sums = list(map(lambda x: summer(x), data.values()))
            return sum(sums)
        if type(data) == str:
            return 0
        if type(data) == int:
            return data
        
    data = parse_input_file_data()
    return summer(data)

    
print(solve_part_2())
