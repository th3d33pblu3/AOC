import math

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

Io = [17, -9, 4]
Europa = [2, 2, -13]
Ganymede = [-1, 5, -1]
Callisto = [4, 7, -7]

def solve_part_1():
    moons = [Io, Europa, Ganymede, Callisto]
    velocities = [[0, 0, 0] for _ in range(4)]

    steps = 1000
    for _ in range(steps):
        # Apply gravity
        for i in range(3):
            for j in range(i+1, 4):
                m1 = moons[i]
                m2 = moons[j]
                v1 = velocities[i]
                v2 = velocities[j]
                for axis in range(3):
                    if m1[axis] < m2[axis]:
                        v1[axis] += 1
                        v2[axis] -= 1
                    elif m1[axis] > m2[axis]:
                        v1[axis] -= 1
                        v2[axis] += 1

        # Apply velocity
        for i in range(4):
            m = moons[i]
            v = velocities[i]
            for axis in range(3):
                m[axis] += v[axis]
    
    # calculate total energy
    total_energy = 0
    for i in range(4):
        total_energy += sum(list(map(abs, moons[i]))) * sum(list(map(abs, velocities[i])))
    return total_energy

def solve_part_2():
    moons = [Io, Europa, Ganymede, Callisto]
    velocities = [[0, 0, 0] for _ in range(4)]
    NUM_MOONS = len(moons)

    dimensions = []
    for dim in range(3):
        states = {}
        displacements = [moons[i][dim] for i in range(NUM_MOONS)]
        velocities = [0] * NUM_MOONS
        curr_state = (*displacements, *velocities)
        
        steps = 0
        while curr_state not in states:
            # Track state
            states[curr_state] = steps
            steps += 1
            # Update velocities
            for i in range(NUM_MOONS - 1):
                for j in range(i + 1, NUM_MOONS):
                    if displacements[i] > displacements[j]:
                        velocities[i] -= 1
                        velocities[j] += 1
                    elif displacements[i] < displacements[j]:
                        velocities[i] += 1
                        velocities[j] -= 1
            # Update displacements
            for i in range(NUM_MOONS):
                displacements[i] += velocities[i]
            # Update state
            curr_state = (*displacements, *velocities)

        dimensions.append(steps - states[curr_state])

    # Since there is no remainder, simply return LCM of the result
    x, y, z = dimensions
    r =  x * y // math.gcd(x, y)
    return r * z // math.gcd(r, z)
    
print(solve_part_2())
