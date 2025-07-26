def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    def parse_line(line):
        ingredients, allergents = line.split(' (')
        ingredients = ingredients.split()
        allergents = allergents[9:-1].split(', ')
        return ingredients, allergents
    foods = list(map(parse_line, read_input_file_data().splitlines()))
    
    all_ingredients = set()
    allergent_sources = {}
    for ingredients, allergents in foods:
        all_ingredients.update(ingredients) # Record all ingredients
        for allergent in allergents:
            if allergent in allergent_sources:
                allergent_sources[allergent].intersection_update(ingredients)
            else:
                allergent_sources[allergent] = set(ingredients)
    
    clean_ingredients = all_ingredients.copy()
    for possible_sources in allergent_sources.values():
        clean_ingredients.difference_update(possible_sources)
    
    count = 0
    for ingredients, _ in foods:
        for ingredient in ingredients:
            if ingredient in clean_ingredients:
                count += 1
    return count

def solve_part_2():
    def parse_line(line):
        ingredients, allergents = line.split(' (')
        ingredients = ingredients.split()
        allergents = allergents[9:-1].split(', ')
        return ingredients, allergents
    foods = list(map(parse_line, read_input_file_data().splitlines()))
    
    allergent_sources = {}
    for ingredients, allergents in foods:
        for allergent in allergents:
            if allergent in allergent_sources:
                allergent_sources[allergent].intersection_update(ingredients)
            else:
                allergent_sources[allergent] = set(ingredients)
    
    confirmed_allergent_sources = []
    checked_ingredients = set()
    while allergent_sources:
        new_allergent_sources = {}
        for allergent, source in allergent_sources.items():
            if len(source) == 1:
                source_ingredient = source.pop()
                confirmed_allergent_sources.append((allergent, source_ingredient))
                checked_ingredients.add(source_ingredient)
            else:
                new_allergent_sources[allergent] = source.difference(checked_ingredients)
        allergent_sources = new_allergent_sources
    
    confirmed_allergent_sources.sort()
    return ','.join([ingredient for (allergent, ingredient) in confirmed_allergent_sources])
    
print(solve_part_2())
