
from io import TextIOWrapper
from typing import List

from advent_day import AdventDay

class Day3(AdventDay):
    rucksacks : TextIOWrapper
    def __init__(self, input: TextIOWrapper):
        super().__init__(input)
        self.rucksacks = input

    def part1(self):
        """
            Sums the priorities of items that appear in both the first and second
            half of each rucksack in the input file
        """
        sum = 0
        self.rucksacks.seek(0,0)
        for rucksack in self.rucksacks:
            trim = rucksack.strip("\n")
            first = trim[0:int(len(trim) / 2)]
            second = trim[int(len(trim) / 2):len(trim)]
            for char in first:
                if second.count(char) > 0:
                    sum += priority(char)
                    break
        return sum
        
    def part2(self):
        """
            Sums the priorities of identifying unique badge items that appear in all three of each group of
            three elves.
        """
        sum = 0
        group_count = 0
        group: List[str] = []
        self.rucksacks.seek(0,0)
        for rucksack in self.rucksacks:
            if rucksack != '\n':
                group.append(rucksack)
                if len(group) == 3:
                    group_count += 1
                    [first, second, third] = [sack.strip(' \n') for sack in group]
                    for char in first:
                        if second.count(char) > 0 and third.count(char) > 0:
                            sum += priority(char)
                            break
                    group.clear()
        return sum


def priority(char: str) -> int:
    """
        returns priority of given rucksack item.
        Priorities are 1-26 for 'a' - 'z' and 27-52 for 'A'-'Z'
    """
    if (char.islower()):
        return ord(char) - ord('a') + 1
    elif (char.isupper()):
        return ord(char) - ord('A') + 27
    else:
        raise ValueError()
