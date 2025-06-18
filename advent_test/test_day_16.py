import logging

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day16.day16 import Day16
from day16.tunnel_path import Valve

class Day16TestCase(AdventDayUnitTestCase):
    INPUT_FILE = 'day16.txt'

    def setUp(self):
        super().setUp(self.INPUT_FILE)
        logging.basicConfig(level = logging.DEBUG)


    def test_parse_input(self):
        day = Day16(self.input)
        self.assertEqual(len(day.valves), 10, "Incorrect # of valves")
        self.assertEqual(day.valves[0], Valve("AA", 0, ["DD", "II", "BB"]), "Incorrect valve data")
        self.assertEqual(day.valves[7], Valve("HH", 22, ["GG"]), "Incorrect handling of singular edge")

    def test_part_1(self):
        day = Day16(self.input)
        self.assertEqual(day.part1(), "1651")
        pass

    def test_part_2(self):
        day = Day16(self.input)
        self.assertEqual(day.part2(), "1707")
        pass