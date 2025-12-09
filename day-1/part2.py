file_path = "input.txt"

with open(file_path, "r") as file:
    num = 0
    cur = 50
    for line in file:
        line = line.strip()
        multi = -1 if line[0] == "L" else 1
        rotations = int(line[1:])
        cur += multi * rotations
        num += abs(cur // 100)
        cur = cur % 100
    print(num)
