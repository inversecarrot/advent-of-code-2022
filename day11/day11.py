from io import TextIOWrapper
import logging
from typing import List
from advent_day import AdventDay
from day11.monkey import Monkey

log = logging.getLogger(__name__)


class Day11(AdventDay):

    monkeys: List[Monkey]

    def __init__(self, input: TextIOWrapper):
        super().__init__(input)
        self._parse_input(input)

    def _parse_input(self, input: TextIOWrapper):
        monkey_state = []
        self.monkeys = []
        for line in input:
            if line != "\n":
                monkey_state.append(line.strip(" \n"))
                if len(monkey_state) == 6:
                    self.monkeys.append(Monkey(monkey_state))
                    monkey_state  = []
        return