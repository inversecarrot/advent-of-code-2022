from typing import List, Tuple

from grid2D import Grid2D


class Cave:
    grid: Grid2D[str]
    sand_origin = (500, 0)
    min_x: int
    max_x: int
    max_y: int

    def __init__(self, min_x: int, max_x: int, max_y: int, lines: List[List[Tuple[int, int]]]):
        self.grid = Grid2D(max_x, max_y, min_x=min_x, init=".")
        self.min_x = min_x
        self.max_x = max_x
        self.max_y = max_y
        for points in lines:
            prev = None
            for cur in points:
                if prev == None:
                    prev = cur
                else:
                    if prev[0] != cur[0]:
                        # horizontal line
                        start = min(prev[0], cur[0])
                        end = max(prev[0], cur[0])
                        for point in [(x, prev[1]) for x in range(start, end + 1)]:
                            self.grid.set(point[0], point[1], "#")
                    else:
                        # vertical line
                        start = min(prev[1], cur[1])
                        end = max(prev[1], cur[1])
                        for point in [(prev[0], y) for y in range(start, end + 1)]:
                            self.grid.set(point[0], point[1], "#")
                    prev = cur
    
    # Returns boolean indicating whether sand successfully came to rest
    def spawnSand(self) -> bool:
        (sand_x, sand_y) = self.sand_origin

        while True:
            next_y = sand_y + 1
            if next_y > self.max_y:
                return False
            if self.grid.get(sand_x, next_y) == ".":
                sand_y = next_y
                continue

            next_x = sand_x - 1
            if next_x < self.min_x:
                return False
            if self.grid.get(next_x, next_y) == ".":
                sand_x = next_x
                sand_y = next_y
                continue

            next_x = sand_x + 1
            if next_x > self.max_x:
                return False
            if self.grid.get(next_x, next_y) == ".":
                sand_x = next_x
                sand_y = next_y
                continue
            
            # At this point, none of the squares we can flow to are open, so we come to rest
            self.grid.set(sand_x, sand_y, "o")
            return True         
