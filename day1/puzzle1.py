def get_calibration_values(s: str) -> int:
    val1 = None
    val2 = None
    i = 0
    while i < len(s):
        if s[i].isnumeric():
            val1 = s[i]
            break
        i += 1
    
    j = len(s) - 1
    while j >= 0:
        if s[j].isnumeric():
            val2 = s[j]
            break
        j -= 1
    
    return int(val1 + val2)

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

res = sum(get_calibration_values(s) for s in lines)

print(res)