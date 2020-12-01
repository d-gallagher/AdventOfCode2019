# test input
# 123456789012
def split_img(file, width, height):
    # img = []
    zeroes = []
    ones = []
    twos = []
    onetwo = []
    with open(file, "r") as infile:
        while True:
            # read in pixels and process
            pixels = infile.read(width * height)
            if not pixels:
                break
            zero, one, two = count_zeroes_ones_twos(pixels)
            # layer = get_layer(pixels, width, height)

            # #
            # img.append(layer)
            zeroes.append(zero)
            ones.append(one)
            twos.append(two)
            onetwo.append(one * two)
    return zeroes, ones, twos, onetwo


def get_layer(pixels, width, height):
    layer = []
    for _ in range(height):
        row = pixels[:width]
        layer.append(row)
    return layer


def count_zeroes_ones_twos(pixels):
    zeroes = ones = twos = 0
    for idx, x in enumerate(pixels):
        if x == '0':
            zeroes += 1
        if x == '1':
            ones += 1
        if x == '2':
            twos += 1
    return zeroes, ones, twos


zeroes, ones, twos, onetwo = split_img("input.txt", 25, 6)
min_zero = min(zeroes)
for z, o, t, ot, in zip(zeroes, ones, twos, onetwo):
    if z == min_zero:
        print(f'{z}, {o}, {t}, {ot}')
