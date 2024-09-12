from enum import Enum
from io import TextIOWrapper
from typing import Dict, List

# class Direction(Enum):
#     UP = 0
#     DOWN = 1
#     LEFT = 2
#     RIGHT = 3


class Forest:
    # indexed by [row, col]
    trees: List[List[int]]
    columns: int
    rows: int
    def __init__(self, input: TextIOWrapper):
        self.trees = self._parse_input(input)
        self.columns = len(self.trees[0])
        self.rows = len(self.trees)
        

    def _parse_input(self, input: TextIOWrapper):
        next_line = input.readline()
        trees = []
        while next_line:
            trees.append([int(x) for x in list(next_line.strip('\n'))])
            next_line = input.readline() 
        return trees
    
    def calculate_cover(self) -> int:
        visibility = [[False for x in range(0, self.columns)] for y in range(0, self.rows)]
        max_heights = [-1 for x in range(0, self.columns)]
        # start down
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                if self.trees[row][col] > max_heights[col]:
                    visibility[row][col] = True
                    max_heights[col] = self.trees[row][col]
        print(visibility)
        return 0
    
    # def _collapse_forest_in_direction(self, cover: List[List[bool]]):
    #     # start going down
        