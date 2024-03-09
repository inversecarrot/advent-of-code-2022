"""
Defines supply stacks object for day 5
"""
from dataclasses import dataclass
from typing import List

@dataclass
class Crate:
    """
        Represents a crate with a name and a column, used for constructing a
        SupplyStack.
    """
    name: str
    column: int

class SupplyStacks:
    """
        Represents a set of supply stacks from the format
            [D]    
        [N] [C]    
        [Z] [M] [P]
        1   2   3 
        where each letter is a crate, and each column is a stack.
        Keeps track of all stacks and can move n crates from stack
        to stack.
    """
    stacks: List[List[str]]
    def __init__(self, crates: List[Crate], column_count: int) -> None:
        self.stacks = [[] for _ in range(0, column_count)]
        for crate in crates:
            self.stacks[crate.column].append(crate.name)

    def process_command_multiple_moves(self, count: int, src: int, dst: int) -> None:
        """
            Moves count crates from column src to dst one at a time
        """
        if (count > len(self.stacks[src - 1])):
            count = len(self.stacks[src - 1])
        while(count > 0):
            self.stacks[dst - 1].append(self.stacks[src - 1].pop())
            count -= 1

    def process_command_single_move(self, count: int, src: int, dst: int) -> None:
        """
            Moves count crates from column src to dst all at once
        """
        src_len = len(self.stacks[src - 1])
        if (count > src_len):
            count = src_len
        crates_to_move = self.stacks[src - 1][src_len - count:src_len]
        self.stacks[src - 1] = self.stacks[src - 1][0:src_len - count]
        self.stacks[dst - 1].extend(crates_to_move)

    def get_top_crates(self) -> str:
        """
            Returns a string representing the top crate on each stack
        """
        return "".join(stack[len(stack) - 1] if len(stack) > 0 else "" for stack in self.stacks)
