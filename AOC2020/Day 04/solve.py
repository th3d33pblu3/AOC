import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    passports = read_input_file_data().split("\n\n")
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid_count = 0
    for passport in passports:
        for field in required_fields:
            if field + ":" not in passport:
                break
        else:
            valid_count += 1
        
    return valid_count


def solve_part_2():
    passports = read_input_file_data().split("\n\n")

    def valid_byr(passport):
        try:
            birth_year = re.search(r'byr:(\d{4})(?:$|\s)', passport).groups()[0]
            return 1920 <= int(birth_year) <= 2002
        except:
            return False

    def valid_iyr(passport):
        try:
            issue_year = re.search(r'iyr:(\d{4})(?:$|\s)', passport).groups()[0]
            return 2010 <= int(issue_year) <= 2020
        except:
            return False

    def valid_eyr(passport):
        try:
            exp_year = re.search(r'eyr:(\d{4})(?:$|\s)', passport).groups()[0]
            return 2020 <= int(exp_year) <= 2030
        except:
            return False

    def valid_hgt(passport):
        try:
            height, unit = re.search(r'hgt:(\d*)(cm|in)(?:$|\s)', passport).groups()
            if unit == "cm":
                return 150 <= int(height) <= 193
            elif unit == "in":
                return 59 <= int(height) <= 76
            else:
                raise Exception(f"Unknown unit: {unit}")
        except:
            return False

    def valid_hcl(passport):
        try:
            color = re.search(r'hcl:#([0-9a-f]{6})(?:$|\s)', passport).groups()[0]
            return True
        except:
            return False

    def valid_ecl(passport):
        try:
            color = re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)(?:$|\s)', passport).groups()[0]
            return True
        except:
            return False

    def valid_pid(passport):
        try:
            id = re.search(r'pid:(\d{9})(?:$|\s)', passport).groups()[0]
            return True
        except:
            return False

    valid_count = 0
    for passport in passports:
        if valid_byr(passport) and valid_iyr(passport) and valid_eyr(passport) and valid_hgt(passport) and valid_hcl(passport) and valid_ecl(passport) and valid_pid(passport):
            valid_count += 1
    return valid_count
    
print(solve_part_2())