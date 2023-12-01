def is_number_string(s: str, i: int) -> (bool, int):
    number_strings = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    s_length = len(s)
    for ns in number_strings.keys():
        l = len(ns)
        if i + l > s_length:
            continue
        if s[i : i + l] == ns:
            return True, number_strings[ns]
    return False, 0


def get_calibration_values(s: str) -> int:
    val1 = None
    val2 = None
    i = 0
    while i < len(s):
        if s[i].isnumeric():
            val1 = s[i]
            break
        is_ns, n = is_number_string(s, i)
        if is_ns:
            val1 = n
            break
        i += 1

    j = len(s) - 1
    while j >= 0:
        if s[j].isnumeric():
            val2 = s[j]
            break
        is_ns, n = is_number_string(s, j)
        if is_ns:
            val2 = n
            break
        j -= 1
    return int(str(val1) + str(val2))

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

res = sum(get_calibration_values(s) for s in lines)

print(res)