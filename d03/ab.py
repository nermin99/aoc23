import re
import numpy as np

data = open("input.txt", "r").read()


numbers = re.findall(r"\d+", data)
specials = re.findall(r"[^\d\.\n]", data)
numbers = list(set(numbers))
specials = list(set(specials))


def get_i_j(index):
    width = len(data.split("\n")[0]) + 1
    col = index % width
    row = int((index - col) / width)
    return row, col


def find_all_indices(main_string, sub_string, number=True):
    if number:
        matches = re.finditer(rf"\b{re.escape(sub_string)}\b", main_string)
    else:
        matches = re.finditer(rf"{re.escape(sub_string)}", main_string)
    return [match.start() for match in matches]


def a():
    special_indices = []
    for special in specials:
        indices = find_all_indices(data, special, number=False)
        for index in indices:
            special_indices.append(get_i_j(index))

    sum = 0
    for number in numbers:
        number_indices = find_all_indices(data, number)

        for number_index in number_indices:
            number_i, number_j = get_i_j(number_index)

            for special_index in special_indices:
                special_i, special_j = special_index
                if abs(number_i - special_i) <= 1 and (
                    abs(number_j - special_j) <= 1
                    or abs(number_j + (len(number) - 1) - special_j) <= 1
                ):
                    # print(number, (number_i, number_j), (special_i, special_j))
                    sum += int(number)
                    break
    print(sum)


a()


def b():
    star_indices = find_all_indices(data, "*", number=False)
    neighbours = []

    number_dict = {}
    for number in numbers:
        number_indices = find_all_indices(data, number)
        i_j = []
        for number_index in number_indices:
            number_i, number_j = get_i_j(number_index)
            i_j.append((number_i, number_j))
        number_dict[number] = i_j

    for star_index in star_indices:
        star_i, star_j = get_i_j(star_index)

        neighbour = []
        for number, number_indices in number_dict.items():
            for number_i, number_j in number_indices:
                if abs(number_i - star_i) <= 1 and (
                    abs(number_j - star_j) <= 1
                    or abs(number_j + (len(number) - 1) - star_j) <= 1
                ):
                    neighbour.append(int(number))
        neighbours.append(neighbour)

    prods = [np.prod(x) for x in neighbours if len(x) == 2]
    total = sum(prods)
    print(total)


b()
