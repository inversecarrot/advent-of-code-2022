import unittest

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day9.day9 import Day9

class Day9TestCase(AdventDayUnitTestCase):
    day: Day9
    INPUT_FILE = 'day9.txt'
    def setUp(self):
        super().setUp(self.INPUT_FILE)
        self.day = Day9(self.input)

    def test_rope_grid_parse_input(self):
        self.assertEqual(self.day.grid._parse_move("U 2\n"), [(1, 0), (1, 0)], "Move does not parse into correct list")

    def test_rope_grid_get_tail_position_basic(self):
        self.assertEqual(self.day.grid._get_tail_position((0,0), (0,0)), (0,0), "Tail should stay if head is on top")
        self.assertEqual(self.day.grid._get_tail_position((1,0), (0,0)), (0,0), "Tail should stay if head is only one step away")
        self.assertEqual(self.day.grid._get_tail_position((4,2), (2,2)), (3,2), "Tail should move up")
        self.assertEqual(self.day.grid._get_tail_position((3,1), (5,1)), (4,1), "Tail should move down")
        self.assertEqual(self.day.grid._get_tail_position((2,4), (2,2)), (2,3), "Tail should move right")
        self.assertEqual(self.day.grid._get_tail_position((0,0), (0,2)), (0,1), "Tail should move left")

    def test_rope_grid_get_tail_position_diagonal(self):
        self.assertEqual(self.day.grid._get_tail_position((1,1), (0,0)), (0,0), "Tail should stay if head is only one step diagonally")
        self.assertEqual(self.day.grid._get_tail_position((2,1), (0,0)), (1,1), "Tail should move NE if head is two up and one right")
        self.assertEqual(self.day.grid._get_tail_position((0,2), (1,0)), (0,1), "Tail should move NW if head is two up one left")
        self.assertEqual(self.day.grid._get_tail_position((0,0), (1,2)), (0,1), "Tail should move SW if head is two down and one right")
        
    
    def test_part_one(self):
        self.assertEqual(self.day.part1(), 13, "Incorrect part 1 answer")

    

    # def test_part_two(self):
    #     self.assertEqual(self.day.part2(), "WHO KNOWS", "Incorrect part 2 answer")
    
