state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

with open('./input', encoding='utf8') as file:
    lanternfish = [int(value) for value in file.readline().strip().split(',')]

for fish in lanternfish:
    state[fish] += 1

day = 0
while day < 80:
    reset = state[0]
    state[0:8] = state[1:]
    state[6] += reset
    state[8] = reset
    day += 1

print(sum(state))
