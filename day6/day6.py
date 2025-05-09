from io import TextIOWrapper
from advent_day import AdventDay


class Day6(AdventDay):

    datastream: TextIOWrapper
    
    def __init__(self, input: TextIOWrapper):
        self.datastream = input

    def part1(self) -> str:
        return self.parse(4)
    
    def part2(self) -> str:
        return self.parse(14)
    
    def parse(self, marker_size: int)-> str:
        self.datastream.seek(0,0)
        char_count = 1
        next_bit = self.datastream.read(1)
        last = ['' for x in range(0, marker_size -1)]
        while next_bit != '\n':
            if not next_bit in last and char_count >= 4 and len(set(last)) == marker_size - 1:
                return char_count
            last[char_count % (marker_size - 1)] = next_bit
            char_count += 1
            next_bit = self.datastream.read(1)

        return char_count
