import re
from pprint import pprint

data = open("input.txt", "r").read()
lines = data.split("\n")

cards = {}

for line in lines:
    id, winning, have = re.search(r"Card\s+(\d+):(.+)\|(.+)", line).groups()
    cards[int(id)] = {
        "winning": list(map(int, winning.strip().split())),
        "have": list(map(int, have.strip().split())),
        "wins": 0,
        "instances": 1,
    }

total = 0
for id, card in cards.items():
    wins = 0

    for winning in card["winning"]:
        for have in card["have"]:
            if winning == have:
                wins += 1

    if wins > 0:
        total += pow(2, wins - 1)
        cards[id]["wins"] = wins

print("total", total)


for id, card in cards.items():
    for i in range(id + 1, id + card["wins"] + 1):
        cards[i]["instances"] += 1 * card["instances"]

total_cards = sum(v["instances"] for v in cards.values())
print("total_cards", total_cards)
