with open('./input', encoding='utf8') as file:
    measurements = [int(value) for value in file]

last = 99999
increasing = 0

for measurement in measurements:
    if measurement > last:
        increasing += 1
    last = measurement

print(increasing)
