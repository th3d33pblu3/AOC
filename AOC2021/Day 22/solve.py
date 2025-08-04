def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    tracked_cubes = {}
    for x in range (-50, 51):
        for y in range(-50, 51):
            for z in range(-50, 51):
                tracked_cubes[(x, y, z)] = False

    instructions = read_input_file_data().splitlines()
    for line in instructions:
        state, cubes = line.split()
        state = state == 'on'
        x, y, z = cubes.split(',')
        x1, x2 = list(map(int, x[2:].split('..')))
        y1, y2 = list(map(int, y[2:].split('..')))
        z1, z2 = list(map(int, z[2:].split('..')))

        if x2 < -50 or x1 > 50 or y2 < -50 or y1 > 50 or z2 < -50 or z1 > 50:
            continue

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    tracked_cubes[(x, y, z)] = state
    
    return len(list(filter(lambda v: v, tracked_cubes.values())))
            
def solve_part_2():
    '''
    Cuts the to_cut cube using the fixed cube.
    '''
    def difference(to_cut: list[int], fixed: list[int]) -> list[list[int]]:
        x1, x2, y1, y2, z1, z2 = fixed
        a1, a2, b1, b2, c1, c2 = to_cut
        
        if x1 > a2 or x2 < a1 or y1 > b2 or y2 < b1 or z1 > c2 or z2 < c1:
            return [to_cut]
        
        output = [
            [a1, a2, b1, b2, z2+1, c2], # Top
            [a1, a2, b1, b2, c1, z1-1], # Bottom
            [a1, x1-1, max(b1, y1), min(b2, y2), max(c1, z1), min(c2, z2)], # Left
            [x2+1, a2, max(b1, y1), min(b2, y2), max(c1, z1), min(c2, z2)], # Right
            [a1, a2, b1, y1-1, max(c1, z1), min(c2, z2)], # Front
            [a1, a2, y2+1, b2, max(c1, z1), min(c2, z2)], # Back
        ]

        output = list(filter(lambda o: o[0] >= a1 and o[1] <= a2 and o[2] >= b1 and o[3] <= b2 and o[4] >= c1 and o[5] <= c2 and o[0] <= o[1] and o[2] <= o[3] and o[4] <= o[5], output))
        return output
    
    '''
    Returns the new ins_area that should turn cubes off
    '''
    def on_difference(cube: list[int], ins_area: list[list[int]]):
        new_ins_area = []
        for ia in ins_area:
            new_ins_area.extend(difference(ia, cube))
        return new_ins_area

    '''
    Returns the new cube after being turned off
    '''
    def off_difference(cube: list[int], ins_area: list[list[int]]):
        fixed = ins_area[0]
        return difference(cube, fixed)

    on_cubes = []
    instructions = read_input_file_data().splitlines()
    for line in instructions:
        state, cubes = line.split()
        is_on = state == 'on'
        x, y, z = cubes.split(',')
        x1, x2 = list(map(int, x[2:].split('..')))
        y1, y2 = list(map(int, y[2:].split('..')))
        z1, z2 = list(map(int, z[2:].split('..')))
        ins_area = [[x1, x2, y1, y2, z1, z2]]

        # Remove duplicate for on
        if is_on:
            for cube in on_cubes:
                ins_area = on_difference(cube, ins_area)
                if not ins_area:
                    break
            if ins_area:
                on_cubes.extend(ins_area)
        # Cut cubes for off
        else:
            new_cubes = []
            for cube in on_cubes:
                off_result = off_difference(cube, ins_area)
                if off_result:
                    new_cubes.extend(off_result)
            on_cubes = new_cubes

    count = 0
    for cube in on_cubes:
        count += (cube[1]+1-cube[0]) * (cube[3]+1-cube[2]) * (cube[5]+1-cube[4])
    return count

print(solve_part_2())