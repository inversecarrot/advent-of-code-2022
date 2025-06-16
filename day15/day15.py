from dataclasses import dataclass
from io import TextIOWrapper
import logging
from typing import List, Tuple
from advent_day import AdventDay

log = logging.getLogger(__name__)

class Sensor:
    position: Tuple[int, int]
    beacon: Tuple[int, int]
    
    def __init__(self, pos: Tuple[int, int], beacon: Tuple[int, int]):
        self.position = pos
        self.beacon = beacon
        self.radius = getManhattanDistance(pos[0], pos[1], beacon[0], beacon[1])

    def getNoBeaconInRow(self, y: int) -> List[int]:
        x_values = []
        distance = self.radius - abs(y - self.position[1])
        if distance > 0:
            for x in range(self.position[0] - distance, self.position[0] + distance + 1):
                x_values.append(x)
        return x_values

def getManhattanDistance(x1: int, y1: int, x2: int, y2: int):
    return abs(x1 - x2) + abs(y1 - y2)

class Day15(AdventDay):
    input: TextIOWrapper
    sensors: List[Sensor]
    y: int

    def __init__(self, input: TextIOWrapper, y: int = 2000000):
        super().__init__(input)
        self.input = input
        self._parse_input(input)
        self.y = y

    def _parse_input(self, input: TextIOWrapper):
        self.sensors = []
        for line in input:
            line = line.strip("\n")
            [senstr, beastr] = line.split(": ")
            [sxstr, systr] = senstr.split(", ")
            senx = int(sxstr.removeprefix("Sensor at x="))
            seny = int(systr.removeprefix("y="))
            [bxstr, bystr] = beastr.split(", ")
            beax = int(bxstr.removeprefix("closest beacon is at x="))
            beay = int(bystr.removeprefix("y="))
            self.sensors.append(Sensor((senx,  seny), (beax, beay)))

    def part1(self):
        pts = set([])
        filled = set([])
        for sensor in self.sensors:
            pts = pts.union(sensor.getNoBeaconInRow(self.y))
            if sensor.position[1] == self.y:
                filled.add(sensor.position[0])
            if sensor.beacon[1] == self.y:
                filled.add(sensor.beacon[0])
        
        #removes points that are sensors or beacons
        pts = pts.difference(filled)

        return str(len(pts))


    def part2(self, xmax = 4000000, ymax = 4000000):
        pt = (-1, -1)
        x = 0
        y = 0
        while y <= ymax:
            while x <= xmax:
                f = True
                for sensor in self.sensors:
                    d = getManhattanDistance(x, y, sensor.position[0], sensor.position[1])
                    if d <= sensor.radius:
                        x = sensor.position[0] + (sensor.radius - abs(sensor.position[1] - y)) + 1
                        f = False
                        break
                if f:
                    pt = (x, y)
                    break
            y += 1
            x = 0
            if pt[0] != -1:
                break   
        return str(pt[0] * 4000000 + pt[1])
    