from io import TextIOWrapper
from typing import List
from advent_day import AdventDay
from day10.circuit import Circuit, Instruction, InstructionType


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
        # strengths = circuit.process_and_record_strengths(20, 40)
        return ""

    def part2(self):
        return ""