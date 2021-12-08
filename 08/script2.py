data = []
with open('./input', encoding='utf8') as file:
    for line in file.readlines():
        s_dat, d_dat = line.strip().split(' | ')
        signals = [digit for digit in s_dat.split(' ')]
        digits = [digit for digit in d_dat.split(' ')]
        data.append({'signals': signals, 'digits': digits})

sum = 0

lengths = [2, 4, 3, 7]

for row in data:
    wire_map = {
        'a': None,
        'b': None,
        'c': None,
        'd': None,
        'e': None,
        'f': None,
        'g': None
    }
    identified_digits = [None]*10

    for digit in row['signals']:
        if len(digit) == 2:
            identified_digits[1] = digit
        elif len(digit) == 4:
            identified_digits[4] = digit
        elif len(digit) == 3:
            identified_digits[7] = digit
        elif len(digit) == 7:
            identified_digits[8] = digit

    for digit in row['signals']:
        if len(digit) == 5 and len(set(digit) & set(identified_digits[1])) == 2:
            identified_digits[3] = digit

    wire_map['a'] = list(set(identified_digits[7]) -
                         set(identified_digits[1]))[0]

    wire_map['d'] = list((set(identified_digits[3])-set(identified_digits[7])
                          ).intersection(set(identified_digits[4])))[0]

    wire_map['g'] = list(set(identified_digits[3]) -
                         set(identified_digits[7])-set(wire_map['d']))[0]

    wire_map['b'] = list(set(identified_digits[4]) -
                         set(identified_digits[1])-set(wire_map['d']))[0]

    for digit in row['signals']:
        if len(digit) == 5 and len(set(digit) & set(wire_map['b'])) == 1:
            identified_digits[5] = digit

    for digit in row['signals']:
        if len(digit) == 5 and digit != identified_digits[5] and digit != identified_digits[3]:
            identified_digits[2] = digit

    wire_map['e'] = list(set(identified_digits[2]) -
                         set(identified_digits[3]))[0]

    for digit in row['signals']:
        if len(digit) == 6 and len(set(digit) & set(wire_map['d'])) == 0:
            identified_digits[0] = digit
        elif len(digit) == 6 and len(set(digit) & set(wire_map['e'])) == 0:
            identified_digits[9] = digit
        elif len(digit) == 6:
            identified_digits[6] = digit

    digit_map = {
        ''.join(sorted(chars)): i
        for i, chars in enumerate(identified_digits)
    }

    number = [str(digit_map[''.join(sorted(chars))])
              for chars in row['digits']]
    number = int(''.join(number))
    sum += number

print(sum)
