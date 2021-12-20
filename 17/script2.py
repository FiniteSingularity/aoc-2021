# return n * (n+1) / 2

def x_hits(x_vel, min_x, max_x):
    cur_x = x_vel
    x_pos = 0
    step = 0
    hit_steps = []
    while x_pos <= max_x and cur_x >= 0:
        step += 1
        x_pos += cur_x
        if x_pos >= min_x and x_pos <= max_x:
            hit_steps.append({'step': step, 'vel': cur_x})
        cur_x -= 1
    return hit_steps


def y_hits(y_vel, min_y, max_y):
    cur_y = y_vel
    y_pos = 0
    step = 0
    hit_steps = []
    while y_pos >= min_y:
        step += 1
        y_pos += cur_y
        if y_pos >= min_y and y_pos <= max_y:
            hit_steps.append({'step': step})
        cur_y -= 1
    return hit_steps


with open('./input', encoding='utf8') as file:
    coord_strs = file.readline().strip()[12:].split(', ')
    x_range = [int(val) for val in coord_strs[0].split('=')[1].split('..')]
    y_range = [int(val) for val in coord_strs[1].split('=')[1].split('..')]

max_y = abs(y_range[0])-1
min_y = y_range[0]
max_x = x_range[1]

possible_x = []
current_x = max_x

x = max_x

x_velocities = {}
x_zero_velcities = {}
y_velocities = {}

while x > 0:
    hits = x_hits(x, x_range[0], x_range[1])
    for hit in hits:
        if hit['vel'] > 0:
            if not hit['step'] in x_velocities:
                x_velocities[hit['step']] = []
            x_velocities[hit['step']].append(x)
        else:
            if not hit['step'] in x_zero_velcities:
                x_zero_velcities[hit['step']] = []
            x_zero_velcities[hit['step']].append(x)
    x -= 1

for y in range(min_y, max_y+1):
    hits = y_hits(y, y_range[0], y_range[1])
    for hit in hits:
        if not hit['step'] in y_velocities:
            y_velocities[hit['step']] = []
        y_velocities[hit['step']].append(y)


zero_keys = list(x_zero_velcities.keys())

valid_shots = []

for steps, vels in y_velocities.items():
    if steps in x_velocities:
        for y in vels:
            valid_shots += [(x, y) for x in x_velocities[steps]]

    valid_zero_keys = list(filter(lambda x: x <= steps, zero_keys))

    for key in valid_zero_keys:
        for y in vels:
            valid_shots += [(x, y) for x in x_zero_velcities[key]]

valid_shots_set = set(valid_shots)

print(len(valid_shots_set))
