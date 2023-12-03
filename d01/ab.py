import re

data = open("input.txt", "r").read()
lines = data.split("\n")


def a():
    digit_strings = [
        "".join([char for char in line if char.isdigit()]) for line in lines
    ]

    digits = [int(string[0] + string[-1]) for string in digit_strings]

    print(sum(digits))


a()


def b():
    digit_map = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    replaced = []
    for line in lines[:]:
        matches = re.findall(
            r"(?=(one|two|three|four|five|six|seven|eight|nine))", line
        )
        for match in matches:
            line = line.replace(match, digit_map[match])
        replaced.append(line)

    digit_strings = [
        "".join([char for char in line if char.isdigit()]) for line in replaced
    ]

    digits = [int(string[0] + string[-1]) for string in digit_strings]

    print(sum(digits))


b()
