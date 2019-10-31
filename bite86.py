def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if rgb[0] not in range(0, 256) or rgb[1] not in range(0, 256) or rgb[2] not in range(0, 256):
        raise ValueError
    converted = '#' + ''.join(["{:02x}".format(x).upper() for x in rgb])

    return converted

print(rgb_to_hex((128, 0, 128)))

