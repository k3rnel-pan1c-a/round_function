def round_function(num: float, round_to: int = 0) -> float:
    if not isinstance(round_to, int):
        raise TypeError(f"'{type(round_to)}' object cannot be interpreted as an integer")

    num_abs: float = abs(num)
    if round_to < 0:
        if int(num_abs * 10 ** (- round_to + 1)) == 0:
            return 0.0
        new_num = num * 10 ** round_to
        after_decimal_point: float = abs(new_num) - int(abs(new_num))
        if 1 > abs(new_num) > 0:
            if int(after_decimal_point * 10) > 4:
                return float((2 * (num > 0) - 1) * 10 ** -round_to)
            else:
                return 0.0
        else:
            return float(int(new_num + (not num > 0) - 0.5) + 2 * (num > 0) - 1) * 10 ** -round_to

    elif 1 > num_abs > 0:
        if round_to == 0:
            if abs(num) % 1 * 10 // 1 > 4:
                return -1.0 if num < 0 else 1.0
            else:
                return 0.0
        else:
            new_num: float = num * 10 ** round_to
            if int(abs(new_num)) == 0 and int((abs(new_num) % 1) * 10) == 0 or int(abs(new_num)) == 0 and \
                    int((abs(new_num) % 1) * 10) < 5:
                return 0.0
            return float(
                format((int(new_num + ((not num > 0) - 0.5)) - (2 * (not num > 0) - 1)) * 10 ** - round_to, "22.15f"))

    return (int((10 ** round_to) * num + ((not num > 0) - 0.5)) - (2 * (not num > 0) - 1)) / 10 ** round_to
