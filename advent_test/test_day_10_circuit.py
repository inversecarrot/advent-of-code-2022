import logging
import unittest

from advent_test.advent_day_test_case import AdventDayUnitTestCase
from day10.circuit import Circuit, Instruction, InstructionType
from day10.day10 import Day10


class Day10CircuitTestCase(unittest.TestCase):

    circuit: Circuit

    def setUp(self):
        logging.basicConfig(level = logging.DEBUG)
        self.circuit = Circuit()

    def test_base(self):
        self.circuit.reset()
        self.assertEqual(self.circuit.X, 1, "X should initialize to 1")
        self.assertEqual(self.circuit.cycle, 0, "Cycle should start at 0")
        self.circuit.executeInstruction(Instruction(type=InstructionType.NOOP))
        self.circuit.reset()
        self.assertEqual(self.circuit.cycle, 0)

    def test_noop(self):
        self.circuit.reset()
        self.circuit.executeInstruction(Instruction(type=InstructionType.NOOP))
        self.assertEqual(self.circuit.X, 1, "NOOP should not change value")
        self.assertEqual(self.circuit.cycle, 1, "NOOP should advance cycle")

    def test_addx(self):
        self.circuit.reset()
        self.circuit.executeInstruction(Instruction(type=InstructionType.ADDX, value=-4))
        self.assertEqual(self.circuit.X, -3, "X does not change correctly")
        self.assertEqual(self.circuit.cycle, 2, "ADDX should take two cycles")
        self.circuit.executeInstruction(Instruction(type=InstructionType.ADDX, value=16))
        self.assertEqual(self.circuit.X, 13, "ADDX should keep a running value")
        self.assertEqual(self.circuit.cycle, 4, "Cycle should continue to advance")
    
    def test_get_signal_strength(self):
        self.circuit.reset()
        self.circuit.executeInstruction(Instruction(type=InstructionType.ADDX, value=-4))
        self.circuit.executeInstruction(Instruction(type=InstructionType.NOOP))
        self.assertEqual(self.circuit.getSignalStrength(), -9, "Incorrect signal strength calculation")

    def test_execute_until_cycle(self):
        self.circuit.reset()
        instruction_list = [
            Instruction(type=InstructionType.NOOP),
            Instruction(type=InstructionType.ADDX, value=5),
            Instruction(type=InstructionType.ADDX, value=4)
        ]
        instructions_executed = self.circuit.executeInstructionsUntilCycle(instruction_list, 0)
        self.assertEqual(instructions_executed, 0, "Should not execute instructions when cycle is at limit")
        self.assertEqual(self.circuit.cycle, 0, "Should not execute instructions when cycle is at limit")
        instructions_executed = self.circuit.executeInstructionsUntilCycle(instruction_list, 5)
        self.assertEqual(instructions_executed, 3, "Should execute all instructions when cycle does not exceed limit")
        self.assertEqual(self.circuit.X, 10)
        self.circuit.reset()
        instructions_executed = self.circuit.executeInstructionsUntilCycle(instruction_list, 4)
        self.assertEqual(instructions_executed, 3, "Should still increment cycle when instruction cannot be fully executed")
        self.assertEqual(self.circuit.X, 6)
        self.circuit.finishStoredInstruction()
        self.assertEqual(self.circuit.cycle, 5, "Incorrect cycle value when executing stored instruction")
        self.assertEqual(self.circuit.X, 10, "Incorrect X when executing stored instruction")
        self.circuit.finishStoredInstruction()
        self.assertEqual(self.circuit.X, 10, "Incorrect X after repeated calls to execute stored instruction")
        instructions_executed = self.circuit.executeInstructionsUntilCycle([Instruction(type=InstructionType.NOOP)] * 2, 6)
        self.assertEqual(instructions_executed, 1, "Should execute NOOP until limit")
        self.assertEqual(self.circuit.cycle, 6)
        self.circuit.finishStoredInstruction()
        self.assertEqual(self.circuit.cycle, 6, "Instructions that exceed limit but do not start until limit should not be stored")

    def test_get_signal_strength(self):
        self.circuit.reset()
        instruction_list = [
            Instruction(type=InstructionType.ADDX, value=5),
            Instruction(type=InstructionType.ADDX, value=4),
            Instruction(type=InstructionType.NOOP),
        ]
        self.circuit.executeInstructionsUntilCycle(instruction_list, 5)
        self.assertEqual(self.circuit.getSignalStrength(), 50, "signal strength should be current cycle number * X")
        self.circuit.reset()
        instruction_list = [
            Instruction(type=InstructionType.NOOP),
            Instruction(type=InstructionType.ADDX, value=5),
            Instruction(type=InstructionType.ADDX, value=4)
        ]
        self.circuit.executeInstructionsUntilCycle(instruction_list, 5)
        self.assertEqual(self.circuit.getSignalStrength(), 30, "signal strength should measure middle of cycle")
    