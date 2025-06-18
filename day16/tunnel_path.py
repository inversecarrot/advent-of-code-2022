from dataclasses import dataclass
from typing import Dict, List, Set, Tuple

@dataclass
class Valve:
    name: str
    flow_rate: int
    neighbors: List[str]

@dataclass
class ValveNode:
    valve: Valve
    best_paths: Dict[Set[str], int]
    max: int

@dataclass
class EleValveNode:
    valve: Valve
    best_paths: Dict[Tuple[Set[str], Set[str]], int]
    max: int

# a path is a list of edges in order with the path's total value at each step
# along with the open valves
@dataclass
class TunnelPath:
    cur: str
    open_valves: Set[str]
    value: int
    time: int
    ele_cur: str = None
    ele_open_valves: Set[str] = None