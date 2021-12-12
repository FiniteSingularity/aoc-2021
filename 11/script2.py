def increment(values):
    for r in range(0,len(values)):
        for c in range(0, len(values[r])):
            values[r][c] += 1
    return values

def trigger_flashes(values, r, c):
    if values[r][c]['val'] > 9 and not values[r][c]['flashed']:
        values[r][c]['flashed'] = True
        for rr in list(set([max(r-1, 0), r, min(r+1, len(values)-1)])):
            for cc in list(set([max(c-1, 0), c, min(c+1, len(values[rr])-1)])):
                values[rr][cc]['val'] += 1
                values = trigger_flashes(values, rr, cc)
    return values


with open('./input', encoding='utf8') as file:
    flash_values = [
        [{'val': int(char), 'flashed': False} for char in line.strip() ]
        for line in file.readlines()
    ]

step = 1
total_flashes = 0

rows = len(flash_values)
cols = len(flash_values[0])
all_flashes = rows * cols

while total_flashes != all_flashes:
    total_flashes = 0
    for r in range(0,len(flash_values)):
        for c in range(0, len(flash_values[r])):
            flash_values[r][c]['val'] += 1
            flash_values[r][c]['flashed'] = False

    for r in range(0,len(flash_values)):
        for c in range(0, len(flash_values[r])):
            flash_values = trigger_flashes(flash_values, r, c)

    for r in range(0,len(flash_values)):
        for c in range(0, len(flash_values[r])):
            if flash_values[r][c]['val'] > 9:
                total_flashes += 1
                flash_values[r][c]['val'] = 0
    step += 1

print(step-1)
