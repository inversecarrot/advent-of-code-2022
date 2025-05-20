import logging

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day9.day9 import Day9
from day9.rope_grid import RopeGrid

class Day9Part1TestCase(AdventDayUnitTestCase):
    INPUT_FILE = 'day9.txt'

    day: Day9    
    simple_grid: RopeGrid

    def setUp(self):
        super().setUp(self.INPUT_FILE)
        logging.basicConfig(level = logging.DEBUG)
        self.day = Day9(self.input, debug=True)
        self.simple_grid = RopeGrid(self.day.moves, debug=True)

    def test_rope_grid_parse_input(self):
        self.assertEqual(self.day.moves, [(1, 0)] * 4 + [(0,1)] * 4 + [(-1,0)] * 3 + [(0,-1)] + [(1,0)] * 4 + [(0, -1)] + [(-1,0)] * 5 + [(1, 0)] * 2, "Move does not parse into correct list")

    def test_rope_grid_get_tail_position_basic(self):
        self.assertEqual(self.simple_grid._get_tail_position((0,0), (0,0)), (0,0), "Tail should stay if head is on top")
        self.assertEqual(self.simple_grid._get_tail_position((1,0), (0,0)), (0,0), "Tail should stay if head is only one step away")
        self.assertEqual(self.simple_grid._get_tail_position((2,4), (2,2)), (2,3), "Tail should move up")
        self.assertEqual(self.simple_grid._get_tail_position((1,3), (1,5)), (1,4), "Tail should move down")
        self.assertEqual(self.simple_grid._get_tail_position((4,2), (2,2)), (3,2), "Tail should move right")
        self.assertEqual(self.simple_grid._get_tail_position((0,0), (2,0)), (1,0), "Tail should move left")

    def test_rope_grid_get_tail_position_diagonal(self):
        self.assertEqual(self.simple_grid._get_tail_position((1,1), (0,0)), (0,0), "Tail should stay if head is only one step diagonally")
        self.assertEqual(self.simple_grid._get_tail_position((1,2), (0,0)), (1,1), "Tail should move NE if head is two up and one right")
        self.assertEqual(self.simple_grid._get_tail_position((2,0), (0,1)), (1,0), "Tail should move NW if head is two up one left")
        self.assertEqual(self.simple_grid._get_tail_position((0,0), (2,1)), (1,0), "Tail should move SW if head is two down and one right")
        
    
    def test_part_one(self):
        self.assertEqual(self.day.part1(), 13, "Incorrect part 1 answer")
