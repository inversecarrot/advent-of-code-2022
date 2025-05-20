from typing import List, Tuple
import logging

log = logging.getLogger(__name__)


class RopeGrid:
    moves: List[Tuple[int, int]]
    rope: List[Tuple[int, int]]
    length: int
    dimensions: Tuple[int, int]
    dimensions_set: bool
    debug: bool
    def __init__(self, moves: List[Tuple[int, int]], length = 2, debug = False):
        self.moves = moves
        self.rope = [(0,0)] * length
        self.length = length
        self.dimensions_set = False
        self.debug = debug
    
    def get_tail_visits(self) -> int:
        tail_positions = {(0,0)}
        for move in self.moves:
            self.rope[0] = tuple(sum(x) for x in zip(self.rope[0], move))
            for segment in range(1,len(self.rope)):
                self.rope[segment] = self._get_tail_position(self.rope[segment - 1], self.rope[segment])
            tail_positions.add(self.rope[self.length - 1])
            if (self.debug):
                log.debug("\n" + self._get_visual_grid())
        if (self.debug):
            log.debug(self._get_tail_visual_grid(tail_positions))
        return len(tail_positions)

        
    def _get_tail_position(self, head_pos, cur_tail):
        x_change = 0
        y_change = 0

        # Check if we're two spaces away in any direction
        if head_pos[0] > cur_tail[0] + 1:
            x_change = 1
        elif head_pos[0] < cur_tail[0] - 1:
            x_change = -1
        if head_pos[1] > cur_tail[1] + 1:
            y_change = 1
        elif head_pos[1] < cur_tail[1] - 1:
            y_change = -1

        
        if x_change == 0 or y_change == 0:
            # Check if we need to move diagonally and aren't
            if x_change != 0 and head_pos[1] != cur_tail[1]:
                y_change = head_pos[1] - cur_tail[1]
            elif y_change != 0 and head_pos[0] != cur_tail[0]:
                x_change = head_pos[0] - cur_tail[0]
        
        return (cur_tail[0] + x_change, cur_tail[1] + y_change)
    
    def _set_dimensions(self):
        max_x, max_y, cur_x, cur_y = [0,0,0,0]
        for move in self.moves:
            cur_x += move[0]
            cur_y += move[1]
            if cur_x > max_x:
                max_x = cur_x
            if cur_y > max_y:
                max_y = cur_y
        self.dimensions = (max_x + 1, max_y + 1)
        self.dimensions_set = True


    def _get_visual_grid(self) -> str:
        if not self.dimensions_set:
            self._set_dimensions()
        # indexed [y][x]
        matrix = [['.' for x in range(0,self.dimensions[0])] for y in range(0,self.dimensions[1])]
        for x in reversed(range(0, len(self.rope))):
            segment = self.rope[x]
            if x == 0:
                matrix[segment[1]][segment[0]] = 'H'
            else:
                matrix[segment[1]][segment[0]] = f'{x}'
        
        output = '\n'
        for row in matrix:
            for char in row:
                output += char
            output += "\n"

        return output
    
    def _get_tail_visual_grid(self, tail_positions) -> str:
        if not self.dimensions_set:
            self._set_dimensions()
        # indexed [y][x]
        matrix = [['.' for x in range(0,self.dimensions[0])] for y in range(0,self.dimensions[1])]
        for pos in tail_positions:
            matrix[pos[1]][pos[0]] = '#'
        
        output = '\n'
        for row in matrix:
            for char in row:
                output += char
            output += "\n"

        return output


        