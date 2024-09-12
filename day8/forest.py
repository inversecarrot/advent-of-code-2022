from io import TextIOWrapper
from typing import List


class Forest:
    trees: List[List[int]]
    visibity: List[List[int]]
    def __init__(self, input: TextIOWrapper):
        self.trees = self._parse_input(input)
        

    def _parse_input(self, input: TextIOWrapper):
        next_line = input.readline()
        trees = []
        while next_line:
            trees.append([int(x) for x in list(next_line.strip('\n'))])
            next_line = input.readline()  
        return trees
    
    def _calculate_cover(self):
        cover = []
        # iterate inward
        # set the outer ring to be 0
        # for the next step in, each value is the max of the value of the cover of the squares immediately
        # between it and the edge and the size of the trees at those positions
        # i.e. the value of every square is the height a tree needs to be to be seen at that position
        return cover