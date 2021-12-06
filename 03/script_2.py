# Open input, and split each line into list of 0 or 1 integers
with open('./input', encoding='utf8') as file:
    report = [
        [int(val) for val in list(line.strip())] for line in file
    ]

# First find the O2 Scrubber rating
o2_rows = report
filtering_col = 0

# While our number of valid rows is greater than 1...
while len(o2_rows) > 1:
    # Transpose our list
    bit_columns = list(map(list, zip(*o2_rows)))
    # Find the most common value in the filtering column (mc)
    # Note: we use >= so that equal common value defaults to 1.
    mc = 1 if sum(bit_columns[filtering_col]) >= len(o2_rows)/2 else 0
    # Filter all rows where the filtering column value == mc
    o2_rows = list(filter(lambda x: x[filtering_col] == mc, o2_rows))
    # Increment mc
    filtering_col += 1

# Now do the same for CO2 Scrubber rating using least common value.
co2_rows = report
filtering_col = 0

while len(co2_rows) > 1:
    bit_columns = list(map(list, zip(*co2_rows)))
    lc = 0 if sum(bit_columns[filtering_col]) >= len(co2_rows)/2 else 1
    co2_rows = list(filter(lambda x: x[filtering_col] == lc, co2_rows))
    filtering_col += 1

# convert list of bits to string of bits, then integer from base2
o2_rating = int(''.join([str(bit) for bit in o2_rows[0]]), 2)
co2_rating = int(''.join([str(bit) for bit in co2_rows[0]]), 2)

print(o2_rating*co2_rating)
