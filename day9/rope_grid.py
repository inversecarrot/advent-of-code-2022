from io import TextIOWrapper



class RopeGrid:
    moves: TextIOWrapper
    def __init__(self, input: TextIOWrapper):
        self.moves = input
    
    def get_tail_visits(self) -> int:
        self.moves.seek(0,0)
        tail_positions = {(0,0)}
        head_pos = (0,0)
        tail_pos = (0,0)
        for move in self.moves:
            steplist = self._parse_move(move)
            for step in steplist:
                head_pos = tuple(sum(x) for x in zip(head_pos, step))
                tail_pos = self._get_tail_position(head_pos, tail_pos)
                tail_positions.add(tail_pos)
        return len(tail_positions)

    def _parse_move(self, line: str):
        move = line.strip("\n").split(" ")
        direction = move[0]
        distance = int(move[1])
        if direction == 'U':
            return [(1,0)] * distance
        elif direction == 'D':
            return [(-1,0)] * distance
        elif direction == 'R':
            return [(0,1)] * distance
        else:
            return [(0,-1)] * distance
        
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

        # Diagonal move if we need to
        if x_change != 0 and head_pos[1] != cur_tail[1]:
            y_change = head_pos[1] - cur_tail[1]
        elif y_change != 0 and head_pos[0] != cur_tail[0]:
            x_change = head_pos[0] - cur_tail[0]
        
        return (cur_tail[0] + x_change, cur_tail[1] + y_change)        
        