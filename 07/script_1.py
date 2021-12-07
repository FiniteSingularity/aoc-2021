import statistics
import math

with open('./input', encoding='utf8') as file:
    positions = [int(value) for value in file.readline().split(',')]

# Brute Force-ish
max_position = max(positions)
min_position = min(positions)
mean_position = statistics.mean(positions)
if (mean_position - min_position) < (max_position - mean_position):
    rng = range(min_position, math.ceil(mean_position)+1)
else:
    rng = range(math.floor(mean_position), max_position)

min_fuel = 10000000

for alignment in rng:
    fuel = [abs(position-alignment) for position in positions]
    total_fuel = sum(fuel)
    min_fuel = min(min_fuel, total_fuel)

print(min_fuel)

# But it also turns out that the median value is the proper position.
median_position = statistics.median(positions)
alignment = median_position
fuel = [abs(position-alignment) for position in positions]
total_fuel = sum(fuel)

print(total_fuel)
