def get_bounds(elf: str) -> tuple[int, int]:
    """
        Parses string of format X-Y into a tuple of the numbers
    """
    bounds = elf.strip("\n").split("-")
    return (int(bounds[0]), int(bounds[1]))

def part1(filename: str) -> int:
    """
        Calculates number of elf pairs who have one assignment entirely contained in the other
    """
    num_overlaps = 0
    with open(filename, encoding="utf-8") as pairs:
        for pair in pairs:
            if pair != '\n':
                bounds = [get_bounds(elf) for elf in pair.split(",")]
                diffs = (bounds[0][0] - bounds[1][0], bounds[1][1] - bounds[0][1])
                if ((diffs[0] >= 0 and diffs[1] >=0 )or (diffs[0] <=0 and diffs[1] <=0)):
                    num_overlaps +=1
    return num_overlaps

def part2(filename: str) -> int:
    """
        Calculates number of elf pairs who overlap at all
    """
    num_overlaps = 0
    with open(filename, encoding="utf-8") as pairs:
        for pair in pairs:
            if pair != '\n':
                [(e1s, e1e), (e2s, e2e)] = [get_bounds(elf) for elf in pair.split(",")]
                if (
                    (e2s >= e1s and e2s <= e1e) or
                    (e2e >= e1s and e2e <= e1e) or
                    (e1s >= e2s and e1s <= e2e) or
                    (e1e >= e2s and e1e <= e2e)
                ):
                    num_overlaps += 1
    return num_overlaps

if __name__ == '__main__':
    print(part1('day4\\input.txt'))
    print(part2('day4\\input.txt'))
