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

    def takeTurn(self, monkeys: List[Self], worryDecrease = True, moduloProduct = -1):
        for item in self.items:
            item = self._inspectItem(item, worryDecrease, moduloProduct)
            self._throwItem(item, monkeys)
        self.items = []
        pass

    def _inspectItem(self, item: int, worryDecrease: bool, moduloProduct = -1) -> int:
        self.activity += 1
        match self.operation.type:
            case MonkeyOperationType.ADD:
                item += self.operation.value
            case MonkeyOperationType.MULT:
                item *= self.operation.value
            case MonkeyOperationType.SQUARE:
                item = item * item
        if worryDecrease:
            item = item // 3
        if moduloProduct != -1:
            # prevent worry values from becoming huge but still preserve all tests
            item = item % moduloProduct
        return item
    
    def _throwItem(self, item: int, monkeys: List[Self]):
        target: int
        if item % self.test.divisor == 0:
            target = self.test.true_target
        else:
            target = self.test.false_target
        monkeys[target].items.append(item)
        pass

