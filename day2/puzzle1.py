import re

max_colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open("input.txt", "r") as f:
    lines = f.readlines()

res = 0
for line in lines:
    match = re.search(r"Game (\d+)", line)

    game_id_regex = match.group(1) if match else None
    game_id = int(game_id_regex)

    subsets_str = line[match.span()[1] + 2 :]
    subsets = subsets_str.split(";")
    possible = True

    for subset in subsets:
        colors_str = subset.split(",")
        colors_str[-1] = colors_str[-1].replace("\n", "")
        for color_str in colors_str:
            count, color = color_str.strip().split(" ")
            if int(count) > max_colors[color]:
                possible = False                
                break
    
    if possible:
        res += game_id

print(res)