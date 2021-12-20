def pad_image(image, padding=3):
    img_y = len(image)
    img_x = len(image[0])
    end_x = img_x + (2 * padding)

    for i in range(img_y):
        line = ''.join(['.' for _ in range(padding)]) + \
            image[i] + ''.join(['.' for _ in range(padding)])
        image[i] = line

    for i in range(padding):
        line = ''.join(['.' for _ in range(end_x)])
        image = [line] + image + [line]

    return image


def enhance(image, iea):
    enhanced = []
    for line in image:
        enhanced.append(['.' for _ in line])

    for idx, line in enumerate(image[1:-1]):
        i = idx+1
        for j in range(1, len(line)-1):
            segment = image[i-1][j-1:j+2]+image[i][j-1:j+2]+image[i+1][j-1:j+2]
            segment_lookup = int(
                ''.join(['0' if val == '.' else '1' for val in segment]), 2)
            enhanced[i][j] = iea[segment_lookup]

    for i in range(0, len(enhanced)):
        enhanced[i] = ''.join(enhanced[i])

    return enhanced


def bright_count(image):
    bright = 0
    for line in image:
        for char in line:
            if char == '#':
                bright += 1
    return bright


with open('./input', encoding='utf8') as file:
    lines = [line.strip() for line in file.readlines()]

iea = lines[0]
image = lines[2:]

image = pad_image(image, 10)
enhanced = enhance(image, iea)
enhanced = enhanced[1:-1]

for i in range(0, len(enhanced)):
    enhanced[i] = enhanced[i][1:-1]

enhanced = enhance(enhanced, iea)

print(bright_count(enhanced))
