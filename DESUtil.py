def add_pads_if_necessary(s):
    """adding bits to make an integer number of 64-bit blocks
    """
    number_of_vacancy = len(s) % 64
    need_pads = number_of_vacancy > 0
    if need_pads:
        for i in range(64 - number_of_vacancy):
            s.append(0)
    return s

def get_bits(plaintext):
    text_bits = []
    for i in plaintext:
        text_bits.extend(to_binary(i))
    return text_bits

def to_binary(s):
    # if isinstance(s, int):
    #     n = s
    # else:
    #     n = ord(s)
    n = ord(s)
    b = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 8):
        if n % 2:
            b[7 - i] = 1
        n = n // 2
    return b

def left_shift(s, times):
    for i in range(times):
        s.append(s.pop(0))
    return s