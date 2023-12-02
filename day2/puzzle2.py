import re


with open("input.txt", "r") as f:
    lines = f.readlines()

res = 0

for line in lines:
    match = re.search(r"Game (\d+)", line)

    subsets_str = line[match.span()[1] + 2 :]
    subsets = subsets_str.split(";")

    max_red = 0   
    max_green = 0
    max_blue = 0 
    for subset in subsets:
        colors_str = subset.split(",")
        colors_str[-1] = colors_str[-1].replace("\n", "")
        for color_str in colors_str:
            count, color = color_str.strip().split(" ")
            count = int(count)
            match color:
                case "red":
                    max_red = max(count, max_red)
                case "blue":
                    max_blue = max(count, max_blue)
                case "green":
                    max_green = max(count, max_green)   
    res += max_red * max_blue * max_green
    
print(res)