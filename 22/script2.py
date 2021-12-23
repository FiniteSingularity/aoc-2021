# Class that describes a rectangular prism.  Inputs are the
# x-min/max, y-min/max, and z-min/max values.  Provides a method
# that returns the result of subtracing another rectangular prism
# from the current instance.
class Prism:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max
        self.volume = (x_max-x_min) * (y_max-y_min) * (z_max-z_min)

    # Returns a list of prisms that describe the remaining volume
    # when you subtract the prism `p` from the current prism.
    # If no overlap, simply returns current prism.  Note, there are
    # either 1 prism (the original) returned (if no overlap), or 6
    # prisms returned (some of which might have a volume of zero)
    def subtract_prism(self, p):
        # 1. Check if there is overlap between self and p.
        #    if not, return self as the only list element
        if (p.x_min >= self.x_max) or \
                (p.x_max <= self.x_min) or \
                (p.y_min >= self.y_max) or \
                (p.y_max <= self.y_min) or \
                (p.z_min >= self.z_max) or \
                (p.z_max <= self.z_min):
            return [self]

        # 2. Cut down the subtracing prism, p, to not extend
        #    beyond the boundaries of our current prism.
        p_x_min = max(self.x_min, p.x_min)
        p_x_max = min(self.x_max, p.x_max)
        p_y_min = max(self.y_min, p.y_min)
        p_y_max = min(self.y_max, p.y_max)
        p_z_min = max(self.z_min, p.z_min)
        p_z_max = min(self.z_max, p.z_max)

        # 3. Return the 6 prisms that result from removing the
        #    volume of prism P.
        return [
            Prism(self.x_min, p_x_min,
                  self.y_min, self.y_max,
                  self.z_min, self.z_max),
            Prism(p_x_max,    self.x_max,
                  self.y_min, self.y_max,
                  self.z_min, self.z_max),
            Prism(p_x_min,    p_x_max,
                  self.y_min, p_y_min,
                  self.z_min, self.z_max),
            Prism(p_x_min,    p_x_max,
                  p_y_max,    self.y_max,
                  self.z_min, self.z_max),
            Prism(p_x_min,    p_x_max,
                  p_y_min,    p_y_max,
                  self.z_min, p_z_min),
            Prism(p_x_min,    p_x_max,
                  p_y_min,    p_y_max,
                  p_z_max,    self.z_max)
        ]


# Load all of the data into a commands list
commands = []
with open('./input', encoding='utf8') as file:
    for line in file.readlines():
        cmd, cube = line.strip().split(" ")
        ranges = [
            [int(val) for val in dimension[2:].split('..')]
            for dimension in cube.split(',')
        ]
        commands.append({'cmd': cmd, 'ranges': ranges})

# Iterate over all comamnds, and do the stuff.
prisms = []
for cmd in commands:
    range_x = cmd['ranges'][0]
    range_y = cmd['ranges'][1]
    range_z = cmd['ranges'][2]

    # must add one to max range, as in the problem we are counting
    # "nodes" that are lit, and here we are using volume.
    # e.g.-  |-|-|  the volume count (-) is 2, the node count (|) is 3.
    # If we expand the max by 1, we get |-|-|-|, which gives up the proper
    # number of nodes in the original volume.
    loaded_prism = Prism(range_x[0], range_x[1]+1, range_y[0],
                         range_y[1]+1, range_z[0], range_z[1]+1)

    # next, take the loaded prism, and subtract it from all other prisms
    # already loaded/generated.  The subtraction process yields up to 6 new
    # prisms (minus a prism in the shape of the intersection).  We replace
    # the current prism in the list with the result of this subtraction process.
    prisms = [
        sub_prism
        for prism in prisms
        for sub_prism in prism.subtract_prism(loaded_prism)
        if sub_prism.volume > 0
    ]

    # If the loaded prism was a command to turn 'on', we add the loaded
    # prism to our list of prisms.  If cmd is 'off' this prism is not
    # added as it is empty space.
    if cmd['cmd'] == 'on':
        prisms.append(loaded_prism)

# sum the volume of all prisims in our list.
print(sum([p.volume for p in prisms]))
