"""Script to calculate answers for day 5"""
from io import TextIOWrapper
from advent_day import AdventDay
from day5.stacks import SupplyStacks, Crate

class Day5(AdventDay):
    lines: TextIOWrapper
    def __init__(self, input: TextIOWrapper):
        super().__init__(input)
        self.lines = input

    def part1(self) -> str:
        """
        Calculates the crates that end on top of each stack assuming each move
        is done one by one
        """
        return self.calculate_moves(False)
    
    def part2(self) -> str:
        """
        Calculates the crates that end on top of each stack assuming each move
        is done all at once
        """
        return self.calculate_moves(True)

    def calculate_moves(self, is_part_2: bool) -> str:
        self.lines.seek(0,0)
        nextline = self.lines.readline()
        crates = []
        col_count = 0
        set_col_count = False
        while(nextline != '\n'):
            unparsed_crates = nextline.strip("\n")
            crate_index = 0
            column_index = 0
            while(crate_index < len(unparsed_crates)):
                crate = unparsed_crates[crate_index:crate_index + 3]
                if (crate[0] == '['):
                    crates.append(Crate(crate[1], column_index))
                column_index += 1
                crate_index += 4
            if not set_col_count:
                col_count = column_index
                set_col_count = True
            nextline = self.lines.readline()
        crates.reverse()
        stacks = SupplyStacks(crates, col_count)
        nextline = self.lines.readline()
        while(nextline != ''):
            command = nextline.strip("\n").split(" ")
            if (is_part_2):
                stacks.process_command_single_move(int(command[1]), int(command[3]), int(command[5]))
            else:
                stacks.process_command_multiple_moves(int(command[1]), int(command[3]), int(command[5]))
            nextline = self.lines.readline()
        return stacks.get_top_crates()
        