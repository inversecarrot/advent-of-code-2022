# Solution for part 1 of day 1
from io import TextIOWrapper

# Reads input file in format specified at https://adventofcode.com/2022/day/1 and
# returns the largest elf's calories
def largest_elf(filename: str) -> int:
    # we're gonna assume the file exists for now
    max_elf: int = 0
    with open(filename, encoding="utf-8") as elves:
        cur: int = 0
        for line in elves:
            if line == '\n':
                max_elf = max(cur, max_elf)
                cur = 0
            else:
                cur = cur + int(line)
    return max_elf

def largest_three_elves(filename: str) -> int:
    total: int = 0
    with open(filename, encoding="utf-8") as elves:
        max_elves: list[int] = []
        cur: int = 0
        for line in elves:
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

def main():
    print(largest_elf('day1\input.txt'))
    print(largest_three_elves('day1\input.txt'))

if __name__ == '__main__':
    main()