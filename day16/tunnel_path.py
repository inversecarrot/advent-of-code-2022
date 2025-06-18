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
    best_paths: Dict[Tuple[int, Set[str]], int]
    max: int

# a path is a list of edges in order with the path's total value at each step
# along with the open valves
# do valves need to have timestamps?
@dataclass
class TunnelPath:
    cur: str
    path: List[str]
    open_valves: Set[str]
    value: int
    time: int