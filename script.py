x = 1000          # X is the number table, eg x = 20 : 1 x 1 = 1, 1 x 20 = 20, 20 x 20 = 400
buffer = 5        # Minimum number of spaces
max_len = 180     # Maximum number that can be printed in a line of a terminal


calculate_label = lambda j: len("Multiplication table of ") + len(str(j)) + buffer
calculate_mulitply = lambda j, k: 6 + len(str(j)) + len(str(k)) + len(str(j * k)) + buffer

printing_array = [""] * (x ** 2 + x)
total_max_len = max(calculate_mulitply(x, x), calculate_label(x))


current_index = 0
for j in range(1, x + 1):
    current_max_line = max(calculate_mulitply(j, x), calculate_label(j))    
    while True:
        current_max_len = max_len - len(printing_array[current_index])
        if current_max_line > current_max_len:
            current_index += (x + 1)
            current_max_line = 0
        else:
            break
    printing_array[current_index] += (f"Multiplication table of {j}" + (buffer * " ") + (" " * (total_max_len - calculate_label(j))))
    for k in range(1, x + 1):
        printing_array[current_index + k] += (f"{j} x {k} = {j*k}" + (" " * buffer) + (" " * (total_max_len - calculate_mulitply(j, k))))
for z in printing_array:
    if z != "":
        print(z)
