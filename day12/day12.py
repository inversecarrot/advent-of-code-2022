import collections
from dataclasses import dataclass
from io import TextIOWrapper
import logging
from typing import List, Tuple
from advent_day import AdventDay

log = logging.getLogger(__name__)

@dataclass
class Square:
    path_length: int
    height: str
    prev: Tuple[int, int] | None = None

class Day12(AdventDay):
    input: TextIOWrapper
    topography: List[List[Square]] # indexed by[row#][col#] or [y][x]
    start_coord: Tuple[int, int] # (col, row) / (x, y)
    end_coord: Tuple[int, int] # (col, row) / (x, y)


    def __init__(self, input: TextIOWrapper):
        super().__init__(input)
        self.input = input
        self._parse_input(input)

    def _parse_input(self, input: TextIOWrapper):
        lines = []
        for line in input:
            line = line.strip("\n")
            if line is not "":
                lines.append(line)

        line_length = len(lines[0])
        self.topography = [
                [
                    Square(path_length = -1, height = lines[row][col]) for col in range(0, line_length)
                ] 
            for row in range(0, len(lines))
        ]
        for row in range(0, len(self.topography)):
            for col in range (0, len(self.topography[0])):
                if self.topography[row][col].height == 'S':
                    self.start_coord = (col, row)
                    self.topography[row][col].height = 'a'
                elif self.topography[row][col].height == 'E':
                    self.end_coord = (col, row)
                    self.topography[row][col].height = 'z'

    def _get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        potential_neighbors = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
        neighbors = []
        cur_square = self.topography[pos[1]][pos[0]]
        for neighbor in potential_neighbors:
            if (
                (neighbor[0] >= 0 and neighbor[0] < len(self.topography[0]))
                and (neighbor[1] >= 0 and neighbor[1] < len(self.topography)) 
            ):
                if ord(cur_square.height) + 1 >= ord(self.topography[neighbor[1]][neighbor[0]].height):
                    neighbors.append(neighbor)
        return neighbors
    
    def _get_neighbors_descending(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        potential_neighbors = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
        neighbors = []
        cur_square = self.topography[pos[1]][pos[0]]
        for neighbor in potential_neighbors:
            if (
                (neighbor[0] >= 0 and neighbor[0] < len(self.topography[0]))
                and (neighbor[1] >= 0 and neighbor[1] < len(self.topography)) 
            ):
                if ord(cur_square.height) <= ord(self.topography[neighbor[1]][neighbor[0]].height) + 1:
                    neighbors.append(neighbor)
        return neighbors
    
    def part1(self) -> str:
        # Graph problem - make a map of each position to the previous node
        # in the shortest path to it, then retrace when we hit the end
        nodes = collections.deque([self.start_coord])
        self.topography[self.start_coord[1]][self.start_coord[0]].path_length = 0
        self.topography[self.start_coord[1]][self.start_coord[0]].prev = self.start_coord
        while nodes:
            cur = nodes.popleft()
            neighbors = self._get_neighbors(cur)
            for neighbor in neighbors:
                if self.topography[neighbor[1]][neighbor[0]].prev is None:
                    self.topography[neighbor[1]][neighbor[0]].path_length = self.topography[cur[1]][cur[0]].path_length + 1
                    self.topography[neighbor[1]][neighbor[0]].prev = cur
                    nodes.append(neighbor)
        return str(self.topography[self.end_coord[1]][self.end_coord[0]].path_length)  

    def part2(self):
        for row in range(0, len(self.topography)):
            for col in range(0, len(self.topography[0])):
                self.topography[row][col].path_length = -1
                self.topography[row][col].prev = None
        nodes = collections.deque([self.end_coord])
        self.topography[self.end_coord[1]][self.end_coord[0]].path_length = 0
        self.topography[self.end_coord[1]][self.start_coord[0]].prev = self.end_coord
        while nodes:
            cur = nodes.popleft()
            neighbors = self._get_neighbors_descending(cur)
            for neighbor in neighbors:
                if self.topography[neighbor[1]][neighbor[0]].prev is None:
                    if self.topography[neighbor[1]][neighbor[0]].height == 'a':
                        return str(self.topography[cur[1]][cur[0]].path_length + 1)
                    self.topography[neighbor[1]][neighbor[0]].path_length = self.topography[cur[1]][cur[0]].path_length + 1
                    self.topography[neighbor[1]][neighbor[0]].prev = cur
                    nodes.append(neighbor)
        return "Did not find a"