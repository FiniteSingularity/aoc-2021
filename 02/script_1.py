with open('./input', encoding='utf8') as file:
    movements = [[line.split(' ')[0], int(line.split(' ')[1])]
                 for line in file]

up = [line[1] for line in filter(lambda x: x[0] == 'up', movements)]
down = [line[1] for line in filter(lambda x: x[0] == 'down', movements)]
forward = [line[1] for line in filter(lambda x: x[0] == 'forward', movements)]

horizontal = sum(forward)
depth = sum(down)-sum(up)

print(horizontal*depth)
