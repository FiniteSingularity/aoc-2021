with open('./input', encoding='utf8') as file:
    measurements = [int(value) for value in file]

last = 99999
increasing = 0

for i, measurement in enumerate(measurements):
    if i > 1:
        sliding_sum = sum(measurements[i-2:i+1])
        if sliding_sum > last:
            increasing += 1
        last = sliding_sum

print(increasing)
