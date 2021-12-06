# Open input, and split each line into list of 0 or 1 integers
with open('./input', encoding='utf8') as file:
    report = [[int(val) for val in list(line.strip())] for line in file]

# Transpose the report list of lists (rows --> columns, columns --> rows)
bit_columns = list(map(list, zip(*report)))

# Get gamma_bits- the most common value in each bit column.  Can sum and see
# if sum > column length/2
gamma_bits = [1 if sum(col) > len(col)/2 else 0 for col in bit_columns]
epsilon_bits = [0 if sum(col) > len(col)/2 else 1 for col in bit_columns]

# convert list of bits to string of bits, then integer from base2
gamma = int(''.join([str(bit) for bit in gamma_bits]), 2)
epsilon = int(''.join([str(bit) for bit in epsilon_bits]), 2)

print(gamma*epsilon)
