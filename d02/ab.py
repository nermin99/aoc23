import re

data = open("input.txt", "r").read()
lines = data.split("\n")


def a():
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    sum = 0

    for line in lines:
        before, after = line.split(":")
        game_id = int(re.search(r"\d+", before).group())
        sets = after.split(";")

        is_possible = True
        for set in sets:
            matches = re.findall(r"(\d+) (\w+)", set.strip())
            for quantity, color in matches:
                if color == "red" and int(quantity) > MAX_RED:
                    is_possible = False
                    break
                elif color == "green" and int(quantity) > MAX_GREEN:
                    is_possible = False
                    break
                elif color == "blue" and int(quantity) > MAX_BLUE:
                    is_possible = False
                    break

        if is_possible:
            sum += game_id

    print(sum)


a()


def b():
    sum = 0

    for line in lines:
        MAX_RED = 0
        MAX_GREEN = 0
        MAX_BLUE = 0

        before, after = line.split(":")
        game_id = int(re.search(r"\d+", before).group())
        sets = after.split(";")

        for set in sets:
            matches = re.findall(r"(\d+) (\w+)", set.strip())
            for quantity, color in matches:
                if color == "red" and int(quantity) > MAX_RED:
                    MAX_RED = int(quantity)
                elif color == "green" and int(quantity) > MAX_GREEN:
                    MAX_GREEN = int(quantity)
                elif color == "blue" and int(quantity) > MAX_BLUE:
                    MAX_BLUE = int(quantity)

        power = MAX_RED * MAX_GREEN * MAX_BLUE
        sum += power

    print(sum)


b()
