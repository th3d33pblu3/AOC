def binary_to_grid(data, width, height):
    for y in range(height):
        row = ''
        for x in range(width):
            index = y * width + x
            if data[index] == '1':
                row += '█'  # Use a solid block character for black (1)
            else:
                row += ' '  # Use space for white (0)
        print(row)  # Print the row of the grid

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    data = read_input_file_data()
    layer_size = 25 * 6
    layers = [data[i * layer_size : (i+1) * layer_size] for i in range(len(data) // (25*6))]
    zero_count = list(map(lambda st: st.count("0"), layers))
    layer_number = zero_count.index(min(zero_count))

    layer = layers[layer_number]
    return layer.count("1") * layer.count("2")

def solve_part_2():
    data = read_input_file_data()
    layer_size = 25 * 6
    layers = [data[i * layer_size : (i+1) * layer_size] for i in range(len(data) // (25*6))]

    output = []
    for i in range(layer_size):
        l = 0
        while True:
            if layers[l][i] != '2':
                output.append(layers[l][i])
                break
            else:
                l += 1
    image = ''.join(output)
    return binary_to_grid(image, 25, 6)
    
print(solve_part_2())
