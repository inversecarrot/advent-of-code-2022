import logging
import unittest

from day11.monkey import Monkey, MonkeyOperation, MonkeyOperationType

class Day11MonkeyTestCase(unittest.TestCase):
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
        self.assertEqual(monkey.operation.type, MonkeyOperationType.SQUARE)

    def test_take_turn(self):
        monkeys = [
            Monkey(
            [
                "Monkey 0:",
                "Starting items: 79, 98",
                "Operation: new = old * 19",
                "Test: divisible by 23",
                "If true: throw to monkey 1",
                "If false: throw to monkey 2",
            ]),
            Monkey(
            [
                "Monkey 1:",
                "Starting items: 76, 92, 53, 93, 79, 86, 81",
                "Operation: new = old + 4",
                "Test: divisible by 2",
                "If true: throw to monkey 0",
                "If false: throw to monkey 2",
            ]),
            Monkey(
            [
                "Monkey 2:",
                "Starting items: 58, 67, 66",
                "Operation: new = old * old",
                "Test: divisible by 7",
                "If true: throw to monkey 0",
                "If false: throw to monkey 1",
            ]),
        ]
        monkeys[0].takeTurn(monkeys)
        self.assertEqual(len(monkeys[0].items), 0, "Monkey should inspect all items")
        self.assertEqual(len(monkeys[2].items), 5, "Monkey 0 should throw both items to monkey 2")
        self.assertEqual(monkeys[2].items[3], 500, "Incorrect value for first thrown item")
