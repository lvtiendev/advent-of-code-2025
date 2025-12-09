file_path = "input.txt"

with open(file_path, "r") as file:
    num = 0
    cur = 50
    for line in file:
        line = line.strip()
        multi = -1 if line[0] == "L" else 1
        cur = (cur + multi * int(line[1:])) % 100
        if cur == 0:
            num += 1
    print(num)
