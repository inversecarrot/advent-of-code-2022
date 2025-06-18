from collections import deque
from io import TextIOWrapper
import logging
from typing import Dict, List
from advent_day import AdventDay
from day16.tunnel_path import TunnelPath, Valve, ValveNode

log = logging.getLogger(__name__)

class Day16(AdventDay):
    input: TextIOWrapper
    valves: List[Valve]

    def __init__(self, input: TextIOWrapper):
        super().__init__(input)
        self.input = input
        self._parse_input(input)

    def _parse_input(self, input: TextIOWrapper):
        self.valves = []
        for line in input:
            [valvestr, neighborsstr] = line.strip("\n").split("; ")
            [namestr, flowstr] = valvestr.split(" has flow rate=")
            name = namestr.removeprefix("Valve ")
            flow_rate = int(flowstr)
            neighbors = neighborsstr.removeprefix("tunnels lead to valves ").removeprefix("tunnel leads to valve ").split(", ")
            self.valves.append(Valve(name, flow_rate, neighbors))

    def _should_trim_path(self, path: TunnelPath, node: ValveNode) -> bool:
        if frozenset(path.open_valves) not in node.best_paths.keys():
            for vs in node.best_paths.keys():
                if vs.issuperset(path.open_valves):
                    return True
            return False
        elif path.value > node.best_paths[frozenset(path.open_valves)]:
            return False
        return True

    def part1(self):
        max_time = 30
        valve_nodes: Dict[str, ValveNode] = {}
        for valve in self.valves:
            valve_nodes[valve.name] = ValveNode(valve, {}, -1)
        paths = deque([])
        next_path = TunnelPath(
                cur="AA",
                open_valves=set([]),
                value=0,
                time=0
            )

        while next_path != None and next_path.time < max_time:
            node = valve_nodes[next_path.cur]
            if not self._should_trim_path(next_path, node):
                # update the highest value seen for this time

                node.best_paths[frozenset(next_path.open_valves)] = next_path.value
                node.max = max(node.max, next_path.value)

                # get all next possible moves
                moves = node.valve.neighbors.copy()
                if next_path.cur not in next_path.open_valves and node.valve.flow_rate > 0:
                    moves.append("O")
                
                # make new paths
                for move in moves:
                    new_path = TunnelPath(
                            cur=move,
                            open_valves=next_path.open_valves.copy(),
                            value=next_path.value,
                            time=next_path.time + 1
                        )
                    # if we are opening a valve, do some special stuff
                    if move == "O":
                        new_path.cur = next_path.cur
                        new_path.open_valves.add(next_path.cur)
                        new_path.value += (max_time - new_path.time) * node.valve.flow_rate

                    paths.append(new_path)
            if len(paths) > 0:
                next_path = paths.popleft()
            else:
                next_path = None
        max_val = 0
        for node in valve_nodes:
            if valve_nodes[node].max > max_val:
                max_val = valve_nodes[node].max
        return str(max_val)

    def part2(self):
        max_time = 30
        valve_nodes: Dict[str, ValveNode] = {}
        for valve in self.valves:
            valve_nodes[valve.name] = ValveNode(valve, {}, -1)
        paths = deque([])
        next_path = TunnelPath(
                cur="AA",
                ele_cur="AA",
                open_valves=set([]),
                value=0,
                time=0,
            )
        while next_path != None and next_path.time < max_time:
            node = valve_nodes[next_path.cur]
            ele_node = valve_nodes[next_path.ele_cur]
            if (not self._should_trim_path(next_path, node)) or (not self._should_trim_path(next_path, ele_node)):
                # update the highest value seen for this time
                cur_best = -1
                if frozenset(next_path.open_valves) in node.best_paths.keys():
                    cur_best = node.best_paths[frozenset(next_path.open_valves)]
                node.best_paths[frozenset(next_path.open_valves)] = max(cur_best, next_path.value)
                node.max = max(node.max, next_path.value)

                ele_best = -1
                if frozenset(next_path.open_valves) in ele_node.best_paths.keys():
                    ele_best = ele_node.best_paths[frozenset(next_path.open_valves)]
                ele_node.best_paths[frozenset(next_path.open_valves)] = max(ele_best, next_path.value)
                ele_node.max = max(ele_node.max, next_path.value)

                # get all next possible moves
                moves = node.valve.neighbors.copy()
                ele_moves = ele_node.valve.neighbors.copy()
                if next_path.cur not in next_path.open_valves and node.valve.flow_rate > 0:
                    moves.append("O")
                
                if next_path.ele_cur not in next_path.open_valves and ele_node.valve.flow_rate > 0:
                    ele_moves.append("O")
                
                # make new paths
                for move in moves:
                    for ele_move in ele_moves:
                        new_path = TunnelPath(
                                cur=move,
                                ele_cur=ele_move,
                                open_valves=next_path.open_valves.copy(),
                                value=next_path.value,
                                time=next_path.time + 1
                            )
                        # if we are opening a valve, do some special stuff
                        if move == "O":
                            new_path.cur = next_path.cur
                            new_path.open_valves.add(next_path.cur)
                            new_path.value += (max_time - new_path.time) * node.valve.flow_rate

                        if ele_move == "O":
                            new_path.ele_cur = next_path.ele_cur
                            new_path.open_valves.add(next_path.ele_cur)
                            new_path.value += (max_time - new_path.time) * ele_node.valve.flow_rate

                    paths.append(new_path)
            if len(paths) > 0:
                next_path = paths.popleft()
            else:
                next_path = None

        max_val = 0
        for node in valve_nodes:
            if valve_nodes[node].max > max_val:
                max_val = valve_nodes[node].max
        return str(max_val)