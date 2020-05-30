#!/usr/bin/python3.8
import csv
import argparse
from typing import Dict


def get_args() -> Dict[str, str]:
    parser = argparse.ArgumentParser(description="Guesses which character would win")
    parser.add_argument("character", type=str)
    parser.add_argument("character2", type=str)

    preParsedVars = vars(parser.parse_args())

    return {k: v.lower() for (k, v) in preParsedVars.items()}


class Character:
    def __init__(self, name, ratingArr):
        self.name = name
        self.ratingArr = [int(num) for num in ratingArr]

    def __str__(self):
        return f"{self.name}:{self.ratingArr}"


def process_file() -> Dict[str, Character]:
    with open("arknights.csv") as csvfile:
        dictreader = csv.DictReader(csvfile)
        participantCount: int = len(
            dictreader.fieldnames[1 : dictreader.fieldnames.index("Average")]
        )
        reader = csv.reader(csvfile)

        characters = dict()
        for line in reader:
            name = line[0]
            lowercaseName = name.lower()
            characters[lowercaseName] = Character(
                lowercaseName, line[-participantCount:]
            )
        return characters


def main():
    characters = process_file()
    args = get_args()
    char = characters[args["character"]]
    char2 = characters[args["character2"]]
    combinedRatingArr = list()
    for i in range(len(char.ratingArr)):
        combinedRating = char2.ratingArr[i] - char.ratingArr[i]
        if combinedRating > 0:
            combinedRatingArr.append(1)
        elif combinedRating < 0:
            combinedRatingArr.append(-1)
        else:
            combinedRatingArr.append(0)

    whoWinsNum = sum(combinedRatingArr)

    if whoWinsNum == 0:
        whoWins = "tie"
    elif whoWinsNum > 0:
        whoWins = char2.name
    else:
        whoWins = char.name

    print(char)
    print(char2)
    print(combinedRatingArr)
    print(whoWinsNum)
    print(whoWins)


if __name__ == "__main__":
    main()
