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
    visibility: List[List[bool]]
    def __init__(self, input: TextIOWrapper):
        self.trees = self._parse_input(input)
        self.columns = len(self.trees[0])
        self.rows = len(self.trees)
        self.visibility = [[False for x in range(0, self.columns)] for y in range(0, self.rows)]
        

    def _parse_input(self, input: TextIOWrapper):
        next_line = input.readline()
        trees = []
        while next_line:
            trees.append([int(x) for x in list(next_line.strip('\n'))])
            next_line = input.readline() 
        return trees
    
    def calculate_cover(self) -> int:
        max_heights = [-1 for x in range(0, self.columns)]

        # start down
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                if self.trees[row][col] > max_heights[col]:
                    self.visibility[row][col] = True
                    max_heights[col] = self.trees[row][col]
        # go up
        max_heights = [-1 for x in range(0, self.columns)]
        for row in reversed(range(0, self.rows)):
            for col in range(0, self.columns):
                if self.trees[row][col] > max_heights[col]:
                    self.visibility[row][col] = True
                    max_heights[col] = self.trees[row][col]
        # go left
        max_heights = [-1 for x in range(0, self.rows)]
        for col in range(0, self.columns):
            for row in range(0, self.rows):
                if self.trees[row][col] > max_heights[row]:
                    self.visibility[row][col] = True
                    max_heights[row] = self.trees[row][col]
        # and finally, right
        max_heights = [-1 for x in range(0, self.rows)]
        for col in reversed(range(0, self.columns)):
            for row in range(0, self.rows):
                if self.trees[row][col] > max_heights[row]:
                    self.visibility[row][col] = True
                    max_heights[row] = self.trees[row][col]

        return sum([col.count(True) for col in self.visibility])

    
    def find_max_visibility(self) -> int:
        # is there some way to look at the data so we only check some squares?
        # i.e. if we are checking a tree and pass over other trees, we can
        # eliminate them somehow? or maybe we can store that info so we don't
        # have to scan back and forth every time.
        max_visibility = 0
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                visibility = self._get_visibility_score(row, col)
                if visibility > max_visibility:
                    max_visibility = visibility
        return max_visibility
        
    def _get_visibility_score(self, row: int, col: int) -> int:
        height = self.trees[row][col]
        if row == 0 or col == 0 or row == self.rows - 1 or col == self.columns - 1:
            return 0
        up, down, left, right = (0,0,0,0)
        # start down
        for cur_row in range(row + 1, self.rows):
            down += 1
            if self.trees[cur_row][col] >= height:
                break
        for cur_row in reversed(range(0, row)):
            up += 1
            if self.trees[cur_row][col] >= height:
                break
        # then left
        for cur_col in range(col + 1, self.columns):
            left +=1
            if self.trees[row][cur_col] >= height:
                break
        # then right
        for cur_col in reversed(range(0, col)):
            right += 1
            if self.trees[row][cur_col] >= height:
                break
        return up * down * left * right
