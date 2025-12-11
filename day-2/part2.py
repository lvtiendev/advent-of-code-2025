file_path = "input.txt"


def check_with_repeat(num, repeat):
    l = len(str(num))
    if (l % repeat) == 0:
        s = l // repeat  # length of 1 group
        p = int(pow(10, s))
        g = num % p
        for i in range(repeat):
            num -= g
            g *= p
    return num == 0


def check(num):
    l = len(str(num))
    for r in range(2, l + 1):
        if check_with_repeat(num, r):
            return True
    return False


def process(lower, upper):
    result = 0
    for x in range(lower, upper + 1):
        if check(x):
            result += x
    return result


with open(file_path, "r") as file:
    result = 0
    for line in file:
        line = line.strip()
        ranges = line.split(",")
        for r in ranges:
            if r != "":
                lower = int(r.split("-")[0])
                upper = int(r.split("-")[1])
                p = process(lower, upper)
                result += p
    print(result)
