from dataclasses import dataclass
from enum import Enum
import logging
from typing import List, Tuple

log = logging.getLogger(__name__)


class InstructionType(Enum):
    NOOP = 0
    ADDX = 1

@dataclass
class Instruction:
    type: InstructionType
    value: int | None = None

class Circuit:
    CYCLE_VALUES = {InstructionType.NOOP: 1, InstructionType.ADDX: 2}
    value: int
    cycle: int
    instruction_in_progress: Tuple[Instruction, int]| None
    last_finished_instruction: Tuple[Instruction, int] | None
    
    def __init__(self):
        self.X = 1
        self.cycle = 0
        self.instruction_in_progress = None
        self.last_finished_instruction = None

    def executeInstruction(self, instruction: Instruction):
        match instruction.type:
            case InstructionType.NOOP:
                self.cycle += self.CYCLE_VALUES[instruction.type]
                self.last_finished_instruction = (instruction, self.cycle)
            case InstructionType.ADDX:
                self.X += instruction.value
                self.cycle += self.CYCLE_VALUES[instruction.type]
                self.last_finished_instruction = (instruction, self.cycle)

    def finishStoredInstruction(self):
        if self.instruction_in_progress is not None:
            self.cycle -= self.instruction_in_progress[1]
            self.executeInstruction(self.instruction_in_progress[0])
            self.instruction_in_progress = None
        

    def getSignalStrength(self) -> int:
        val = self.X
        if self.last_finished_instruction is not None and self.last_finished_instruction[1] == self.cycle and self.last_finished_instruction[0].type == InstructionType.ADDX:
            val -= self.last_finished_instruction[0].value
        log.debug(f"Strength during {self.cycle} is {self.cycle * val} (X is {self.X})")
        return val * self.cycle
    
    # Executes instructions until cycle would exceed limit
    # returns number of instructions executed including partial ones
    def executeInstructionsUntilCycle(self, instructions: List[Instruction], limit: int) -> int:
        executed = 0
        for instruction in instructions:
            # Check if we can execute this instruction
            if self.cycle + self.CYCLE_VALUES[instruction.type] > limit:
                # see if we need to partially execute this instruction
                if self.cycle < limit:
                    # store instruction and how many cycles of this instruction have
                    # been executed
                    self.instruction_in_progress = (instruction, limit - self.cycle)
                    self.cycle = limit
                    executed += 1
                break
            self.executeInstruction(instruction)
            executed += 1
        return executed
    
    def reset(self):
        self.cycle = 0
        self.X = 1
        self.instruction_in_progress = None

        
    