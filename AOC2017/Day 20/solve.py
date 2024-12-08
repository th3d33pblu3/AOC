import re
from math import sqrt

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def get_particles():
    return [[tuple(map(int, match)) for match in re.findall(r"<(-?\d+),(-?\d+),(-?\d+)>", line)] for line in read_input_file_data().splitlines()]

def solve_part_1():
    particles = get_particles()
    min_abs = float('infinity')
    min_p = -1
    for p in range(len(particles)):
        ax, ay, az = particles[p][2]
        abs_val = abs(ax) + abs(ay) + abs(az)
        if abs_val < min_abs:
            min_abs = abs_val
            min_p = p
    return min_p

def solve_part_2():
    particles = get_particles()
    NUM_PARTICLES = len(particles)

    def get_collision_frame(particle1, particle2):
        INVALID = -1
        axes1 = list(zip(*particle1))
        axes2 = list(zip(*particle2))
        prev_t = -1
        for i in range(3):
            p1, v1, a1 = axes1[i]
            p2, v2, a2 = axes2[i]

            # Get equation of the form at^2 + bt + c = 0
            a = (a1 - a2) / 2
            b = v1 + (a1 / 2) - v2 - (a2 / 2)
            c = p1 - p2

            if a != 0: # quadratic
                D = b*b - 4*a*c
                if D < 0: return INVALID # No solution
                t_values = [(-b - sqrt(D)) / (2*a), (-b + sqrt(D)) / (2*a)]
                t_values.sort()
                t1, t2 = t_values
                t = t2 if t1 < 0 or not t1.is_integer() else t1
            elif b != 0: # linear
                t = -c / b
            elif c != 0: # constant != 0, no solution
                return INVALID
            else: # any t works
                if i == 2:
                    return 0 if prev_t == -1 else int(prev_t)
                continue
            if t < 0 or not t.is_integer(): return INVALID

            if prev_t == -1:
                prev_t = t
            else:
                if t != prev_t: return INVALID
        return int(prev_t)

    collision_times = set()
    collision_particles = {}
    for i in range(NUM_PARTICLES):
        for j in range(i + 1, NUM_PARTICLES):
            t = get_collision_frame(particles[i], particles[j])
            if t != -1:
                if t in collision_times:
                    collision_particles[t].add((i, j))
                else:
                    collision_particles[t] = {(i, j)}
                    collision_times.add(t)
    collision_times = list(collision_times)
    collision_times.sort()

    collided = set()
    assert set(collision_particles.keys()) == set(collision_times)
    for t in collision_times:
        collisions = collision_particles[t]
        just_collided = set()
        for i, j in collisions:
            if i in collided or j in collided:
                continue
            just_collided.add(i)
            just_collided.add(j)
        collided.update(just_collided)
    return NUM_PARTICLES - len(collided)

def solve_part_2_brute_force():
    def move(particle):
        p, v, a = particle
        v2 = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
        p2 = (p[0] + v2[0], p[1] + v2[1], p[2] + v2[2])
        return (p2, v2, a)

    particles = get_particles()

    ids = set(range(len(particles)))
    for t in range(50): # brute force iterations
        poss = [particles[i][0] for i in ids]
        ids = set(filter(lambda i: poss.count(particles[i][0]) == 1, ids))
        particles = [move(p) for p in particles]
    return len(ids)

print(solve_part_2())

# # Can use this for brute forcing as well
# def get_pos(p, v, a, t):
#     return p + (v * t) + (a * ((t + 1) * t) // 2) # always divisible
