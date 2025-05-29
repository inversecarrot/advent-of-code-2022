from dataclasses import dataclass
from enum import Enum
from typing import List

class MonkeyOperationType(Enum):
    ADD = 0
    MULT = 1
    EXP = 2

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
            self.operation = MonkeyOperation(MonkeyOperationType.EXP, 2)
        else:
            self.operation = MonkeyOperation(MonkeyOperationType.MULT, int(operation[1]))

        self.test = MonkeyTest(
            divisor=int(initial_state[3].removeprefix("Test: divisible by ")),
            true_target=int(initial_state[4].removeprefix("If true: throw to monkey ")),
            false_target=int(initial_state[5].removeprefix("If false: throw to monkey "))
        )
