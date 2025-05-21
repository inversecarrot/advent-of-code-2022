import logging

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day10.circuit import Circuit, InstructionType


class Day10CircuitTestCase(AdventDayUnitTestCase):
    INPUT_FILE = 'day9.txt'

    circuit: Circuit

    def setUp(self):
        super().setUp(self.INPUT_FILE)
        # logging.basicConfig(level = logging.DEBUG)
        # self.circuit = Circuit(self.input)

    # Test if we are setting up the instructions correctly
    