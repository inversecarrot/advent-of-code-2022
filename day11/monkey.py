import logging
from dataclasses import dataclass
from enum import Enum
from typing import List, Self

log = logging.getLogger(__name__)

class MonkeyOperationType(Enum):
    ADD = 0
    MULT = 1
    SQUARE = 2

@dataclass
class MonkeyOperation:
    type: MonkeyOperationType
    value: int

@dataclass
class MonkeyTest:
    divisor: int
    true_target: int
    false_target: int

class Monkey:
    name: int
    items: List[int]
    activity: int
    operation: MonkeyOperation
    test: MonkeyTest

    def __init__(self, initial_state: List[str]):
        self.activity = 0
        self._parseInitialState(initial_state)


    def _parseInitialState(self, initial_state: List[str]):
        self.name = int(initial_state[0]
                        .removeprefix("Monkey ")
                        .removesuffix(":"))
        
        self.items = [int(x) for x in initial_state[1]
                      .removeprefix("Starting items: ")
                      .split(", ")]
        
        operation = initial_state[2].removeprefix("Operation: new = old ").split(" ")
        if operation[0] == "+":
            self.operation = MonkeyOperation(MonkeyOperationType.ADD, int(operation[1]))
        elif operation[1] == "old":
            self.operation = MonkeyOperation(MonkeyOperationType.SQUARE, 0)
        else:
            self.operation = MonkeyOperation(MonkeyOperationType.MULT, int(operation[1]))

        self.test = MonkeyTest(
            divisor=int(initial_state[3].removeprefix("Test: divisible by ")),
            true_target=int(initial_state[4].removeprefix("If true: throw to monkey ")),
            false_target=int(initial_state[5].removeprefix("If false: throw to monkey "))
        )

    def takeTurn(self, monkeys: List[Self], worryDecrease = True):
        # log.debug(f"Monkey {self.name}:")
        for item in self.items:
            # log.debug(f"\tMonkey inspects item with worry level {item}")
            item = self._inspectItem(item, worryDecrease)
            self._throwItem(item, monkeys)
        self.items = []
        pass

    def _inspectItem(self, item: int, worryDecrease: bool) -> int:
        self.activity += 1
        match self.operation.type:
            case MonkeyOperationType.ADD:
                item += self.operation.value
                # log.debug(f"\t\tWorry level increases by {self.operation.value} to {item}")
            case MonkeyOperationType.MULT:
                item *= self.operation.value
                # log.debug(f"\t\tWorry level is multiplied by {self.operation.value} to {item}")
            case MonkeyOperationType.SQUARE:
                # log.debug(f"\t\tWorry level is raised to power of {self.operation.value} to {item}")
                item = item * item
        if worryDecrease:
            # log.debug(f"\t\tMonkey gets bored, worry level decreases to {item // 3}")
            item = item // 3
        return item
    
    def _throwItem(self, item: int, monkeys: List[Self]):
        target: int
        if item % self.test.divisor == 0:
            # log.debug(f"\t\tItem is divisible by {self.test.divisor}")
            target = self.test.true_target
        else:
            # log.debug(f"\t\tItem is not divisible by {self.test.divisor}")
            target = self.test.false_target
        # log.debug(f"\t\tItem with worry {item} is thrown to monkey {target}")
        monkeys[target].items.append(item)
        pass

