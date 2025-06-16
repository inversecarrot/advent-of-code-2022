import logging

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day15.day15 import Day15, Sensor

class Day15TestCase(AdventDayUnitTestCase):
    INPUT_FILE = 'day15.txt'

    def setUp(self):
        super().setUp(self.INPUT_FILE)
        logging.basicConfig(level = logging.DEBUG)


    def test_parse_input(self):
        day = Day15(self.input, y = 10)
        self.assertEqual(len(day.sensors), 14, "Incorrect # of sensors")
        self.assertEqual(day.sensors[0].radius, 7, "Incorrect radius calculation")

    def test_get_no_beacon_in_row(self):
        s = Sensor((8,7), (2,10))
        self.assertEqual(s.radius, 9, "Incorrect radius on sensor")
        self.assertEqual(s.getNoBeaconInRow(7), [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
        pass

    def test_part_1(self):
        day = Day15(self.input, y = 10)
        self.assertEqual(day.part1(), "26", "Incorrect part 1 answer")

    def test_part_2(self):
        day = Day15(self.input, y = 10)
        self.assertEqual(day.part2(20, 20), "56000011", "Incorrect part 2 answer")
        pass