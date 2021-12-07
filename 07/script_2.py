import statistics
import math


def additorial(n):
    return n * (n+1) / 2


with open('./input', encoding='utf8') as file:
    positions = [int(value) for value in file.readline().split(',')]

max_position = max(positions)
min_position = min(positions)
mean_position = statistics.mean(positions)
if (mean_position - min_position) < (max_position - mean_position):
    rng = range(min_position, math.ceil(mean_position)+1)
else:
    rng = range(math.floor(mean_position), max_position)

# rng = range(min_position, max_position)

min_fuel = 100000000000000

for alignment in rng:
    fuel = [additorial(abs(position-alignment)) for position in positions]
    total_fuel = sum(fuel)
    min_fuel = min(min_fuel, total_fuel)

print(min_fuel)
