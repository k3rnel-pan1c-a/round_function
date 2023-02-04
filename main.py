

def round_function(num: float, round_to: int = 0) -> float:

    if not isinstance(round_to, int):
        raise TypeError(f"'{type(round_to)}' object cannot be interpreted as an integer")

    num_abs = abs(num)
    if round_to < 0:
        if abs(round_to) > len(str(num_abs).split(".")[0]):
            return 0.0
        new_num = num * 10 ** round_to
        after_decimal_point = new_num % 1
        if 1 > new_num > 0:
            if int(after_decimal_point[0]) > 4:
                return float((2 * (num > 0) - 1) * 10 ** -round_to)
            else:
                return 0.0
        else:
            return float(int(new_num + (not num > 0) - 0.5) + 2 * (num > 0) - 1) * 10 ** -round_to

    elif 1 > num > 0:
        if round_to == 0:
            if abs(num) % 1 * 10 // 1 > 4:
                return -1.0 if num < 0 else 1.0
            else:
                return 0.0
        else:
            before_decimal_point, after_decimal_point = str(
                (num_abs - 0.5 * 10 ** -round_to) + 1 * 10 ** -round_to).split(".")
            if int(before_decimal_point) == 1:
                return 1.0 if num > 0 else -1.0
            before = "".join(after_decimal_point[0:round_to - 1])

            return (2 * (num > 0) - 1) * float(f"0.{before}{after_decimal_point[round_to - 1]}")

    return (int((10 ** round_to) * num + ((not num > 0) - 0.5)) - (2 * (not num > 0) - 1)) / 10 ** round_to
