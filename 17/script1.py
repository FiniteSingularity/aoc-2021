# return n * (n+1) / 2

with open('./input', encoding='utf8') as file:
    coord_strs = file.readline().strip()[12:].split(', ')
    x_range = [int(val) for val in coord_strs[0].split('=')[1].split('..')]
    y_range = [int(val) for val in coord_strs[1].split('=')[1].split('..')]

y_speed = abs(y_range[0])-1

print(y_speed * (y_speed+1)/2)
