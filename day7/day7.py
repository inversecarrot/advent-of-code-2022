from io import TextIOWrapper
from advent_day import AdventDay
from day7.filetree import FileTree

class Day7(AdventDay):
    TOTAL_SPACE = 70000000
    FREE_SPACE = 30000000

    command_tree: FileTree
    def __init__(self, input:TextIOWrapper):
        self.command_tree= FileTree(input)

    def part1(self) -> str:
        return self.command_tree.get_sum_of_large_directories()
    
    def part2(self) -> str:
        return self.command_tree.get_smallest_big_directory(self.TOTAL_SPACE, self.FREE_SPACE)
        