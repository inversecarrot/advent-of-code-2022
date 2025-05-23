from io import TextIOWrapper
import logging
from typing import List
from advent_day import AdventDay
from day10.circuit import Circuit, Instruction, InstructionType

log = logging.getLogger(__name__)


class Day10(AdventDay):
    instructions: List[Instruction]
    def __init__(self, input: TextIOWrapper):
        super().__init__(input)
        self._parse_input(input)

        
    def _parse_input(self, input: TextIOWrapper):
        self.instructions = []
        for line in input:
            instruction = line.strip("\n").split(" ")
            if instruction[0] == "addx":
                self.instructions.append(Instruction(InstructionType.ADDX, value = int(instruction[1])))
            elif instruction[0] == "noop":
                self.instructions.append(Instruction(InstructionType.NOOP))

    def part1(self):
        circuit = Circuit()
        limit = 20
        interval = 40
        strength_sum = 0
        idx = 0
        while idx < len(self.instructions) and circuit.cycle < limit:
            circuit.finishStoredInstruction()
            idx += circuit.executeInstructionsUntilCycle(self.instructions[idx:], limit)
            if circuit.cycle == limit:
                strength_sum += circuit.getSignalStrength()
            limit += interval
        return str(strength_sum)

    def part2(self):
        return ""