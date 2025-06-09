from functools import cmp_to_key
from io import TextIOWrapper
import logging
from typing import List, Tuple
from advent_day import AdventDay

log = logging.getLogger(__name__)

type Packet = List[int | Packet]

def comparePackets(left: Packet, right: Packet):
    min_length = min(len(left), len(right))
    for i in range(0, min_length):
        l = left[i]
        r = right[i]

        if isinstance(l, int):
            # handle both integer case
            if isinstance(r, int):
                if l < r:
                    return -1
                elif l > r:
                    return 1
                else:
                    continue
            # handle int l, list r case
            else:
                cmp = comparePackets([l], r)
                if cmp != 0:
                    return cmp
                continue
        # handle list l, int r case
        if isinstance(r, int):
            cmp = comparePackets(l, [r])
            if cmp != 0:
                return cmp
            continue
        # only case left is list l, list r case
        cmp = comparePackets(l,r)
        if cmp != 0:
            return cmp
    # at this point, all list elements we checked are equal
    # so we return the difference between lengths
    # will be positive if l is longer, 0 if equal, negative if r is longer
    return len(left) - len(right)

class Pair:
    first: Packet
    second: Packet

    def __init__(self, first: Packet, second: Packet):
        self.first = first
        self.second = second

    def isOrdered(self):
        cmp = comparePackets(self.first, self.second)
        if cmp < 0:
            return True
        return False

class Day13(AdventDay):
    input: TextIOWrapper
    pairs: List[Pair]

    def __init__(self, input: TextIOWrapper):
        super().__init__(input)
        self.input = input
        self._parse_input(input)

    def _parse_input(self, input: TextIOWrapper):
        self.pairs = []
        lines = input.readlines()
        first = None
        second = None
        for line in lines:
            if line != "\n":
                if first is None:
                    first = self._parse_line(line.strip("\n"))
                else:
                    second = self._parse_line(line.strip("\n"))
                    self.pairs.append(Pair(first, second))
                    first = None
                    second = None

    def _parse_line(self, line: str) -> Packet:
        # strip leading and trailing bracket
        line = line[1:len(line) - 1]
        pieces = line.split(',')
        tmp = ""
        res = []
        for piece in pieces:
            if tmp != "" or ("[" in piece or "]" in piece):
                if tmp == "":
                    tmp = tmp + piece
                else:
                    tmp = tmp + "," + piece
                if tmp.count("[") == tmp.count("]"):
                    res.append(self._parse_line(tmp))
                    tmp = ""
            elif piece != "":
                res.append(int(piece))
        return res

    def part1(self):
        index_sum = 0
        for i in range(len(self.pairs)):
            if self.pairs[i].isOrdered():
                index_sum += i + 1
        return str(index_sum)


    def part2(self):
        packets = []
        for pair in self.pairs:
            packets.append(pair.first)
            packets.append(pair.second)
        packets.append([[2]])
        packets.append([[6]])
        sorted_packets = sorted(packets, key=cmp_to_key(comparePackets))
        first = 0
        second = 0
        for i in range(0, len(sorted_packets)):
            if sorted_packets[i] == [[2]]:
                first = i + 1
            elif sorted_packets[i] == [[6]]:
                second = i + 1
        return str(first * second)