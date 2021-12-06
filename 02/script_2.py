with open('./input', encoding='utf8') as file:
    movements = [[line.split(' ')[0], int(line.split(' ')[1])]
                 for line in file]

aim = 0
depth = 0
horizontal = 0

for move in movements:
    if move[0] == 'forward':
        horizontal += move[1]
        depth += aim * move[1]
    elif move[0] == 'up':
        aim -= move[1]
    else:
        aim += move[1]

print(horizontal * depth)
