commands = []

with open('./input', encoding='utf8') as file:
    for line in file.readlines():
        cmd, cube = line.strip().split(" ")
        ranges = [
            [int(val)+50 for val in dimension[2:].split('..')]
            for dimension in cube.split(',')
        ]
        commands.append({'cmd': cmd, 'ranges': ranges})

reactor = [[[0 for col in range(101)]for row in range(101)]
           for x in range(101)]

for cmd in commands:
    if cmd['cmd'] == 'on':
        val = 1
    else:
        val = 0
    for i in range(cmd['ranges'][0][0], cmd['ranges'][0][1]+1):
        if abs(cmd['ranges'][0][0]) > 100 or abs(cmd['ranges'][0][1])+1 > 100:
            continue
        for j in range(cmd['ranges'][1][0], cmd['ranges'][1][1]+1):
            for k in range(cmd['ranges'][2][0], cmd['ranges'][2][1]+1):
                reactor[i][j][k] = val

total = 0
for r1 in reactor:
    for r2 in r1:
        total += sum(r2)

print(total)
