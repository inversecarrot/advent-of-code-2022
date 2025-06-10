from typing import Generic, List, TypeVar

T = TypeVar('T')

# This abstracts a list of lists that will be traversed row by row
# so it can be accessed by standard coordinates rather than [y][x]

class Grid2D(Generic[T]):
    x_offset: int
    y_offset: int
    grid: List[List[T]]

    def __init__(self, max_x: int, max_y: int, min_x: int = 0, min_y: int = 0, init: T = None):
        width = 1 + max_x - min_x
        height = 1 + max_y - min_y
        self.grid = [[init for _ in range(0, width)] for _ in range(0, height)]
        self.x_offset = min_x
        self.y_offset = min_y

    def get(self, x: int, y: int) -> T:
        return self.grid[y - self.y_offset][x - self.x_offset]
    
    def set(self, x: int, y: int, val: T):
        self.grid[y - self.y_offset][x - self.x_offset] = val

    def getWidth(self) -> int:
        return len(self.grid[0])
    
    def getHeight(self) -> int:
        return len(self.grid)
                  