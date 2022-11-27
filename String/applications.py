def is_unique(x: str) -> bool:
    # return len(x) == len(set(x))
    chars_dict = dict()
    i = 0
    while i < len(x):
        if x[i] in chars_dict:
            return False
        else:
            chars_dict[x[i]] = 1
        i += 1
    return True


def reverse_int(x: int) -> int:
    symbol = -1 if x < 0 else 1
    number = symbol * int(str(abs(x))[::-1])

    if number.bit_length() > 31:
        return 0

    return number


def chars_to_int(x: str) -> int:
    num = 0
    count = len(x) - 1
    for s in x:
        num += 26 ** count * (ord(s) - ord('A') + 1)
        count -= 1
    return num


def str_to_int(input_str: str) -> int:
    output_int = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True
    else:
        start_idx = 0
        is_negative = False

    for i in range(start_idx, len(input_str)):
        place = 10**(len(input_str) - (i+1))
        digit = ord(input_str[i]) - ord('0')
        output_int += place * digit

    if is_negative:
        return -1 * output_int
    else:
        return output_int


def int_to_str(input_int: int) -> str:
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []

    if input_int == 0:
        output_str.append('0')
    else:
        while input_int > 0:
            output_str.append(chr(ord('0') + input_int % 10))
            input_int //= 10
        output_str = output_str[::-1]

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str
