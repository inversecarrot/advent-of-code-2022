from io import TextIOWrapper

from advent_day import AdventDay

class Day4(AdventDay): 
    pairs: TextIOWrapper
    def __init__(self, input: TextIOWrapper):
        super().__init__(input)
        self.pairs = input

    def part1(self) -> str:
        num_overlaps = 0
        self.pairs.seek(0,0)
        for pair in self.pairs:
            if pair != '\n':
                bounds = [get_bounds(elf) for elf in pair.split(",")]
                diffs = (bounds[0][0] - bounds[1][0], bounds[1][1] - bounds[0][1])
                if ((diffs[0] >= 0 and diffs[1] >=0 )or (diffs[0] <=0 and diffs[1] <=0)):
                    num_overlaps +=1
        return num_overlaps
    
    def part2(self) -> str:
        """
            Calculates number of elf pairs who overlap at all
        """
        num_overlaps = 0
        self.pairs.seek(0,0)
        for pair in self.pairs:
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

def get_bounds(elf: str) -> tuple[int, int]:
    """
        Parses string of format X-Y into a tuple of the numbers
    """
    bounds = elf.strip("\n").split("-")
    return (int(bounds[0]), int(bounds[1]))
    


