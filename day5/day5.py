"""Script to calculate answers for day 5"""
from stacks import SupplyStacks, Crate

def part2(filename: str) -> str:
    """
        Calculates the crates that end on top of each stack assuming each move
        is done all at once
    """
    return part1(filename, True)

def part1(filename: str, is_part_2: bool = False) -> str:
    """
        Calculates the crates that end on top of each stack assuming each move
        is done one by one
    """
    with open(filename, encoding="utf-8") as lines:
        nextline = lines.readline()
        crates = []
        col_count = 0
        set_col_count = False
        while(nextline != '\n'):
            unparsed_crates = nextline.strip("\n")
            crate_index = 0
            column_index = 0
            while(crate_index < len(unparsed_crates)):
                crate = unparsed_crates[crate_index:crate_index + 3]
                if (crate[0] == '['):
                    crates.append(Crate(crate[1], column_index))
                column_index += 1
                crate_index += 4
            if not set_col_count:
                col_count = column_index
                set_col_count = True
            nextline = lines.readline()
        crates.reverse()
        stacks = SupplyStacks(crates, col_count)
        nextline = lines.readline()
        while(nextline != ''):
            command = nextline.strip("\n").split(" ")
            if (is_part_2):
                stacks.process_command_single_move(int(command[1]), int(command[3]), int(command[5]))
            else:
                stacks.process_command_multiple_moves(int(command[1]), int(command[3]), int(command[5]))
            nextline = lines.readline()
        return stacks.get_top_crates()

if __name__ == '__main__':
    print(part1('day5\\input.txt'))
    print(part2('day5\\input.txt'))