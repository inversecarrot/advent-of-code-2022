from io import TextIOWrapper
import logging
from typing import List
from advent_day import AdventDay
from day11.monkey import Monkey

log = logging.getLogger(__name__)


class Day11(AdventDay):

    monkeys: List[Monkey]
    monkeyModuloProduct: int
    input: TextIOWrapper

    def __init__(self, input: TextIOWrapper):
        super().__init__(input)
        self.input = input
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

        monkeyModuloProduct = 1
        for monkey in self.monkeys:
            monkeyModuloProduct = monkeyModuloProduct * monkey.test.divisor
        self.monkeyModuloProduct = monkeyModuloProduct

    def resetMonkeys(self):
        self.input.seek(0,0)
        self._parse_input(self.input)
        
    def part1(self):
        self.resetMonkeys()
        rounds = 20
        for _ in range(0, rounds):
            for monkey in self.monkeys:
                monkey.takeTurn(self.monkeys)
        activities = [m.activity for m in self.monkeys]
        activities.sort(reverse=True)
        return str(activities[0] * activities[1])
    
    def part2(self):
        self.resetMonkeys()
        rounds = 10000
        for r in range(0, rounds):
            for monkey in self.monkeys:
                # Can't keep track of items with actual values so we can use product mod the product of all divisors
                monkey.takeTurn(self.monkeys, False, self.monkeyModuloProduct)
        activities = [m.activity for m in self.monkeys]
        activities.sort(reverse=True)
        return str(activities[0] * activities[1])