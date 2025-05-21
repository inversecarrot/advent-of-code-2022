from dataclasses import dataclass
from enum import Enum


class InstructionType(Enum):
    NOOP = 0
    ADDX = 1

@dataclass
class Instruction:
    type: InstructionType
    value: int | None = None

class Circuit:
    value: int
    cycle: int
    
    def __init__(self):
        self.value = 0
        self.cycle = 0
        
    