import logging
from unittest import mock

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day14.cave import Cave
from day14.day14 import Day14

class Day14TestCase(AdventDayUnitTestCase):
    INPUT_FILE = 'day14.txt'

    def setUp(self):
        super().setUp(self.INPUT_FILE)
        logging.basicConfig(level = logging.DEBUG)

    def test_parse_input(self):
        day = Day14(self.input)  
        self.assertEqual(day.lines, 
                         [
                             [(498,4), (498,6), (496,6)],
                             [(503,4), (502,4), (502,9), (494,9)]
                         ], 
                         "Incorrect parse result")
        self.assertEqual(day.min_x, 494,"Incorrect min x")
        self.assertEqual(day.max_x, 503, "Incorrect max x")
        self.assertEqual(day.max_y, 9, "Incorrect max y")

    def test_cave(self):
        day = Day14(self.input)
        cave = Cave(day.min_x, day.max_x, day.max_y, day.lines)
        self.assertEqual(cave.grid.get(cave.grid.x_offset, cave.grid.y_offset), '.', "Incorrect origin")
        self.assertEqual(cave.grid.getWidth(), 10)
        self.assertEqual(cave.grid.getHeight(), 10)
        self.assertEqual(cave.grid.get(502, 6), "#", "Incorrect # placement")

    def test_part_1(self):
        day = Day14(self.input)
        self.assertEqual(day.part1(), "24", "Incorrect part 1 test answer")

    def test_part_2(self):
        day = Day14(self.input)
        self.assertEqual(day.part2(), "93", "Incorrect part 2 answer")