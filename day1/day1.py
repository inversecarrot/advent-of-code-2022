from io import TextIOWrapper
from typing import List

from advent_day import AdventDay

class Day1(AdventDay):
    elves: TextIOWrapper
    def __init__(self, input):
        super().__init__(input)
        self.elves = input

    def part1(self):
        """ 
        Reads input file in format specified at https://adventofcode.com/2022/day/1 and 
            returns the largest elf's calories
        """
        # we're gonna assume the file exists for now
        max_elf: int = 0
        cur: int = 0
        self.elves.seek(0,0)
        for line in self.elves:
            if line == '\n':
                max_elf = max(cur, max_elf)
                cur = 0
            else:
                cur = cur + int(line)
        return max_elf
    
    def part2(self):
        """ 
        Reads input file in format specified at https://adventofcode.com/2022/day/1 and 
            returns the sum of the three largest elves' calories
        """
        total: int = 0
        self.elves.seek(0,0)
        max_elves: List[int] = []
        cur: int = 0
        for line in self.elves:
            if line == '\n':
                if len(max_elves) < 3:
                    max_elves.append(cur)
                else:
                    if len(max_elves) == 3:
                        max_elves.sort(reverse=True)
                    if cur > max_elves[2]:
                        max_elves[2] = cur
                        max_elves.sort(reverse=True)
                cur = 0
            else:
                cur = cur + int(line)
        total = sum(max_elves)
        return total


