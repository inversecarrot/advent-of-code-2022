import logging
from unittest import mock

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day13.day13 import Day13, Pair, comparePackets

class Day13TestCase(AdventDayUnitTestCase):
    INPUT_FILE = 'day13.txt'

    def setUp(self):
        super().setUp(self.INPUT_FILE)
        logging.basicConfig(level = logging.DEBUG)

    @mock.patch.object(Pair, '__new__')
    def test_parse_input(self, mockPair):
        day = Day13(self.input)
        self.assertEqual(len(day.pairs), 8, "Incorrect # of packet pairs")
        mockPair.assert_called_with(
            mock.ANY,
            [1,[2,[3,[4,[5,6,7]]]],8,9],
            [1,[2,[3,[4,[5,6,0]]]],8,9]
        )

    def test_compare_packet(self):
        self.assertLessEqual(comparePackets([1], [2]), -1, "Incorrect int comparison case")
        self.assertLessEqual(comparePackets([1],[1,1]), -1, "Incorrect handling of different lengths")
        self.assertLessEqual(comparePackets([[1]], [2]), -1, "Incorrect handle of left list right not list case")
        self.assertEqual(comparePackets([1], [[1]]), 0, "Incorrect handle of left int right  list case")
        self.assertGreaterEqual(comparePackets([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]), 1, "Incorrect complex case")
        

    def test_part_1(self):
        day = Day13(self.input)
        self.assertEqual(day.part1(), "13", "Incorect part 1 answer")

    def test_part_2(self):
        day = Day13(self.input)
        self.assertEqual(day.part2(), "140", "Incorect part 2 answer")
        pass