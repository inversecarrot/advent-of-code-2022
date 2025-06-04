import logging

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day12.day12 import Day12

class Day12TestCase(AdventDayUnitTestCase):
    INPUT_FILE = 'day12.txt'

    def setUp(self):
        super().setUp(self.INPUT_FILE)
        logging.basicConfig(level = logging.DEBUG)


    def test_parse_input(self):
        day = Day12(self.input)
        self.assertEqual(len(day.topography), 5, "Incorrect # of rows")
        self.assertEqual(len(day.topography[0]), 8, "Incorrect # of columns")
        self.assertEqual(day.topography[4][7].path_length, -1, "Incorrect initial value for bottom right corner")
        self.assertEqual(day.topography[4][7].height, "i", "Incorrect height for bottom right corner")
        self.assertEqual(day.start_coord, (0,0), "Incorrect start position")
        self.assertEqual(day.end_coord, (5, 2), "Incorrect end coordinate")

    def test_part_1(self):
        day = Day12(self.input)
        self.assertEqual(day.part1(), "31", "Incorrect part 1 answer")

    def test_part_2(self):
        day = Day12(self.input)
        self.assertEqual(day.part2(), "29", "Incorrect part 1 answer")
                    