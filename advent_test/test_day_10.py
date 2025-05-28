import logging

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day10.circuit import InstructionType
from day10.day10 import Day10


class Day10TestCase(AdventDayUnitTestCase):
    INPUT_FILE = 'day10.txt'

    day: Day10

    def setUp(self):
        super().setUp(self.INPUT_FILE)
        logging.basicConfig(level = logging.DEBUG)
        self.day = Day10(self.input)

    # Check if we are making instructions correctly
    def test_parse_instructions(self):
        self.assertEqual(len(self.day.instructions), 146)
        self.assertEqual(self.day.instructions[0].type, InstructionType.ADDX)
        self.assertEqual(self.day.instructions[0].value, 15)
        self.assertEqual(self.day.instructions[1].type, InstructionType.ADDX)
        self.assertEqual(self.day.instructions[1].value, -11)
        self.assertEqual(self.day.instructions[len(self.day.instructions) - 1].type, InstructionType.NOOP)

    def test_part_1(self):
        self.assertEqual(self.day.part1(), "13140", "Part 1 test answer is incorrect")

    def test_part_2(self):
        self.assertEqual(
            self.day.part2(),
"""
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
""",
            "Part 2 test answer is incorrect"
        )