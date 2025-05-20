from io import TextIOWrapper
from typing import List, Tuple
from advent_day import AdventDay
from day9.rope_grid import RopeGrid

class Day9(AdventDay):
    debug: bool
    moves: List[Tuple[int, int]]

    def __init__(self, input: TextIOWrapper, debug = False):
        self.moves = Day9._parse_moves(input)
        self.debug = debug
        super().__init__(input)

    def part1(self) -> str:
        grid = RopeGrid(self.moves, debug=self.debug)
        return grid.get_tail_visits()

    def part2(self) -> str:
        grid = RopeGrid(self.moves, 10, debug=self.debug)
        return grid.get_tail_visits()
    
    def _parse_moves(input: TextIOWrapper) -> List[Tuple[int, int]]:
        moves = []
        for line in input:
            move = line.strip("\n").split(" ")
            direction = move[0]
            distance = int(move[1])
            if direction == 'U':
                moves += [(0,1)] * distance
            elif direction == 'D':
                moves += [(0,-1)] * distance
            elif direction == 'R':
                moves += [(1,0)] * distance
            else:
                moves += [(-1,0)] * distance
        return moves