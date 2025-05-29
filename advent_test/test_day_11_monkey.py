import logging
import unittest

from day11.monkey import Monkey, MonkeyOperation, MonkeyOperationType

class Day11CircuitTestCase(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level = logging.DEBUG)

    def test_init(self):
        monkey = Monkey([
            "Monkey 0:",
            "Starting items: 79, 98",
            "Operation: new = old * 19",
            "Test: divisible by 23",
            "If true: throw to monkey 2",
            "If false: throw to monkey 3",
        ])
        self.assertEqual(monkey.name, 0, "Incorrect name")
        self.assertEqual(monkey.items, [79, 98], "Incorrect starting items")
        pass
        self.assertEqual(monkey.operation, MonkeyOperation(MonkeyOperationType.MULT, 19))
        self.assertEqual(monkey.test.divisor, 23, "Incorrect test divisor")
        self.assertEqual(monkey.test.true_target, 2, "Incorrect true condition")
        self.assertEqual(monkey.test.false_target, 3, "Incorrect false condition")
        monkey = Monkey([
            "Monkey 2:",
            "Starting items: 79, 60, 97",
            "Operation: new = old * old",
            "Test: divisible by 13",
            "If true: throw to monkey 1",
            "If false: throw to monkey 3",
        ])
        self.assertEqual(monkey.operation, MonkeyOperation(MonkeyOperationType.EXP, 2))
