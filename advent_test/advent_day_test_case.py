from io import TextIOWrapper
import unittest
class AdventDayUnitTestCase(unittest.TestCase):

    input: TextIOWrapper
    def setUp(self, input_file: str):
        self.input = open(f'advent_test/input/{input_file}', encoding="utf-8")

    def tearDown(self):
        self.input.close()
        return super().tearDown()
        