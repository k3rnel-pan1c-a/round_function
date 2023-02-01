from random import randint, uniform


def round_function(num: float, round_to: int = 0) -> float:
    num_abs = abs(num)

    if isinstance(round_to, (float, str, list, dict, tuple)):
        raise TypeError

    if round_to < 0:
        if abs(round_to) > len(str(num_abs).split(".")[0]):
            return 0
        new_num = num * 10 ** round_to
        before_decimal_point, after_decimal_point = str(abs(new_num)).split(".")
        if before_decimal_point == "0":
            if int(after_decimal_point[0]) > 4:
                if num < 0:
                    return float(-1 * 10 ** -round_to)
                else:
                    return float(1 * 10 ** -round_to)
            else:
                return 0
        else:
            if num > 0:
                return float((int(new_num - 0.5) + 1)) * 10 ** -round_to
            else:
                return float((int(new_num + 0.5) - 1)) * 10 ** -round_to

    elif int(str(num_abs)[0]) == 0:
        if round_to == 0:
            if int(str(num_abs).split(".")[1][0]) > 4:  
                return -1 if num < 0 else 1
            else:
                return 0
        else:
            before_decimal_point, after_decimal_point = str(
                (num_abs - 0.5 * 10 ** -round_to) + 1 * 10 ** -round_to).split(".")
            if int(before_decimal_point) == 1:
                return 1 if num > 0 else -1
            before = "".join(after_decimal_point[0:round_to - 1])
            if num > 0:
                return float(f"0.{before}{after_decimal_point[round_to - 1]}")
            else:
                return float(f"-0.{before}{after_decimal_point[round_to - 1]}")
    elif num > 0:
        return (int((10 ** round_to) * num - 0.5) + 1) / 10 ** round_to
    else:
        return (int((10 ** round_to) * num + 0.5) - 1) / 10 ** round_to


def main() -> None:
    correct = 0
    for _ in range(100_000):
        n = uniform(-10_000, 10_000)
        ndigits = randint(-5, 5)
        a = round(n, ndigits)
        b = round_function(n, ndigits)
        if a == b:
            correct += 1
            continue
        print(
            f"round({n: >22.15f}, {ndigits: })    ->    "
            f"built-in: {a: >22.15f}\t\tcustom: {b: >22.15f}"
        )
    print(f"Correct: {correct / 100_000:%}")


if __name__ == "__main__":
    main()
    num = -5
    print()