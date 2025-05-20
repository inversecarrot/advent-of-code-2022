import logging

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day9.day9 import Day9
from day9.rope_grid import RopeGrid

class Day9Part2TestCase(AdventDayUnitTestCase):
    INPUT_FILE = 'day9long.txt'

    day: Day9    

    def setUp(self):
        super().setUp(self.INPUT_FILE)
        logging.basicConfig(level = logging.DEBUG)
        self.day = Day9(self.input, debug=True)

    def test_part_two(self):
        self.assertEqual(self.day.part2(), 36, "Incorrect part 1 answer")
