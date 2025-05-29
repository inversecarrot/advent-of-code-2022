import logging

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day11.day11 import Day11
from day11.monkey import Monkey
import unittest.mock as mock


class Day11TestCase(AdventDayUnitTestCase):
    INPUT_FILE = 'day11.txt'

    def setUp(self):
        super().setUp(self.INPUT_FILE)
        logging.basicConfig(level = logging.DEBUG)

    
    @mock.patch.object(Monkey, '__new__')
    def test_parse_input(self, mockMonkey):
        # mockMonkey.return_value = 
        day = Day11(self.input)
        self.assertEqual(len(day.monkeys), 4, "Incorrect number of monkeys")
        mockMonkey.assert_called_with(
            mock.ANY,
            [
            "Monkey 3:",
            "Starting items: 74",
            "Operation: new = old + 3",
            "Test: divisible by 17",
            "If true: throw to monkey 0",
            "If false: throw to monkey 1"
            ])
        
        pass